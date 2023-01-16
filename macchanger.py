#!/usr/bin/env python

import subprocess

interface = input("Digite a interface que deseja mudar o mac: ")
new_mac = "00:11:22:33:44:55"

print(interface)

print("[+] Mudando o MAC address de " + interface + " para " + new_mac)

subprocess.call("ifconfig " + interface + " down" , shell=True)
print("Setting interface down....")
#subprocess.call("ifconfig interface hw ether 00:11:22:33:44:66" , shell=True)
subprocess.call("ifconfig " + interface + " up" , shell=True)
print("Setting interface up....")

