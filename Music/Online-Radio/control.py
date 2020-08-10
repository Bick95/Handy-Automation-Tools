#!/usr/local/bin/python3.8
import sys
sys.path.insert(0,'/home/pi/.local/lib/python3.8/site-packages'); # Make packages available, since otherwise RPI or vlc wouldn't be found

from model import LiveStream

try:
    from gpio_controller import GPIOController
    gpio = True
except Exception:
    print('No GPIO available!')
    gpio = False


with open("/home/pi/Downloads/Handy-Automation-Tools/Music/Online-Radio/controllllllxxxxx1.txt", "w") as outfile:
    outfile.write("hello")
        
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
    #input() # Workaround to keep script alive...
    while True:  # To keep script alive...
        pass
    stream.close()


def main():
    stream = LiveStream()
    if gpio:
        GPIO_control(stream)
    else:
        terminal_control(stream)
        

if __name__ == '__main__':
    main()
    
    with open("/home/pi/Downloads/Handy-Automation-Tools/Music/Online-Radio/controllllllxxxxx1.txt", "w") as outfile:
        outfile.write("Cioa!")