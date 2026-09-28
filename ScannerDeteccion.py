import psutil
import ipaddress
def list_interface():
    interfaces=psutil.net_if_addrs()
    stats = psutil.net_if_stats()
    activate_interfaces= []

    for name, dir in interfaces.items():
        print(name)
        if name in stats and stats[name].isup:
            activate_interfaces.append(name)
        for dir in dir: 
            if dir.family==2: #ipv4
                ip=dir.address
                mask=dir.netmask
                network=ipaddress.IPv4Network(f"{ip}/{mask}", strict=False)
                cidr = network.prefixlen
                print(ip,mask)
            print(network,cidr)
            if(name=="lo"):
                loopback = (name,dir.address)
            
    return loopback

def LoopBackDetector():
     IsLoopBack=False
     nameInterface, dir = list_interface()
     if (nameInterface == "lo"):
         IsLoopBack=True
     return IsLoopBack, nameInterface ,dir

list_interface()

#Por qué append y ipv4networks