import time
from model import LiveStream


def execute(stream, command):
	switch = {
		'start': 		stream.start,
		'stop':  		stream.stop,
		'station_up': 	stream.station_up,
		'station_down':	stream.station_down,
		'vol_up':		stream.vol_up,
		'vol_down':		stream.vol_down,
		'close':		stream.close,
	}
	if command in switch:
		switch[command]()
	else:
		stream.show('Invalid command.')


def terminal_control(stream):

	stream.show_options()

	command = ''

	while command != 'close':
		stream.show_options()
		command = input()

		execute(stream, command)

def GPIO_control():
	pass


def main():
	stream = LiveStream()
	terminal_control(stream)

if __name__ == '__main__':
	main()