import vlc
import time

from view import View
from helper import load_json, save_json


class LiveStream:

	def __init__(self, database='./data/database.js'):

		self.view = View()
		self.state = 0  # 0: Radio off, 1: Radio on

		# Set defaults
		self.settings = {'urls': ['http://rhh.streamabc.net/rhh-rhhlivestream-mp3-192-5434905',
								  'https://stream.antenne1.de/a1stg/livestream2.mp3'],
						 'stations': ['Radio Hamburg', 'Antenne 1'],
						 'vol': 20,
						 'current_station_id': 0,
						 }

		# Define VLC instance
		self.instance = vlc.Instance('--quiet') #'--input-repeat=-1', '--fullscreen'

		# Define VLC player
		self.player = self.instance.media_player_new()

		self.VOL_MIN = 0
		self.VOL_MAX = 100
		self.VOL_CHANGE = 5

		self.settings = load_json(database, self)

		self.set_station(self.settings['urls'][self.settings['current_station_id']])
		self.player.audio_set_volume(self.settings['vol'])

		# Define possible action commands (how to use stream)
		self.commands = {
			'start': 		self.start,
			'stop':  		self.stop,
			'station_up': 	self.station_up,
			'station_down':	self.station_down,
			'vol_up':		self.vol_up,
			'vol_down':		self.vol_down,
			'close':		self.close,
		}

		self.show('Player instentiated.')


	def show_options(self):
		self.view.show_options(self)


	def set_station(self, url):
		# Define VLC media
		media = self.instance.media_new(url)
		
		# Set player media
		self.player.set_media(media)
		

	def start(self):
		# Play the media
		self.player.play()
		self.state = 1
		self.show('Player started.')


	def stop(self):
		# Play the media
		self.player.stop()
		self.state = 0
		self.show('Player stopped.')


	def vol_up(self):
		self.settings['vol'] += self.VOL_CHANGE
		self.player.audio_set_volume(self.settings['vol'])
		self.view.show_vol(self.settings['vol'])


	def vol_down(self):
		self.settings['vol'] -= self.VOL_CHANGE
		self.player.audio_set_volume(self.settings['vol'])
		self.view.show_vol(self.settings['vol'])


	def add_station(self, query_term):
		# TODO
		self.show('Not yet implemented...')

	def remove_station(self):
		pass


	def station_up(self):
		current_id = self.settings['current_station_id']
		next_id = current_id + 1
		num_stations = len(self.settings['urls'])

		if next_id >= num_stations:
			self.settings['current_station_id'] = 0
		else:
			self.settings['current_station_id'] = next_id
		
		url = self.settings['urls'][self.settings['current_station_id']]
		station_name = self.settings['stations'][self.settings['current_station_id']]
		self.set_station(url)
		if self.state:
			self.start()
		self.view.show_station(station_name, url)


	def station_down(self):
		current_id = self.settings['current_station_id']
		next_id = current_id - 1
		last_station = len(self.settings['urls']) - 1

		if next_id < 0:
			self.settings['current_station_id'] = last_station
		else:
			self.settings['current_station_id'] = next_id
		
		url = self.settings['urls'][self.settings['current_station_id']]
		station_name = self.settings['stations'][self.settings['current_station_id']]
		self.set_station(url)
		if self.state:
			self.start()
		self.view.show_station(station_name, url)


	def	close(self):
		self.player.stop()
		save_json('./data/database.js', self.settings, self)
		self.show('Bye Bye!')


	def show(self, *text):
		text = [str(t) for t in text]  # Transform everything to text
		self.view.show(' '.join(text)) # Show text