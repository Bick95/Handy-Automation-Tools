# Retrieved from https://stackoverflow.com/a/46782229/11478452
import vlc
import time

#url = 'http://rhh.streamabc.net/rhh-rhhlivestream-mp3-192-5434905'
#url = 'https://stream.antenne1.de/a1stg/livestream2.mp3'

#define VLC instance
#instance = vlc.Instance('--quiet') #'--input-repeat=-1', '--fullscreen'

#Define VLC player
#player=instance.media_player_new()

#Define VLC media
#media=instance.media_new(url)

#Set player media
#player.set_media(media)

#Play the media
#player.play()
#time.sleep(9)
#player.stop()

class LiveStream():

	def __init(database='./data/database.js')__:

		# Set defaults
		self.settings = {'urls'=['http://rhh.streamabc.net/rhh-rhhlivestream-mp3-192-5434905'],
						 'vol'=20,
						 'current_channel_id'=0,
						 }

		# Define VLC instance
		self.instance = vlc.Instance('--quiet') #'--input-repeat=-1', '--fullscreen'

		# Define VLC player
		self.player = instance.media_player_new()

		self.VOL_MIN = 0
		self.VOL_MAX = 100
		self.VOL_CHANGE = 10

		try:
			# Load settings, including station list
			with open('./data/database.js', 'w') as f:
				self.settings = json.load(f)

		except Exception as e:
			print('Exception occured:\n', e)

		# Testing
		self.set_channel(self.settings['urls'][self.settings['current_channel_id']])
		self.player.audio_set_volume(self.settings['vol'])
		self.start_stream()
		time.sleep(10)
		self.vol_up()
		self.player.audio_set_volume(self.settings['vol'])
		time.sleep(10)
		self.vol_up()
		self.player.audio_set_volume(self.settings['vol'])
		time.sleep(10)
		self.vol_up()
		self.player.audio_set_volume(self.settings['vol'])
		time.sleep(10)
		self.vol_up()
		self.player.audio_set_volume(self.settings['vol'])
		time.sleep(10)
		self.player.stop()


	def set_channel(url):
		# Define VLC media
		media = self.instance.media_new(url)
		
		# Set player media
		self.player.set_media(media)

	def start_stream():
		# Play the media
		self.player.play()

	def stop_stream():
		# Play the media
		self.player.stop()

	def vol_up():
		self.settings['vol'] += self.VOL_CHANGE
		player.audio_set_volume(self.settings['vol'])

	def vold_down():
		self.settings['vol'] -= self.VOL_CHANGE
		player.audio_set_volume(self.settings['vol'])

	def add_station(query_term):
		pass

	def	close():
		self.player.stop()
		with open('./data/database.js', 'w') as f:
    		json.dump(team, f)
