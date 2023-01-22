import discord
import speech_recognition as sr 
import os
from pydub import AudioSegment 
from pydub.silence import split_on_silence

client = discord.Client()
modcanalid = bot.get_channel()
canal = ""
words = []
path = discord.PCMAudio(stream)
reco = open("reco.txt", "r")

def silence_based_conversion(path): 
  song = AudioSegment.from_wav(path) 
  fh = open("reco.txt", "w+") 
  chunks = split_on_silence(song,  
    min_silence_len = 500,  
    silence_thresh = -16
  )
  try: 
	  os.mkdir('audio_chunks')
  except(FileExistsError):
	  pass
  i = 0
  for chunk in chunks:
		chunk_silent = AudioSegment.silent(duration = 10)
		audio_chunk = chunk_silent + chunk + chunk_silent
		audio_chunk.export("./chunk{0}.wav".format(i), bitrate ='192k', format ="wav") 
		filename = 'chunk'+str(i)+'.wav'
		file = filename 
		r = sr.Recognizer() 
		with sr.AudioFile(file) as source: 
			r.adjust_for_ambient_noise(source) 
			audio_listened = r.listen(source) 
		try: 
			rec = r.recognize_google(audio_listened) 
			fh.write(rec+". ") 
		i += 1
	os.chdir('..') 

silence_based_conversion(path)

@client.event
async def on_ready():
    print('Iniciado en {0.user}'.format(client))

if words in reco.read():
  message.chane
  message.reply("")
  await channel.message.send("Se han mencionado palabras malsonantes en " + canal)
try:
    client.run(os.getenv("TOKEN"))
except discord.HTTPException as e:
    if e.status == 429:
        print("Muchas request")
        print("Aqui una ayudita https://stackoverflow.com/questions/66724687/in-discord-py-how-to-solve-the-error-for-toomanyrequests")
    else:
        raise e