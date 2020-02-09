import re
import os
import time
import wave
import subprocess
import shlex
from subprocess import Popen, PIPE
from threading import Timer
from pathlib import Path
from datetime import datetime

"""
    This script allows for recording the sound sent to the AUX output of a computer for a given period of time. 
    The resulting sound file is then saved as a .waw file. Sampling frequeny can be chosen freely.
    
    Used underlying shell command: >>timeout 5 pacat --record -d alsa_output.pci-0000_00_1f.3.analog-stereo.monitor | sox -t raw -r 44100 -s -L -b 16 -c 2 - "~/Musik/output.wav"<<
    
    Tested on Ubuntu 16.04
    Requires: sox; get it via: sudo apt-get install sox
"""

# refs: https://docs.python.org/3/library/subprocess.html | https://stackabuse.com/executing-shell-commands-with-python/ | 
#       http://www.circuitbasics.com/how-to-write-and-run-a-shell-script-on-the-raspberry-pi/

## Select audio source

# Retrieve info about sound services
process = subprocess.Popen(args=['pacmd', 'list', '|', 'grep', '".monitor"'], shell=False, stdout=subprocess.PIPE)
output, _ = process.communicate()

# Filter output for module/region of interest
roi = re.search('sources:(.+?)/#0: Monitor of Built-in Audio Analog Stereo', str(output))
module = roi.groups()[0][roi.groups()[0].find('alsa_'):]
print('Module to listen to:', module)


## Record

# Set suond file name and save path/folder
now = datetime.now()
TIME_STAMP = now.strftime("_%Y_%d_%m__%H_%M_%S__%f")

home_dir = str(Path.home())
folder = '/Musik' # must be located in home directory or path specified as of there
path = home_dir + folder
# Make sure folder exists
if not os.path.exists(path):
    os.makedirs(path)
    print('Created dir: ' + path)
    
# Create dummy wave file - To output actual contents into
file_name = 'output' + TIME_STAMP + '.wav'
print('Output file: ~/' + path + '/' + file_name)
os.system('timeout 0.1 rec  ' + '~/' + folder + '/' + file_name)

# Start recording
timeout = 21720         # Record time. Here: Timeout in seconds: 6h * 60min * 60sec = 21600sec + 2min = 21720; else: None
frequency = 44100       # Sampling frequency

command = 'timeout ' + str(timeout) + ' pacat --record -d ' + module + ' | sox -t raw -r ' + str(frequency) + ' -s -L -b 16 -c 2 - "~/' + folder + '/' + file_name + '"'
try:
    os.system(command)
except Exception(e):
    print('Exception:', e)
                 
print('Done.')
