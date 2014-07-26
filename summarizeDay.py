import soundcloud
import credentials

soundcloud = soundcloud.Client(client_id=credentials.client_id, client_secret=credentials.client_secret, username=credentials.username, password=credentials.passw)
todaysplaylist = soundcloud.get('/playlists/'+credentials.pID)

def getTrax():
  playlist = open('playlist.txt','w')
  trax = todaysplaylist.tracks
  for track in trax:
    title = track['title']
    link = track['permalink_url']
    playlist.write(title+" ("+link+")\n")

getTrax()
