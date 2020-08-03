import time
from model import LiveStream


def execute(stream, command):
	if command in stream.commands:
		stream.commands[command]()
	else:
		stream.show('Invalid command.')


def terminal_control(stream):

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