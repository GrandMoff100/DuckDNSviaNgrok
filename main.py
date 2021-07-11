import sys
import socket
import requests
from pyngrok import ngrok

file, ngrok_token, duckdns_token, *duckdns_domains = sys.argv

ngrok.set_auth_token(ngrok_token)
tunnel = ngrok.connect(8123, insecure=True)
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
import sys
import socket
import requests
from pyngrok import ngrok

file, ngrok_token, duckdns_token, *duckdns_domains = sys.argv

ngrok.set_auth_token(ngrok_token)
tunnel = ngrok.connect(8123, insecure=True)
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

ngrok_process = ngrok.get_ngrok_process()

try:
    # Block until CTRL-C or some other terminating event
    print('Waiting for tunnel process completion.')
    ngrok_process.proc.wait()
except KeyboardInterrupt:
    print("Shutting down server.")
    ngrok.kill()