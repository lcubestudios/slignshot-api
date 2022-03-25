from classes import *

# Load Classes
db = Database()
method = Methods()
function = CoreFunctions()

# Params
files=sys.argv[1]
dir=sys.argv[2]

array=files.split(',')[:-1]
count=len(array)

content = []

if (count > 0):
    for file in array:
        file_name = dir+"/"+file
        # Convert Audio to blob
        blob = (function.ConvertToBinary(file_name))

        # Audio Duration
        duration = function.AudioDuration(file)
        
        if (duration < 60):
            # Transcribe audio to text (google api)
            transcripts = function.SpeechToText(file)[0]
            # Insert audio in the database
            method.InsertNewAudio(file,dir,transcripts,blob,duration)
            # Output
            content.append({
                "audioname": file, 
                "dir": dir, 
                "duration": duration,
                "txtrecording": transcripts
            })
            
        else:
            # Split & Transcribe audio to text
            transcripts = function.SplitAudio(file, duration)
            # Insert to database
            method.InsertNewAudio(file,dir,transcripts,blob,duration)
            # Output
            content.append({
                "audioname": file, 
                "dir": dir, 
                "duration": duration,
                "txtrecording": transcripts
            })
        # Remove files
        os.remove(file_name)

output = {
    "success": "true", 
    "status": 200, 
    "message": str(count) + " record(s) has been added.",
    "results": content
}

print(json.dumps(output))
# Close SQL Connection
my_cursor.close()