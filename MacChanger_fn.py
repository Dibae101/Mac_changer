#!/usr/bin/env python

import subprocess
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Enter interface (First byte even)")
    parser.add_option("-m", "--mac", dest="new_mac", help="Enter Mac Address")
    (options, argument) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Enter proper argument, enter --help for more information")
    if not options.new_mac:
        parser.error("[-] Enter proper new mac address, enter --help for more information")
    return options

def change_mac(interface, new_mac):
    print ("[+] Changing MAC address of " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
    subprocess.call(["ifconfig"])
    print("------------>Mac Address Successfully changed<----------------")

options = get_arguments()
change_mac(options.interface, options.new_mac)

