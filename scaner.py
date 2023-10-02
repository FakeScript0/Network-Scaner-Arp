import scapy.all as scapy
import optparse
option=optparse.OptionParser()
def nmap(ipadress,macadress):
    arp_request=scapy.ARP(pdst=ipadress)
    broadcast=scapy.Ether(dst=macadress)
    combined=broadcast/arp_request
    (answer,unanswer)=scapy.srp(combined,timeout=1)
    answer.summary()
def opt():
    option.add_option("-i",dest="ipadress",help="IpAdress")
    option.add_option("-m",dest="macadress",help="MacAdress")
    (user_input,arguments)=option.parse_args()
    ipadress=(user_input.ipadress)
    macadress=(user_input.macadress)
    return nmap(ipadress,macadress)
print("Network Proqraminiz Isleyir")
opt()
