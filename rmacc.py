#!/usr/bin/env python

import subprocess
import argparse
import re
import random

def parse_args():
    parser = argparse.ArgumentParser(prog = "rmacc", description = "Change to a random MAC address")
    parser.add_argument('-i','--interface', dest='interface', help='Interface to change its MAC address', required=True)
    parser.add_argument('-r','--random', help='Generate random MAC Address', action="store_true")
    parser.add_argument('-m','--mac', dest='new_mac',help='User set the MAC Address')
    
    return parser.parse_args()
       
def random_mac_address():
    mac = [random.randint(0x00, 0xff) for _ in range(6)]
    return ':'.join(map(lambda x: "%02x" % x, mac))

def change_mac(interface, new_mac):
    print(f"[+] Changing MAC address for {interface} to {new_mac}")
    subprocess.run(["ifconfig", interface ,"down"])
    print("[+] Setting interface down....")
    subprocess.run(["ifconfig", interface , "hw" ,"ether", new_mac])
    subprocess.run(["ifconfig", interface ,"up"])
    print("[+] Setting interface up....")


def get_current_mac(interface):
    ifconfig_result = subprocess.run(['ifconfig', interface], capture_output=True)
    ifconfig_result = ifconfig_result.stdout.decode()

    address_match = re.search(r"ether (\S+)", ifconfig_result)
    if address_match:
        return address_match.group(1)
    else:
        print("[-] Could not read MAC address")


args = parse_args()

current_mac = get_current_mac(args.interface)
print(f"[+] The current MAC is: {current_mac}")

if args.random:
    new_mac = random_mac_address()
else:
    new_mac = args.new_mac
    
change_mac(args.interface , new_mac)

if current_mac == get_current_mac(args.interface):
    print(f"[-] Mac adress did not get changed")
else:
    print(f"[+] The new mac is: {get_current_mac(args.interface)}")
