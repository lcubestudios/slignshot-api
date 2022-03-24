from classes import *

# Load Classes
db = Database()
method = Methods()
function = CoreFunctions()

# Params
audio_id = sys.argv[1]
id = [audio_id]
file_name="/tmp/tmp_audio_"+str(audio_id)+".wav"

# Load Current Directory
dir=os.getcwd()   
# Get Blob data
data = method.LoadBlob(id)
# Convert Blob to audio
function.WriteFile(data, file_name)
os.system('ffmpeg -i '+file_name+' /tmp/tmp_audio_'+str(audio_id)+'_new.wav')
# Create audio
new_audio = '/tmp/tmp_audio_'+str(audio_id)+'_new.wav'
# Load Duration
duration = function.AudioDuration(new_audio)

# Check if audio is more than a min long
if (duration < 60):
    # list
    audio_list=[]
    # Transcribe audio to text
    transcript = function.SpeechToText(new_audio)
    # Add content to list
    audio_list.append(transcript)
    # Join list
    transcripts="".join(["".join(i) for i in audio_list])
    # Update audio in the database
    method.UpdateAudio(audio_id,transcripts,duration)
    # Output
    content = {
        "msg_id": audio_id, 
        "file_name": file_name, 
        "duration": duration,
        "txtrecording": transcripts
    }
    output = {
        "success": "true", 
        "status": 200, 
        "message": "Record has been updated.", 
        "results": content
    }
else:
    # List
    audio_list = []
    # Split & Transcribe audio to text
    transcripts = function.SplitAudio(new_audio, duration)
    # Update Query
    method.UpdateAudio(audio_id,transcripts,duration)
    # Output
    content = {
        "msg_id": audio_id, 
        "file_name": file_name, 
        "duration": duration,
        "txtrecording": transcripts
    }
    output = {
        "success": "true", 
        "status": 200, 
        "message": "Record has been updated.", 
        "results": content
    }
    
print(json.dumps(output))
#Remove files
os.remove(file_name)
os.remove(new_audio)
