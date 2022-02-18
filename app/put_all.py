from classes import *

## Edit audio ##
db = Database()
method = Methods()
function = CoreFunctions()

dir=os.getcwd()   
data = method.LoadEmptyTxtRecording()
for item in data:
    audio_id=item[0]
    id_to_download=str(audio_id)
    id = [audio_id]
    file_name="/tmp/tmp_audio_"+str(audio_id)+".wav"
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
