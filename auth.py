# Auth
# The idea behind this script is to store the credentails
# Then to only make new requests for X-GSAccessTokens as needed.

import os
import sys
import json
import time
import requests

def get_auth_url():
    return 'https://auth.gamesparks.net/restv2/auth'

def get_api_path():
    return '.gsConfigManager/api.json' 

def get_auth_path():
    return os.path.expanduser('~') + '/.gsConfigManager/auth.json'

def get_credential_path():
    return os.path.expanduser('~') + '/.gsConfigManager/credentials.json'

def check_path(path):
    return os.path.exists(os.path.dirname(path))

def make_path(path):
    os.makedirs(os.path.dirname(path))

def open_json_file(filename):
    return json.load(open(filename, 'r'))

def write_file(filename, data):
    if not check_path(filename):
        make_path(filename)
    print('Writing ' + filename)
    with open(filename, 'w') as f:
        f.write(data)

def write_json_file(filename, jsonData):
    write_file(filename, json.dumps(jsonData, indent=4, sort_keys=False))

def fail_with_error (msg):
    print('Fatal Error: ' + msg)
    sys.exit()

def has_configured_credentials ():
    if not check_path(get_credential_path()):
        fail_with_error('Credentails not specified. Run with configure option.')

def get_configured_apikey():
    has_configured_credentials()
    return open_json_file(get_api_path())['apikey']

def get_configured_credentials ():
    return open_json_file(get_credential_path())

def request_gs_access_token (username, password):
    url = get_auth_url() + '/user'
    res = requests.get(url, auth=requests.auth.HTTPBasicAuth(username, password))
    if (res.status_code != 200):
        fail_with_error('Invalid Credentials')
    return res.json()

def get_gs_jwt_token_request ():
    url = get_auth_url() + '/game/' + apiKey + '/jwt'
    res = requests.get(url, params={ 'X-GSAccessToken': gs_access_token })
    if (res.status_code != 200):
        fail_with_error('Failed to get JWT Token with ' + str(res.status_code) + ' status code.')
    return res.json()['X-GS-JWT']

def get_gs_access_token ():
    if os.path.isfile(get_auth_path()):
        t = open_json_file(get_auth_path())
        if t['expiresAt']/1000 - time.time() > 0:
            return t['X-GSAccessToken']
    
    has_configured_credentials()
    c = get_configured_credentials()
    t = request_gs_access_token(c['username'], c['password'])
    write_json_file(get_auth_path(), t)
    return t['X-GSAccessToken']

def configureApi ():
    d = {}
    d['apikey'] = raw_input("API Key: ")
    write_json_file(get_api_path(), d)

def configureAuth ():
    d = {}
    d['username'] = raw_input("Portal Username: ")
    d['password'] = raw_input("Portal Password: ")
    write_json_file(get_credential_path(), d)

def configure ():
    configureAuth()
    configureApi()