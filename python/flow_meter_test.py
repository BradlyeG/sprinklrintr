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

# Devices and objects
in_sol_ctrl = gpiozero.DigitalOutputDevice(IN_SOL_PIN)
out_sol_ctrl = gpiozero.DigitalOutputDevice(OUT_SOL_PIN)
in_flw_ctrl = gpiozero.DigitalInputDevice(IN_FLW_MTR, True) # True to enable internal pull up resistor on pi
out_fwl_ctrl = gpiozero.DigitalInputDevice(OUT_FLW_MTR, True) # True to enable internal pull up resistor on pi

# Web server's php will call this python script, grab the amount specified from the web dashboard, and pass in the water target as the first and only argument
water_target = float(sys.argv[1])
water_amount = 0

# Sensor outputs pulses when the hall effect sensor moves
sensor_count = 0

print("Water target is: " + str(water_target) + " L")

# The script only needs to run once. Best practice would put this all in a class but this is a test
while water_amount < water_target:
    # Activate the solenoid, only if it already off
    if not in_sol_ctrl.value:
        in_sol_ctrl.on()
        print("sols on")

    # If a pulse is detected
    if in_flw_ctrl.value:
        # Add to the total amount of pulses
        sensor_count += 1
        # Convert pulses to liters
        water_amount = sensor_count * PLS_CON
        print("Water amount: " + str(water_amount))

    # We need to turn the solenoid off if we have watered enough
    if water_amount >= water_target:
        in_sol_ctrl.off()
        print("sols off")

