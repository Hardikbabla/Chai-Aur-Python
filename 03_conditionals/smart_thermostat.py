# Building Smart Thermostat System
# =====================================================================
"""
Your're building a smart thermostat alert system:
    - if the device_status is "active"
        - And temperture > 35 -> Warn: "High temperature alert!"
        - Else: "Temperature is Normal"
    - if device is off -> "Device is offline"
"""
# =====================================================================

device_status = "active"
temperature = 36

if device_status == "active":
    if temperature > 35:
        print("High temperature alert!") 
    else:
        print("Temperature is Normal")
else:
    print("Device is offline")
