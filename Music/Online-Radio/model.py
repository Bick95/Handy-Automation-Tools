import vlc
import time

from view import View
from helper import load_json, save_json


class LiveStream:

	def __init__(self, database='./data/database.js'):

		self.view = View()

		# Set defaults
		self.settings = {'urls': ['http://rhh.streamabc.net/rhh-rhhlivestream-mp3-192-5434905',
								  'https://stream.antenne1.de/a1stg/livestream2.mp3'],
						 'stations': ['Radio Hamburg', 'Antenne 1'],
						 'vol': 20,
						 'current_channel_id': 0,
						 }

		# Define VLC instance
		self.instance = vlc.Instance('--quiet') #'--input-repeat=-1', '--fullscreen'

		# Define VLC player
		self.player = self.instance.media_player_new()

		self.VOL_MIN = 0
		self.VOL_MAX = 100
		self.VOL_CHANGE = 5

		self.settings = load_json(database, self)

		self.set_channel(self.settings['urls'][self.settings['current_channel_id']])
		self.player.audio_set_volume(self.settings['vol'])

		self.show('Player instentiated.')


	def set_channel(self, url):
		# Define VLC media
		media = self.instance.media_new(url)
		
		# Set player media
		self.player.set_media(media)
		

	def start(self):
		# Play the media
		self.player.play()
		self.show('Player started.')


	def stop(self):
		# Play the media
		self.player.stop()
		self.show('Player stopped.')


	def vol_up(self):
		self.settings['vol'] += self.VOL_CHANGE
		self.player.audio_set_volume(self.settings['vol'])
		self.show('Volume:', self.settings['vol'])


	def vold_down(self):
		self.settings['vol'] -= self.VOL_CHANGE
		self.player.audio_set_volume(self.settings['vol'])
		self.show('Volume:', self.settings['vol'])


	def add_station(self, query_term):
		self.show('Not yet implemented...')


	def channel_up(self):
		current_id = self.settings['current_channel_id']
		next_id = current_id + 1
		num_channels = len(self.settings['urls'])

		if next_id >= num_channels:
			self.settings['current_channel_id'] = 0
		else:
			self.settings['current_channel_id'] = next_id
		
		channel = self.settings['urls'][self.settings['current_channel_id']]
		channel_name = self.settings['stations'][self.settings['current_channel_id']]
		self.set_channel(channel)
		self.show('Channel:', channel_name, ',', channel)


	def channel_down(self):
		current_id = self.settings['current_channel_id']
		next_id = current_id - 1
		last_channel = len(self.settings['urls']) - 1

		if next_id < 0:
			self.settings['current_channel_id'] = last_channel
		else:
			self.settings['current_channel_id'] = next_id
		
		channel = self.settings['urls'][self.settings['current_channel_id']]
		channel_name = self.settings['stations'][self.settings['current_channel_id']]
		self.set_channel(channel)
		self.show('Channel:', channel_name, ',', channel)


	def	close(self):
		self.player.stop()
		save_json('./data/database.js', self.settings, self)
		self.show('Bye Bye!')

	def show(self, *text):
		text = [str(t) for t in text]  # Transform everything to text
		self.view.show(' '.join(text)) # Show text