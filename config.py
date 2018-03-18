# Config

import sys
import requests

configUrl = 'https://config2.gamesparks.net'

def fail_with_error (msg):
    print('Fatal Error: ' + msg)
    sys.exit()

def get_config (apiKey, gs_access_token):
    url = configUrl + '/restv2/game/' + apiKey + '/config'
    res = requests.get(url, params={ 'X-GSAccessToken': gs_access_token, 'full': True })
    if (res.status_code != 200):
        fail_with_error('Failed to get config for ' + apiKey + ' with ' + str(res.status_code) + ' status code.')
    return res.json()

def get_scripts (apiKey, gs_access_token):
    url = configUrl + '/restv2/game/' + apiKey + '/config/~scripts'
    res = requests.get(url, params={ 'X-GSAccessToken': gs_access_token })
    if res.status_code != 200:
        fail_with_error('Failed to get scripts for ' + apiKey + ' with ' + str(res.status_code) + ' status code.')
    return res.json()

def get_script (apiKey, shortCode, gs_access_token):
    url = configUrl + '/restv2/game/' + apiKey + '/config/~scripts/' + shortCode
    res = requests.get(url, params={ 'X-GSAccessToken': gs_access_token })
    if res.status_code != 200:
        fail_with_error('Failed to get script ' + shortCode + ' with ' + str(res.status_code) + ' status code.')
    return res.json()

def get_snapshots (apiKey, gs_access_token):
    url = configUrl + '/restv2/game/' + apiKey + '/admin/snapshots'
    res = requests.get(url, params={ 'X-GSAccessToken': gs_access_token })
    if (res.status_code != 200):
        fail_with_error('Failed to get snapshots for ' + apiKey + ' with ' + str(res.status_code) + ' status code.')
    return res.json()

def get_snapshot (apiKey, snapshotId, gs_access_token):
    url = configUrl + '/restv2/game/' + apiKey + '/admin/snapshots/' + snapshotId
    res = requests.get(url, params={ 'X-GSAccessToken': gs_access_token })
    if (res.status_code != 200):
        fail_with_error('Failed to get snapshot ' + snapshotId + ' with ' + str(res.status_code) + ' status code.')
    return res.json()

def get_management_screens (apiKey, gs_access_token):
    url = configUrl + '/restv2/game/' + apiKey + '/manage/screens'
    res = requests.get(url, params={ 'X-GSAccessToken': gs_access_token })
    if res.status_code != 200:
        fail_with_error('Failed to get Management Screens with ' + str(res.status_code) + ' status code.')
    return res.json()

def get_management_snippets (apiKey, gs_access_token):
    url = configUrl + '/restv2/game/' + apiKey + '/manage/snippets'
    res = requests.get(url, params={ 'X-GSAccessToken': gs_access_token })
    if res.status_code != 200:
        fail_with_error('Failed to get Management Snippets with ' + str(res.status_code) + ' status code.')
    return res.json()

def get_management_snippet (apiKey, shortCode, gs_access_token):
    url = configUrl + '/restv2/game/' + apiKey + '/manage/snippets/' + shortCode
    res = requests.get(url, params={ 'X-GSAccessToken': gs_access_token })
    if res.status_code != 200:
        fail_with_error('Failed to get Management Snippet with ' + str(res.status_code) + ' status code.')
    return res.json()