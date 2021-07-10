import sys
import socket
import requests
from pyngrok import ngrok

file, ngrok_token, duckdns_token, *duckdns_domains = sys.argv

ngrok.set_auth_token(ngrok_token)
tunnel = ngrok.connect(8123)
print('Ngrok URL:',  tunnel.public_url)
protocol, domain = tunnel.public_url.split('://')
ip = socket.gethostbyname(domain)
print('Resolved IP:', ip)

BASE = 'https://www.duckdns.org/update'
PARAMS = {
    'token': duckdns_token,
    'ip': ip,
    'domains': ','.join(duckdns_domains)
}

resp = requests.get(BASE, params=PARAMS)
print('DuckDNS URL:', resp.url)
print('DuckDNS Response:', resp.text)
