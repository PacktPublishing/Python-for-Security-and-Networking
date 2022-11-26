import requests
import sys

def main(url):
    robot_url = f'{url}/robots.txt'
    response = requests.get(robot_url)
    print(response.text)

if __name__ == "__main__":
    url = sys.argv[1]
    main(url)
