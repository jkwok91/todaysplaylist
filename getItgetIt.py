#using lastfm because it has a more comprehensive group of songs. but idk man, this means i have to manually add the shit into a playlist, just like i would have to if i manually typed out the playlist. and it doesnt come with a link and shit like soundcloud does.
#worst of every world, man.

import pylast
import credentials

lastfm = pylast.LastFMNetwork(api_key=credentials.lf_api_key, api_secret=credentials.lf_api_secret, username=credentials.lf_username, password_hash=pylast.md5(credentials.lf_passw))
me = lastfm.get_user(credentials.lf_username)
todaysplaylist = me.get_playlists()[0] 

def getTrax():
  playlist = open('playlist.txt','w')
  tracks = todaysplaylist.get_tracks()
  for track in tracks:
    playlist.write(str(track)+"\n")

getTrax()
