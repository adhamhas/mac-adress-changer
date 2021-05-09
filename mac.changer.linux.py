import subprocess
interface = "wlan0"
new_mac = input("new MAC > ")
print("[+] Changing mac adress for " + interface + "to " + new_mac)

subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)
