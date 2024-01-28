'''
ESC204 2024S PSA
Task: 3-state toggle w/ button
'''

# Import libraries needed for blinking the LED
import board
import digitalio

# Configure the GPIO pin connected to the LED as a digital output
R = digitalio.DigitalInOut(board.GP17)
R.direction = digitalio.Direction.OUTPUT

G = digitalio.DigitalInOut(board.GP16)
G.direction = digitalio.Direction.OUTPUT

B = digitalio.DigitalInOut(board.GP18)
B.direction = digitalio.Direction.OUTPUT

# Configure the GPIO pin connected to the button as a digital input
button = digitalio.DigitalInOut(board.GP15)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP # Set internal pull-up resistor

# button.value = False when pressed
# led turns on when led.value = True
pressed = False
state = 1 # 1 is off, 2 is R and B on, 3 is all lights on
        
# Loop so the code runs continuously
while True:
    if (pressed == False and button.value == False): # if button is initially pressed
        pressed = True
        if (state == 3):
            state = 1
            print(state)
        else:
            state += 1
            print(state)
    elif (button.value): # if button is released
        pressed = False
    if (state == 1):
        R.value = False
        G.value = False
        B.value = False
    elif (state == 2):
        R.value = True
        G.value = False
        B.value = True
    else:
        R.value = True
        G.value = True
        B.value = True
