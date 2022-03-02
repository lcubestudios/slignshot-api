from classes import *

# Load Classes
db = Database()
method = Methods()
function = CoreFunctions()
dir=os.getcwd()   

# Check for all empty voicemails
data = method.LoadEmptyTxtRecording()

# Loop audios
for item in data:
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
        content = (audio_id, file_name, transcripts, duration)
        output = {"success": "true", "status": 200, "results":content}
    else:
        # List
        audio_list = []
        # Split & Transcribe audio to text
        transcripts = function.SplitAudio(new_audio, duration)
        # Update Query
        method.UpdateAudio(audio_id,transcripts,duration)
        # Output
        content = (audio_id, file_name, transcripts, duration)
        output = {"success": "true", "status": 200, "results":content}
        
    print(output)
    #Remove files
    os.remove(file_name)
    os.remove(new_audio)
