# Retrieved from https://stackoverflow.com/a/46782229/11478452
import vlc
import time

url = 'http://rhh.streamabc.net/rhh-rhhlivestream-mp3-192-5434905'
#url = 'https://stream.antenne1.de/a1stg/livestream2.mp3'

#define VLC instance
instance = vlc.Instance('--quiet') #'--input-repeat=-1', '--fullscreen'

#Define VLC player
player=instance.media_player_new()

#Define VLC media
media=instance.media_new(url)

#Set player media
player.set_media(media)

#Play the media
player.play()
time.sleep(9)
player.stop()