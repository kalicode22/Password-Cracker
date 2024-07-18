from scapy.all import ARP, Ether, srp
import argparse

def scan(ip):
    arp_request = ARP(pdst=ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp_request

    result = srp(packet, timeout=3, verbose=0)[0]

    clients = []
    for sent, received in result:
        clients.append({'ip': received.psrc, 'mac': received.hwsrc})

    print("Scanning complete:")
    print("IP\t\t\tMAC Address")
    print("-----------------------------------------")
    for client in clients:
        print(f"{client['ip']}\t\t{client['mac']}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple Network Scanner")
    parser.add_argument("-t", "--target", required=True, help="Target IP address or range (e.g., 192.168.1.1/24)")
    args = parser.parse_args()
    
    scan(args.target)
