from requests_oauthlib import OAuth2Session
import json

client_id = "f97ae0269c79de5bb177"
client_secret = "53488c4d18ab6f462dc2d119a1673120259e1f0b"

authorization_base_url = 'https://github.com/login/oauth/authorize'
token_url = 'https://github.com/login/oauth/access_token'

github = OAuth2Session(client_id)

authorization_url, state = github.authorization_url(authorization_base_url)
print('Please go here and authorize,', authorization_url)

redirect_response = input('Paste the full redirect URL here:')

github.fetch_token(token_url, client_secret=client_secret,authorization_response=redirect_response)

response = github.get('https://api.github.com/user')
print(response.content.decode())

dict_response = json.loads(response.content.decode())
for key,value in dict_response.items():
	print(key,"-->",value)
