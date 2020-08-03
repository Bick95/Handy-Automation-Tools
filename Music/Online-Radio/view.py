
class View:

	def __init__(self):
		pass


	def show(self, content):
		print(content)


	def show_options(self, stream):
		text = '\nOptions: You may enter any command after a colon.' + '\n\n'

		text += 'Start: \t\tstart' + '\n'
		text += 'Stop: \t\tstop' + '\n'

		text += 'Volume up: \tvol_up' + '\n'
		text += 'Volume down: \tvol_down' + '\n'

		text += 'Station up: \tstation_up' + '\n'
		text += 'Station down: \tstation_down' + '\n'

		text += 'Close radio: \tclose' + '\n'

		text += '\nEnd.' + '\n'

		print(text)


	def show_vol(self, vol):
		print('Volume:', vol)

	def show_station(self, station, url):
		print('station:', station, ',', url)

