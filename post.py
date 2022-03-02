from classes import *

# Load Classes
db = Database()
method = Methods()
function = CoreFunctions()

# Params
file=sys.argv[1]
dir=sys.argv[2]

# Convert Audio to blob
blob = (function.ConvertToBinary(dir+"/"+file))

# Audio Duration
duration = function.AudioDuration(file)

if (duration < 60):
    # List
    audio_list=[]
    # Transcribe audio to text (google api)
    transcript = function.SpeechToText(file)
    # Add content to list
    audio_list.append(transcript)
    # Join list
    transcripts="".join(["".join(i) for i in audio_list])
    # Insert audio in the database
    method.InsertNewAudio(file,dir,transcripts,blob,duration)
    # Output
    content = (file, dir, transcripts, duration)
    output = {"success": "true", "status": 200, "results":content}

else:
    # List
    audio_list = []
    # Split & Transcribe audio to text
    transcripts = function.SplitAudio(file, duration)
    # Insert to database
    method.InsertNewAudio(file,dir,transcripts,blob,duration)
    # Output
    content = (file, dir, transcripts , duration)
    output = {"success": "true", "status": 200, "results":content}

print(output) 