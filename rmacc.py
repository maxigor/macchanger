#!/usr/bin/env python

import subprocess
import argparse
import re


def get_arguments():
    parser = argparse.ArgumentParser(
        prog = "rmacc",
        description = "Change to a random MAC address"
    )

    parser.add_argument(
        '-i', 
        '--interface', 
        dest='interface' , 
        help='Interface to change its MAC address')

    parser.add_argument(
        '-m', 
        '--mac', 
        dest='new_mac',
        help='New MAC address')
    
    args = parser.parse_args()
    if not args.interface:
        parser.error("[-] Please specify an interface, use --help for more info")
    if not args.new_mac:
        parser.error("[-] Please specify a new mac, use --help for more info")
    
    return parser.parse_args()


def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)

    subprocess.call(["ifconfig", interface ,"down"])
    print("[+] Setting interface down....")

    subprocess.call(["ifconfig", interface , "hw" ,"ether", new_mac])

    subprocess.call(["ifconfig", interface ,"up"])
    print("[+] Setting interface up....")


def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(['ifconfig', interface])

    address_match = re.search(r"ether (\S+)", ifconfig_result.decode())
    if address_match:
        return address_match.group(1)
    else:
        print("[-] Could not read MAC address")


args = get_arguments()
change_mac(args.interface , args.new_mac)

current_mac = get_current_mac(args.interface)
print("The current MAC is: " + str(current_mac))
