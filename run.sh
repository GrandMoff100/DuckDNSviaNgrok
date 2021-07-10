#!/usr/bin/with-contenv bashio

NGROK_TOKEN=$(bashio::config 'ngrok_token')
DUCKDNS_TOKEN=$(bashio::config 'duckdns_token')
DUCKDNS_DOMAINS=$(bashio::config 'duckdns_domains')

pip install -r requirements.txt
python main.py NGROK_TOKEN DUCKDNS_TOKEN ${DUCKDNS_DOMAINS[@]}