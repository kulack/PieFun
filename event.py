import RPi.GPIO as GPIO
import time

print("Starting with board revision %s" % GPIO.RPI_REVISION)

# Use raspberry pi board pin numbers
GPIO.setmode(GPIO.BOARD)

# These are the available buttons and the pins they are on
one=35
two=37
three=22
four=40
five=36
six=38
seven=18

inputs = [ one, two, three, four, five, six, seven ]
outputs = { one   : 'fire # 1',
            two   : 'fire # 2',
            three : 'fire # 3',
            four  : 'fire # 4',
            five  : 'fire # 1 and 4',
            six   : 'fire # 2 and 3',
            seven : 'fire ALL' }


def trigger1(channel):
    print("Button pressed pin=%s  %s" % (str(channel), outputs[channel]))

try:
    # Set up GPIO channels as input or output
    for pin in inputs:
        print("Turning on input triggers for pin %d" % pin)
        GPIO.setup(pin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        GPIO.add_event_detect(pin, GPIO.RISING, callback=trigger1, bouncetime=200)

    #for pin in outputs:
    #    GPIO.setup(xx, GPIO.OUT)

    while True:
        time.sleep(1)
        print("Waiting...")

    # GPIO.output(xx, GPIO.HIGH)
except KeyboardInterrupt:
    print("Ending")
finally:
    GPIO.cleanup()

