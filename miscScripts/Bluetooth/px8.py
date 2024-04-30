#%%MARK: About
# script to connect PC to a previously connected bluetooth device
#! script is not working!

""" 
Program is not working. The code is from chatgpt. Protocol of px8 seem to be 
L2PAC, not RFCOMM. Not sure how to handle this.
"""

# import bluetooth

# tn = 'Px8 COM'  # target name
# ta = None  # target address


# def nameIsTarget(name, tn):
#     match name:
#         case 'Px8 COM': return name + f' {"found":*^15}'
#         case _: return name


# print(f'Looking for {tn}...')

# devices = bluetooth.discover_devices(lookup_names=True)
# print(f'Found devices:')
# for addr, name in devices:
#     if name == tn: ta = addr
#     print(f'{addr}, {nameIsTarget(name,tn)}')


import os
import sys
import bluetooth


def find_port(bd_addr):
    port = None
    services = bluetooth.find_service(address=bd_addr)
    if services:
        for service in services:
            # if service['uuid'] == service_uuid:
            port = service['port']
            print(port)
            print(service['uuid'])
            # break
    return port


# Set the target Bluetooth device name
target_name = "Px8 COM"

# Search for nearby devices
nearby_devices = bluetooth.discover_devices()

# Try to find the target device by its name
for address in nearby_devices:
    if target_name == bluetooth.lookup_name(address):
        target_address = address
        find_port(target_address)
        break

# Check if the target device was found
if target_address:
    print(f"Found target device with address {target_address}")
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    try:
        # Try to connect to the target device
        sock.connect((target_address, 1))
        print("Successfully connected to the target device")
    except bluetooth.btcommon.BluetoothError as error:
        print(f"Failed to connect to the target device: {error}")
        sys.exit(1)
else:
    print(f"Could not find a nearby device named {target_name}")
