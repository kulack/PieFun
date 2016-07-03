import RPi.GPIO as GPIO
import time

print("Starting with board revision %s" % GPIO.RPI_REVISION)

# Use raspberry pi board pin numbers
GPIO.setmode(GPIO.BOARD)

# These are the available buttons and the GPIO pins they are on
one=35
two=37
three=22
four=40
five=36
six=38
seven=18

# These are the GPIO pins for the fire control relays
fire1=33
fire2=31
fire3=29
fire4=32

# On the input of any of these buttons
inputs = [ one, two, three, four, five, six, seven ]
outputs = [ fire1, fire2, fire3, fire4 ]

# These are the actions we're going to take
actions = { one   : [ fire1 ],
            two   : [ fire2 ],
            three : [ fire3 ],
            four  : [ fire4 ],
            five  : [ fire1, fire4 ],
            six   : [ fire2, fire3 ],
            seven : [ fire1, fire2, fire3, fire4 ] }


# This runs in a secondary thread
def trigger(channel):
    fires = actions[channel]
    print("Fire pin=%s  %s" % (str(channel), fires))
    try:
        for pin in fires:
            GPIO.output(pin, GPIO.HIGH)
        # We will eventually do something better here so that
        # we can hold the button down and continue to fire the output
        time.sleep(0.4)
    except:
        print("Failed firing pin=%s  %s" % (str(channel), fires))
    finally:
        print("Off pin=%s  %s" % (str(channel), fires))
        for pin in fires:
            GPIO.output(pin, GPIO.LOW)


try:
    # Set up GPIO channels as input or output
    for pin in outputs:
        print("Activating output for pin %d" % pin)
        GPIO.setup(pin, GPIO.OUT)

    for pin in inputs:
        print("Activating input triggers for pin %d" % pin)
        GPIO.setup(pin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        GPIO.add_event_detect(pin, GPIO.RISING, callback=trigger, bouncetime=300)

    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print("\nEnding")

finally:
    # Attempt to turn off everything
    try:
        for pin in inputs:
            GPIO.remove_event_detect(pin)
        for pin in outputs:
            GPIO.output(pin, GPIO.LOW)
    except:
        print("Couldn't do reset of output GPIO pins")
    GPIO.cleanup()

