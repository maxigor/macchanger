#!/usr/bin/env python

import subprocess
import argparse

parser = argparse.ArgumentParser(
    prog = "rmacc",
    description = "Change to a random MAC address"
)
parser.add_argument('-i', '--interface', dest='interface' , help='Interface to change its MAC address')
parser.add_argument('-m', '--mac', dest='new_mac',help='New MAC address')

args = parser.parse_args()

interface = args.interface
new_mac = args.new_mac

print("[+] Changing MAC address for " + interface + " to " + new_mac)

subprocess.call(["ifconfig", interface ,"down"])
print("[+] Setting interface down....")

subprocess.call(["ifconfig", interface , "hw" ,"ether", new_mac])

subprocess.call(["ifconfig", interface ,"up"])
print("[+] Setting interface up....")

