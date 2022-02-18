from classes import *

##GET Audio## 
db = Database()
method= Methods()
id = sys.argv[1]
audio_id = [id]
print(method.LoadSingleAudio(audio_id))
#print(method.LoadAllAudios())