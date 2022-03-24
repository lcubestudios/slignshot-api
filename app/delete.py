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
output = {
	"success": "true", 
	"status": 200, 
	"message": "Record has been deleted.",
	"result": {
		"msg_id": id
	}
}

print(json.dumps(output))