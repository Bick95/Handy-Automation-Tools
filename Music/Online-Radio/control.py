import time
from model import LiveStream


def execute(stream, command):
	switch(command){
		case 'start':
			stream.start()
			break
		case 'stop':
			stream.stop()
			break
		case 'station_up':
			stream.station_up()
			break
		case 'station_down':
			stream.station_down()
			break
		case 'vol_up':
			stream.vol_up()
			break
		case 'vol_down':
			stream.vol_down()
			break
		case 'close':
			stream.close()
			break
		default:
		       stream.show('Invalid command.')
   }

def terminal_control(stream):

	stream.show_options()

	command = ''

	while not command is 'close':
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