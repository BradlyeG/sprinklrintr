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
#water_target = float(sys.argv[1])
water_amount = 0

# Sensor outputs pulses when the hall effect sensor moves
sensor_count = 0

# The script only needs to run once. Best practice would put this all in a class but this is a test

while True:
    # Activate solenoid
    in_sol_ctrl.on()
    # Track the sensor count
    if in_flw_ctrl.value:
        sensor_count += 1
    # print how many we have
    print("Estimated Amount:" + str((sensor_count * PLS_CON)) + " liters")



    