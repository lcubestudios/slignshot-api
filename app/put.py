from classes import *

## Edit audio ##
db = Database()
method = Methods()
function = CoreFunctions()
audio_id = sys.argv[1]
id = [audio_id]
#audio_id = 1642295306
#id = [1642295306]

file_name="/tmp/tmp_audio_"+str(audio_id)+".wav"
dir=os.getcwd()   
data = method.LoadBlob(id)
function.WriteFile(data, file_name)
os.system('ffmpeg -i '+file_name+' /tmp/tmp_audio_'+str(audio_id)+'_new.wav')
new_audio = '/tmp/tmp_audio_'+str(audio_id)+'_new.wav'
duration = function.AudioDuration(new_audio)
minimun_length = "0:0:3"
if duration < minimun_length:
    tanscript=""
    print("Empty voicemail")
else:
    transcript = function.SpeechToText(new_audio)
    print("done")

method.UpdateAudio(audio_id,transcript,duration)
os.remove(file_name)
os.remove(new_audio)
