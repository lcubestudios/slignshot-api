from classes import *

# Load Classes
db = Database()
method= Methods()

# Params
id = sys.argv[1]
audio_id = [id]

# Delete Query 
delete = method.DeleteAudio(audio_id)

# Output
content = ("Audio have been deleted")
output = {"success": "true", "status": 200, "results":content, "audio_id": id}
print(output)