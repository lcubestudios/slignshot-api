from cgi import print_form
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
            port=os.getenv("DATABASE_PORT")
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
            result = my_cursor.fetchone()
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
        sql = "insert into ast_voicemessages (audioname,dir,txtrecording,recording,duration,lastmodify) value (%s,%s,%s,%s,%s,CURTIME())"
        data =(file,dir,transcript,blob,duration)
        #print(data)
        my_cursor.execute(sql,data)
        my_cursor.close()

    def UpdateAudio(self, audio_id, transcript,duration):
        sql= "update ast_voicemessages set txtrecording=%s,duration=%s,audioname=%s,lastmodify=CURTIME() where msg_id=%s"
        new_audioname = "Audio_"+ str(audio_id)
        data = (transcript,duration,new_audioname,audio_id)
        my_cursor.execute(sql,data)

    def DeleteAudio(self,audio_id):
        sql = "Delete from ast_voicemessages where msg_id = %s"
        my_cursor.execute(sql, audio_id)


class CoreFunctions:
    def SpeechToText(self,file):
        # Creates google client
        client = speech.SpeechClient()

        # Full path of the audio file, Replace with your file name
        file_name = os.path.join(os.path.dirname(__file__),file)

        #Loads the audio file into memory
        with io.open(file_name, "rb") as audio_file:
            content = audio_file.read()
            audio = speech.RecognitionAudio(content=content)

        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            audio_channel_count=1,
            language_code="en-US",
        )

        # Sends the request to google to transcribe the audio
        response = client.recognize(request={"config": config, "audio": audio})

        # Reads the response
        for result in response.results:
            #print("Transcript: {}".format(result.alternatives[0].transcript))
            text_audio="{}".format(result.alternatives[0].transcript)
            return text_audio

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
        # Audio length function
        def DurationDetector(length):
            hours = length // 3600  # calculate in hours
            length %= 3600
            mins = length // 60  # calculate in minutes
            length %= 60
            seconds = length  # calculate in seconds
            return hours, mins, seconds

        with audioread.audio_open(file) as f:
            # totalsec contains the length in float
            audio = f.duration
            hours, mins, seconds = DurationDetector(int(audio))
            #print('Total Duration: {}:{}:{}'.format(hours, mins, seconds))
            total_length=('{}:{}:{}'.format(hours, mins, seconds))
            return (total_length)
