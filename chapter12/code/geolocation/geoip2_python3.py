import argparse
import geoip2.database
import socket

def geolocation(ip_address):
    with geoip2.database.Reader('GeoLite2-City.mmdb') as gi:
        rec = gi.city(ip_address)

        city = rec.city.name
        region = rec.subdivisions.most_specific.name
        country = rec.country.name
        continent = rec.continent.name
        latitue = rec.location.latitude
        longitude = rec.location.longitude

        print(f'[*] Target: {ip_address} Geo-located.')
        print(f'[+] {city}, {region}, {country}, {continent}')
        print(f'[+] Latitude: {latitue}, Longitude: {longitude}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Get IP Geolocation info')
    parser.add_argument('--hostname', action="store", dest="hostname",default='python.org')
    given_args = parser.parse_args()
    hostname = given_args.hostname
    ip_address = socket.gethostbyname(hostname)
    geolocation(ip_address)
