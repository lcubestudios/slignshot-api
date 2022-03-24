from cgi import print_form
from xxlimited import new
import mysql.connector
from mysql.connector import Error
from google.cloud import speech
import os
from os import path
from dotenv import load_dotenv
import sys
import audioread
import io
import re
import json

 # LOAD CONTAINER VARIABLES
load_dotenv()

class Database:
    my_db = my_cursor = None
    def __init__(self):
        global my_db, my_cursor
        my_db = mysql.connector.connect(
            host=os.getenv("DATABASE_HOST"),
            user=os.getenv("DATABASE_USER"),
            password=os.getenv("DATABASE_USER_PASSWORD"),
            database=os.getenv("DATABASE_NAME"),
            port=os.getenv("DATABASE_PORT"),
            auth_plugin='mysql_native_password'
        )
        my_cursor = my_db.cursor()

    def __del__(self):
        my_db.commit()
    
class Methods:
    def LoadSingleAudio(self, audio_id):
        sql= "SELECT msg_id,msgnum,dir,context,macrocontext,callerid,origtime,duration,mailboxuser,mailboxcontext,txtrecording,flag,audioname,lastmodify FROM ast_voicemessages WHERE msg_id=%s"
        #sql= "SELECT * FROM ast_voicemessages WHERE msg_id=%s"        
        try:
            my_cursor.execute(sql, audio_id)
            result = [dict((my_cursor.description[i][0], str(value)) \
                for i, value in enumerate(row)) 
                    for row in my_cursor.fetchall()
            ][0]

            my_cursor.close()
        except Exception as e:
            return e
        return result

    def LoadAllAudios(self):
        sql= "SELECT msg_id,msgnum,dir,context,macrocontext,callerid,origtime,duration,mailboxuser,mailboxcontext,txtrecording,flag,audioname,lastmodify FROM ast_voicemessages"
        try:
            my_cursor.execute(sql)
            result = my_cursor.fetchall()
            my_cursor.close()
        except Exception as e:
            return e
        return result
    
    def LoadBlob(self,audio_id):
        sql = "select recording from ast_voicemessages where msg_id=%s"
        my_cursor.execute(sql,audio_id)
        data = my_cursor.fetchone()[0]
        return data

    def LoadEmptyTxtRecording(self):
        sql = "select msg_id from ast_voicemessages where txtrecording IS NULL"
        my_cursor.execute(sql)
        data = my_cursor.fetchall()
        return data
    
    def InsertNewAudio(self,file,dir,transcript,blob,duration):
        sql = "insert into ast_voicemessages (audioname,dir,txtrecording,recording,duration,lastmodify) values (%s,%s,%s,%s,%s,CURTIME())"
        data =(file,dir,transcript,blob,duration)
        my_cursor.execute(sql,data)
        
    def UpdateAudio(self, audio_id, transcript,duration):
        sql= "update ast_voicemessages set txtrecording=%s,duration=%s,audioname=%s,lastmodify=CURTIME() where msg_id=%s"
        new_audioname = "Audio_"+ str(audio_id)
        data = (transcript,duration,new_audioname,audio_id)
        my_cursor.execute(sql,data)

    def DeleteAudio(self,audio_id):
        sql = "Delete from ast_voicemessages where msg_id = %s"
        my_cursor.execute(sql, audio_id)


class CoreFunctions:
    def SpeechToText(self,file_name):
        
        # Creates google client
        #client = speech.SpeechClient.from_service_account_file('/home/kira/projects/slingshot/slingshot-api/key.json')
        client = speech.SpeechClient()

        with open(file_name, "rb") as f:
            content = f.read()
            audio = speech.RecognitionAudio(content=content)
            config = speech.RecognitionConfig(
            language_code="en-US"
        )
        # Sends the request to google to transcribe the audio
        operation = client.long_running_recognize(config=config, audio=audio)
        response = operation.result(timeout=90)
        
        audio_list=[]

        for result in response.results:
            for alt in result.alternatives:
                text_audio = alt.transcript
                audio_list.append(text_audio)
                
        return audio_list

    # Convert Audio to Binary 
    def ConvertToBinary(self,file):
        with open(file,'rb') as file:
            binarydata=file.read()
        return binarydata
    
    # Convert Binary to Audio
    def WriteFile(self, data,file_name):
        with open(file_name, 'wb') as f:
            f.write(data)
            
    #Load Audio Duration
    def AudioDuration(self,file):  
        with audioread.audio_open(file) as f:
            # totalsec contains the length in float
            audio = f.duration
            total_length=(int(audio))
            return (total_length)
        
    #Split Audio
    def SplitAudio(self, file, duration):
        segmentbysec = 59
        audio_list = []
        
        for i in range(0, duration, segmentbysec):
            segments = i + segmentbysec
            newaudioname = "temp-audio-" + str(i)+ "-" + str(segments) + ".wav"
            os.system("ffmpeg -y -hide_banner -loglevel error -i "+file+" -ss "+str(i)+" -t "+str(segmentbysec)+" "+newaudioname)
            audio_list2=self.SpeechToText(newaudioname)
            audio_list.append(audio_list2)
            os.system("rm "+ newaudioname)

        text="".join([" ".join(i) for i in audio_list])
        return text
