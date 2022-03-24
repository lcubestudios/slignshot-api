from classes import *

##Load Classes
db = Database()
method= Methods()

# Params
id = sys.argv[1]
audio_id = [id]

# Load Audio info
content = method.LoadSingleAudio(audio_id)

# Check if ID Exists
if (content):
    output = {
        "success": "true", 
        "status": 200,
        "message": "Record Found.", 
        "results": content
    }
else:
    output = {
        "success": "false", 
        "status": 404, 
        "message": "Record Not Found.",
        "result": None
    }

print(json.dumps(output))
