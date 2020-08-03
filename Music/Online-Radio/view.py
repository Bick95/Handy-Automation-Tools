
class View:

	def __init__(self):
		pass


	def show(self, content):
		print(content)


	def show_options(self, stream):
		text = '\nOptions: You may enter any command after a colon.' + '\n\n'

		for option in stream.commands.keys():
			command = (option[0].upper()+option[1:]).replace('_', ' ')
			text += command + ':' + '\t' + ('\t' if len(command) < 8 else '') + option + '\n'

		text += '\nEnd options.' + '\n'

		print(text)


	def show_vol(self, vol):
		print('Volume:', vol)


	def show_station(self, station, url):
		print('station:', station, ',', url)


	def show_station_list(self, station_names, urls):
		for i in range(len(station_names)):
			print('[' + str(i) + ']\t', station_names[i] + ',\t' + urls[i])

