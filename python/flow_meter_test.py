# "Smart Rainwater Havesting Meter"
# Captsone project for Purdue Global IT599
# Bradlge-Jacob Gordon 2024
# Code and project under MIT license

# Python code to interact with relays and get data from flow meters
# The general idea is that this python program is interfaced with a web server that will call
# python functions. This program will sit and wait for those calls to do something

# Libraries
import gpiozero
import sys
from time import sleep
from signal import pause

# Pin Definitions
IN_SOL_PIN = 23
OUT_SOL_PIN = 18
IN_FLW_MTR = 14
OUT_FLW_MTR = 15

# Sensor pulse conversion per specs, in liters
PLS_CON = .0025
# Bounce time to calibrate liquid flow meters
LFM_BNC = 0.0032

# Devices and objects
in_sol_ctrl = gpiozero.DigitalOutputDevice(IN_SOL_PIN)
out_sol_ctrl = gpiozero.DigitalOutputDevice(OUT_SOL_PIN)
in_flw_ctrl = gpiozero.DigitalInputDevice(IN_FLW_MTR, True, bounce_time=LFM_BNC) # True to enable internal pull up resistor on pi and account for bounce - time for signal to change properly
out_fwl_ctrl = gpiozero.DigitalInputDevice(OUT_FLW_MTR, True, bounce_time=LFM_BNC) # True to enable internal pull up resistor on pi and account for bounce - time for signal to change properly

# Web server's php will call this python script, grab the amount specified from the web dashboard, and pass in the water target as the first and only argument
#water_target = float(sys.argv[1])
water_amount = 0

# Sensor outputs pulses when the hall effect sensor moves
sensorp_count = 0

# Simple function to count the pulses, and output how much water has been let out thus far
def count_pulse():
    global sensorp_count
    sensorp_count += 1
    print("Estimated Amount: " + str((sensorp_count * PLS_CON)) + " liters")

# Give the sensor a when_activated function
in_flw_ctrl.when_activated = count_pulse

# The script only needs to run once. Best practice would put this all in a class but this is a test

while True:
    # Activate solenoid if it isn't already
    if not in_sol_ctrl.value:
        in_sol_ctrl.on()
    # The script still needs to run, but doesn't need to do anything in while waiting
    pause()
    



    