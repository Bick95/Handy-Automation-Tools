from model import LiveStream
from gpio_controller import GPIOController


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


def GPIO_control(stream):
    controller = GPIOController(stream.alternate_start_stop,
                                stream.vol_up,
                                stream.vol_down,
                                stream.station_up,
                                stream.station_down,
                                )
    input() # Workaround to keep script alive...


def main():
    stream = LiveStream()
    #terminal_control(stream)
    GPIO_control(stream)


if __name__ == '__main__':
    main()