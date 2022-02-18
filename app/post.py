from classes import *

##Insert New Audios##
##POST##

db = Database()
method = Methods()
function = CoreFunctions()

#Bash scripts passes these variables 
file=sys.argv[1]
dir=sys.argv[2]
file_total=dir+"/"+file
##Transcribe audio to text
transcript = function.SpeechToText(file_total)
#print(transcript)

##Convert Audio to blob
blob = (function.ConvertToBinary(dir+"/"+file))
#print(blob)

##Audio Duration
duration = function.AudioDuration(file)
#print(duration)

method.InsertNewAudio(file,dir,transcript,blob,duration)
print("New Audio has been transcribed ")
