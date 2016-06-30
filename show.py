import RPi.GPIO as GPIO

print("Starting with revision %s" % GPIO.RPI_REVISION)

# Use raspberry pi board pin numbers
GPIO.setmode(GPIO.BOARD)

inputs = [ 35 ]
outputs = [ ];

try:
    # Set up GPIO channels as input or output
    for pin in inputs:
        print("Turning on input for pin %s" % str(pin))
        GPIO.setup(pin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

    #for pin in outputs:
    #    GPIO.setup(xx, GPIO.OUT)

    while True:
        for pin in inputs:
            input_value = GPIO.input(pin)
            print("Pin %s is %s" % (str(pin), input_value))

    # GPIO.output(xx, GPIO.HIGH)
except:
    print("\nEnding")
finally:
    GPIO.cleanup()

