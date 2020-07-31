#!/usr/bin/env python

import subprocess
import optparse

parser= optparse.OptionParser()
parser.add_option("-i", "--interface", dest="interface", help="Enter interface to change the Mac Address(first byte even)")
parser.add_option("-m", "--mac", dest="new_mac", help="Enter New Mac Address")
(options, arguments) = parser.parse_args()

interface = options.interface
new_mac = options.new_mac

print ("[+] Changing MAC address of " + interface + " to " + new_mac)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])

