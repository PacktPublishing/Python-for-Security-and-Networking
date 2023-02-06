import gvm 
from gvm.protocols.latest import Gmp 

connection = gvm.connections.TLSConnection(hostname='localhost',port=9392) 

# using the with statement to automatically connect and disconnect to gvmd
with Gmp(connection=connection) as gmp:
    # get the response message returned as a utf-8 encoded string
    response = gmp.get_version()

    # print the response message
    print(response)
