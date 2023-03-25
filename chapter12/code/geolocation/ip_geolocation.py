import requests

class IPGeolocation(object):

    def __init__(self, ip_address):
        self.latitude = ''
        self.longitude = ''
        self.country = ''
        self.city = ''
        self.time_zone = ''
        self.ip_address = ip_address
        self.get_location()

    def get_location(self):
	
        json_request = requests.get('http://ip-api.com/json/%s' % self.ip_address).json()
        print(json_request)
        
        if 'country' in json_request.keys():
        	self.country = json_request['country']
        if 'countryCode' in json_request.keys():
        	self.country_code = json_request['countryCode']
        if 'timezone' in json_request.keys():
        	self.time_zone = json_request['timezone']
        if 'city' in json_request.keys():
        	self.city = json_request['city']
        if 'lat' in json_request.keys():
        	self.latitude = json_request['lat']
        if 'lon' in json_request.keys():
        	self.longitude = json_request['lon']

if __name__ == '__main__':
    geolocation = IPGeolocation('151.101.1.168')
    print(geolocation.__dict__)
