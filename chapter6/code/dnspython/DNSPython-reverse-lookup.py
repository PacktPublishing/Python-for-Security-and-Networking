import dns.reversename

name = dns.reversename.from_address("45.55.99.72")
print(name)
print(dns.reversename.to_address(name))



