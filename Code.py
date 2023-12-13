import requests
import sys
from torrequest import TorRequest

proxyPort = 9050
ctrlPort = 9051
site = input("Enter your Blog Address: ")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36"
}

def run(tr):  
    try:
        response = tr.get(site, headers=headers, verify=True)  # Set verify=True for certificate verification
        print("Blog View Added With IP: " + tr.get('http://ipecho.net/plain').content.decode('utf-8'))
    except requests.exceptions.HTTPError as e:
        print("HTTP Error:", e)
    except requests.exceptions.RequestException as e:
        print("Request Exception:", e)


if __name__ == '__main__':
    if len(sys.argv) > 3:
        if sys.argv[1] and sys.argv[2]:
            proxyPort = sys.argv[1]
            ctrlPort = sys.argv[2]

    with TorRequest(proxy_port=proxyPort, ctrl_port=ctrlPort, password=None) as tr:
            run(tr)  # Pass the TorRequest object to the run function
