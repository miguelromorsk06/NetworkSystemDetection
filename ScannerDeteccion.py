import psutil
import ipaddress
from scapy.all import ARP,Ether,srp
def get_Network():
    interfaces=psutil.net_if_addrs()
    for name, dir in interfaces.items():
        for dir in dir: 
           if dir.family.name=="AF_INET":
               ip=dir.address
               mask=dir.netmask
               if ip.startswith("127."):
                   continue
               network=ipaddress.IPv4Network(f"{ip}/{mask}",strict=False)
               return str(network)  

def list_host(network):
    package= Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=network)
    answer =srp(package,timeout=2,verbose=False)[0]
    hosts = []

    for send, answers in answer:
        hosts.append(
             {
            "ip":answers.psrc,
            "mac": answers.hwsrc 
             }
        )
    return hosts 

network =get_Network()
print(f"Network Detected: {network}")
print("Searching Devices... \n")
hosts = list_host(network)
for host in hosts:
    print(f"IP:{host['ip']:<15} MAC: {host['mac']}")