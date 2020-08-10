import time
import RPi.GPIO as GPIO


class GPIOController:

    def __init__(self,
                 on_off_action,
                 vol_up_action,
                 vol_down_action,
                 station_up_action,
                 station_down_action,
                 save_state_action
                 ):
        
        # Init GPIO
        GPIO.setmode(GPIO.BCM)
    
        # Define constants
        INITIAL_VAL = GPIO.LOW
        CURRENT_VAL = GPIO.LOW


        # Indicative LED GPIO Pins - Init
        # Station -
        GPIO.setup(18, GPIO.OUT, initial=INITIAL_VAL)  # Set pin as output
        GPIO.output(18, CURRENT_VAL)

        # Station up
        GPIO.setup(23, GPIO.OUT, initial=INITIAL_VAL)  # Set pin as output
        GPIO.output(23, CURRENT_VAL)

        # Vol -
        GPIO.setup(24, GPIO.OUT, initial=INITIAL_VAL)  # Set pin as output
        GPIO.output(24, CURRENT_VAL)

        # Vol +
        GPIO.setup(25, GPIO.OUT, initial=INITIAL_VAL)  # Set pin as output
        GPIO.output(25, CURRENT_VAL)

        # On/Off
        GPIO.setup(12, GPIO.OUT, initial=INITIAL_VAL)  # Set pin as output
        GPIO.output(12, CURRENT_VAL)
        
        
        self.gpio_greeting()
        

        # Switch GPIO Pins - Init

        # On/Off
        GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        GPIO.add_event_detect(26, GPIO.BOTH) # Which switch's action-event to detect - RISING, FALLING or BOTH

        def callback_on_off(x):
            GPIO.output(12, GPIO.input(26))
            if GPIO.input(26):
                print('On/Off!', x)
                on_off_action()
                save_state_action()

        GPIO.add_event_callback(26, callback_on_off)
        
        
        # Vol +
        GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        GPIO.add_event_detect(13, GPIO.BOTH) # Which switch's action-event to detect - RISING, FALLING or BOTH

        def callback_vol_up(x):
            GPIO.output(25, GPIO.input(13))
            if GPIO.input(13):
                print('Vol up!', x)
                vol_up_action()
                save_state_action()

        GPIO.add_event_callback(13, callback_vol_up)
        

        # Vol -
        GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        GPIO.add_event_detect(22, GPIO.BOTH) # Which switch's action-event to detect - RISING, FALLING or BOTH

        def callback_vol_down(x):
            GPIO.output(24, GPIO.input(22))
            if GPIO.input(22):
                print('Vol down!', x)
                vol_down_action()
                save_state_action()

        GPIO.add_event_callback(22, callback_vol_down)


        # Station +
        GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        GPIO.add_event_detect(27, GPIO.BOTH) # Which switch's action-event to detect - RISING, FALLING or BOTH

        def callback_station_up(x):
            GPIO.output(23, GPIO.input(27))
            if GPIO.input(27):
                print('Station up!', x)
                station_up_action()
                save_state_action()

        GPIO.add_event_callback(27, callback_station_up)


        # Station -
        GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        GPIO.add_event_detect(4, GPIO.BOTH) # Which switch's action-event to detect - RISING, FALLING or BOTH

        def callback_station_down(x):
            GPIO.output(18, GPIO.input(4))
            if GPIO.input(4):
                print('Station down!', x)
                station_down_action()
                save_state_action()

        GPIO.add_event_callback(4, callback_station_down)
        
    
    def gpio_set_all(self, status):
        # Set all connected LEDs to same on/off status
        GPIO.output(12, status)
        GPIO.output(18, status)
        GPIO.output(23, status)
        GPIO.output(24, status)
        GPIO.output(25, status)
        
        
    def gpio_greeting(self):
        # Let LEDs light up on startup to indicate waiting for command
        self.gpio_set_all(GPIO.LOW)
        self.gpio_set_all(GPIO.HIGH)
        time.sleep(0.5)
        self.gpio_set_all(GPIO.LOW)
        time.sleep(0.4)
        self.gpio_set_all(GPIO.HIGH)
        time.sleep(0.5)
        self.gpio_set_all(GPIO.LOW)
    
