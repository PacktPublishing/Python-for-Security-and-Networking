import dpkt
import socket
import geoip2.database
import argparse

def geolocation(ip_address):
    try:
        with geoip2.database.Reader('GeoLite2-City.mmdb') as gi:
            rec = gi.city(ip_address)
            city = rec.city.name
            country = rec.country.name
            continent = rec.continent.name
            latitue = rec.location.latitude
            longitude = rec.location.longitude
            return f'{city}, {country}, {continent}, {latitue} {longitude}'

    except Exception as e:
        print(f'{"":>3}[-] Exception: {e.__class__.__name__}')


def read_pcap(pcap_file):
    for ts, buf in pcap_file:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)
            print(f'[+] Src: {geolocation(src)} --> Dst: {geolocation(dst)}')
        except Exception as exception:
            print(f'{"":>3}[-] Exception: {exception}')
            pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser(usage='python3 geo_print PCAP_FILE')
    parser.add_argument('--pcap', type=str,help="specify the name of the PCAP file")
    args = parser.parse_args()
    pcap = args.pcap

    with open(pcap, 'rb') as file:
        pcap = dpkt.pcap.Reader(file)
        read_pcap(pcap)
