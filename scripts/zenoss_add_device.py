#!/usr/bin/env python

import argparse
import os
import sys
import zenossapi

def add_device(host, username, password, device, device_class, pem=None, maintenance=False):
    """
    Adds the device using to the specified class using provided credentials.
    """
    z = zenossapi.ZenossAPI()
    try:
        z.connect(host, username, password, pem)
        # Add device
        z.add_device(device, device_class)
        if maintenance:
            z.set_maintenance(device)
        # Reset IP just in case
        z.reset_ip(device)
    except Exception, ex:
        print(str(ex))
        return -1
    return 0
        
if __name__ == "__main__":
    """Handle argument passing from command line"""

    parser = argparse.ArgumentParser(prog='zenoss_add_device.py')

    parser.add_argument('host', help='Zenoss host')
    parser.add_argument('username', help='Zenoss username')
    parser.add_argument('password', help='Zenoss password')
    parser.add_argument('-K', '--client-pem', type=str, help='Zenoss user pem file')
    parser.add_argument('-m', '--maintenance', action='store_true', help='Set device to maintenance')
    parser.add_argument('device', help='Device to add')
    parser.add_argument('device_class', help='Device class for new device')

    args = parser.parse_args()

    if args.client_pem:
        if not os.path.exists(args.client_pem):
            print('Specified client pem file doesn\'t exist\n')
            sys.exit(1)

    sys.exit(
        add_device(
            args.host,
            args.username,
            args.password,
            args.device,
            args.device_class,
            args.client_pem,
            args.maintenance
            )
        )
