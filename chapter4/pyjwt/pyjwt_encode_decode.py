import datetime
import jwt

SECRET_KEY = "python_jwt"

# json data to encode
json_data = {
    "sender": "Python JWT",
    "message": "Testing Python JWT",
    "date": str(datetime.datetime.now()),
    #"exp": datetime.datetime.utcnow() - datetime.timedelta(seconds=1) 
}

# encode the data with SECRET_KEY and 
# algorithm "HS256" -> Symmetric Algorithm
encoded_token = jwt.encode(payload=json_data, key=SECRET_KEY, algorithm="HS256")

print("Token:",encoded_token)

try:
    decode_data = jwt.decode(jwt=encoded_token, key=SECRET_KEY, algorithms="HS256")
    print("Decoded data:",decode_data)
except Exception as e:
    message = f"Token is invalid --> {e}"
    print({"message": message})
    
 
