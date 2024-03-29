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

# Pin Definitions
IN_SOL_PIN = 23
OUT_SOL_PIN = 18
IN_FLW_MTR = 14
OUT_FLW_MTR = 15

# Sensor pulse conversion per specs, in liters
PLS_CON = .0025

# Bounce time to calibrate liquid flow meters
LFM_BNC = 0.001

# Constant for watchdog timeout count
WTD_TMOC = 3

# Devices and objects
in_sol_ctrl = gpiozero.DigitalOutputDevice(IN_SOL_PIN)
out_sol_ctrl = gpiozero.DigitalOutputDevice(OUT_SOL_PIN)
in_flw_ctrl = gpiozero.DigitalInputDevice(IN_FLW_MTR, True, bounce_time=LFM_BNC) # True to enable internal pull up resistor on pi and account for bounce - time for signal to change properly
out_fwl_ctrl = gpiozero.DigitalInputDevice(OUT_FLW_MTR, True, bounce_time=LFM_BNC) # True to enable internal pull up resistor on pi and account for bounce - time for signal to change properly

# Web server's php will call this python script, grab the amount specified from the web dashboard, and pass in the water target as the first and only argument
water_target = float(sys.argv[1])
water_amount = 0

# Sensor outputs pulses when the hall effect sensor moves
sensorp_count = 0
lastsensorp_count = 0

# How many times should the watchdog notice no flow output
# before quitting
timeout_count = 0

# Simple function to count the pulses
def count_pulse():
    global sensorp_count, lastsensorp_count
    lastsensorp_count = sensorp_count
    sensorp_count += 1

# Simple function to calculate the water amount
def calculate_water():
    global sensorp_count, water_amount
    water_amount = sensorp_count * PLS_CON

# The watch dog makes sure that the sensor is actually doing something
# or quits the program if it isn't or there is some error
def watchdog():
    global sensorp_count, lastsensorp_count, timeout_count

    if timeout_count == WTD_TMOC:
        sys.exit("Watchdog no longer detecting water output")
    elif lastsensorp_count == sensorp_count:
        timeout_count += 1

# Attach function to sensor's when_activated
in_flw_ctrl.when_activated = count_pulse

print("Water target is: " + str(water_target) + " L")

# The script only needs to run once. Best practice would put this all in a class but this is a test
while water_amount < water_target:

    # Activate the solenoid, only if it already off
    if not in_sol_ctrl.value:
        in_sol_ctrl.on()

    # Wait a moment
    sleep(0.5)

    # Update the water amount
    calculate_water()

    # Run the watchdog
    watchdog()

    # We need to turn the solenoid off if we have watered enough
    if water_amount >= water_target:
        in_sol_ctrl.off()
        print("sols off")


