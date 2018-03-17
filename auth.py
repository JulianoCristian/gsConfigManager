# Auth
# The idea behind this script is to store the credentails
# Then to only make new requests for X-GSAccessTokens as needed.
# When reconfiguring have cache on values already there

import os
import sys
import json
import requests

authUrl = 'https://auth.gamesparks.net/restv2/auth'
authPath = '.gsConfigManager/auth.json'
credentailsPath = '.gsConfigManager/credentails.json'

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
    if not check_path(credentailsPath):
        fail_with_error('Credentails not specified. Run with configure option.')

def get_configured_apikey():
    has_configured_credentials()
    return open_json_file(credentailsPath)['apikey']

def get_configured_credentials ():
    return open_json_file(credentailsPath)

def get_gs_access_token_from_file (filename):
    credentials = export.read_file()
    accessToken = gamesparks.get_gs_access_token(username, password)

def request_gs_access_token (username, password):
    url = authUrl + '/user'
    res = requests.get(url, auth=requests.auth.HTTPBasicAuth(username, password))
    if (res.status_code != 200):
        fail_with_error('Invalid Credentials')
    return res.json()

def get_gs_jwt_token_request ():
    url = authUrl + '/game/' + apiKey + '/jwt'
    res = requests.get(url, params={ 'X-GSAccessToken': gs_access_token })
    if (res.status_code != 200):
        fail_with_error('Failed to get JWT Token with ' + str(res.status_code) + ' status code.')
    return res.json()['X-GS-JWT']

def get_gs_access_token ():
    # Check has token in auth, check token not expired yet
    has_configured_credentials()
    c = get_configured_credentials()
    t = request_gs_access_token(c['username'], c['password'])
    write_json_file(authPath, t)
    return t['X-GSAccessToken']

def configure ():
    d = {}
    d['apikey'] = raw_input("API Key: ")
    d['username'] = raw_input("Portal Username: ")
    d['password'] = raw_input("Portal Password: ")
    write_json_file(credentailsPath, d)