from classes import *

# Load Classes
db = Database()
method = Methods()
function = CoreFunctions()
dir=os.getcwd()   

# Check for all empty voicemails
data = method.LoadEmptyTxtRecording()
count = len(data)

# has empty voicemails
if (count > 0):
    content = []
    # Loop audios
    for ndx, item in enumerate(data):
        content.append({})
        # Load id 
        audio_id=item[0]
        # Add audio to list
        id = [audio_id]
        # Default audio Name
        file_name="/tmp/tmp_audio_"+str(audio_id)+".wav"
        # Process 
        #print("Downloading audio")
        # Convert Blob to audio
        data = method.LoadBlob(id)
        # Process 2
        #print("Converting blob to audio")
        function.WriteFile(data, file_name)
        os.system('ffmpeg -y -i '+file_name+' /tmp/tmp_audio_'+str(audio_id)+'_new.wav')
        # temporary audio name
        new_audio = '/tmp/tmp_audio_'+str(audio_id)+'_new.wav'
        # Load Duration
        duration = function.AudioDuration(new_audio)
        
        if (duration < 60):
            # Transcribe audio to text
            transcripts = function.SpeechToText(new_audio)[0]
            # Update audio in the database
            method.UpdateAudio(audio_id,transcripts,duration)
            # Output
            content[ndx] = {
                "msg_id": audio_id, 
                "audioname": file_name, 
                "duration": duration,
                "txtrecording": transcripts
            }
        else:
            # Split & Transcribe audio to text
            transcripts = function.SplitAudio(new_audio, duration)
            # Update Query
            method.UpdateAudio(audio_id,transcripts,duration)
            # Output
            content[ndx] = {
                "msg_id": audio_id, 
                "audioname": file_name, 
                "duration": duration,
                "txtrecording": transcripts
            }
# no empty voicemails
else:
    content = []

output = {
    "success": "true", 
    "status": 200, 
    "message": str(count) + " record(s) have been updated.",
    "results": content
}

        
print(json.dumps(output))
#Remove files
os.remove(file_name)
os.remove(new_audio)
# Close SQL Connection
my_cursor.close()
