import time
from model import LiveStream

stream = LiveStream()
stream.start()

time.sleep(2)

stream.stop()

time.sleep(2)

stream.start()

time.sleep(2)

stream.channel_up()

time.sleep(2)

stream.stop()

stream.channel_up()

time.sleep(2)

stream.start()

time.sleep(2)

stream.vol_up()

time.sleep(2)

stream.close()
