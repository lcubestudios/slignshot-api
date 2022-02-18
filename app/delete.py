from classes import *

##Delete Audio ##
db = Database()
method= Methods()

#Pass ids 
id = sys.argv[1]
audio_id = [id]

#Delete audio
method.DeleteAudio(audio_id)
print("Audio with " + id + " has been deleted")