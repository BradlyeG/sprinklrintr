# "Smart Rainwater Havesting Meter"
# Captsone project for Purdue Global IT599
# Bradlge-Jacob Gordon 2024
# Code and project under MIT license

# Python code to interact with relays and get data from flow meters
# The general idea is that this python program is interfaced with a web server that will call
# python functions. This program will sit and wait for those calls to do something

# Libraries
import gpizero

# Pin Definitions
IN_SOL_PIN = 23
OUT_SOL_PIN = 18
IN_FLW_MTR = 14
OUT_FLW_MTR = 15

# Devices and objects
in_sol_ctlr = gpizero.DigitalOutputDevice(IN_SOL_PIN)
out_sol_ctrl = gpizero.DigitalOutputDevice(OUT_SOL_PIN)
in_flw_ctrl = gpizero.DigitalInputDevice(IN_FLW_MTR, True) # True to enable internal pull up resistor on pi
out_fwl_ctrl = gpizero.DigitalInputDevice(OUT_FLW_MTR, True) # True to enable internal pull up resistor on pi

while True:
    in_sol_ctrl.blink()
    out_sol_ctrl.blink()