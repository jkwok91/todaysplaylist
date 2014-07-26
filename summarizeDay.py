import soundcloud
import credentials

soundcloud = soundcloud.Client(client_id=credentials.sc_client_id, client_secret=credentials.sc_client_secret, username=credentials.sc_username, password=credentials.sc_passw)
todaysplaylist = soundcloud.get('/playlists/'+credentials.sc_pID)

def getTrax():
  playlist = open('playlist.txt','w')
  trax = todaysplaylist.tracks
  for track in trax:
    title = track['title']
    link = track['permalink_url']
    playlist.write(title+" ("+link+")\n")

getTrax()
