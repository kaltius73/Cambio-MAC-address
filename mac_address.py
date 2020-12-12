#!/usr/bin/env phyton

import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interfaccia per cambiare il Mac address")
    parser.add_option("-m", "--mac", dest="new_mac", help="Nuovo Mac address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Specifica una interfaccia, usa --help per ulteriori info")
    elif not options.new_mac:
        parser.error("[-] Specifica un MAC address, usa --help per ulteriori info")
    return options

def change_mac(interface, new_mac):
    print("[+] Cambio MAC Address per " + interface + " a " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Non leggo il MAC address")


options = get_arguments()
current_mac = get_current_mac(options.interface)
print("MAC address corrente = " + str(current_mac))

change_mac(options.interface, options.new_mac)

current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("[+] MAC address cambiato in " + current_mac)
else:
    print("[-] MAC address non cambiato")