# Export Operations

import os
import json
import config

def check_path(path):
    if not os.path.exists(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))

def write_file(filename, data):
    check_path(filename)
    print('Writing ' + filename)
    with open(filename, 'w') as f:
        f.write(data)

def write_json_file(filename, jsonData):
    write_file(filename, json.dumps(jsonData, indent=4, sort_keys=False))

def export_scripts (apiKey, gs_access_token):
    print('Exporting ' + apiKey + ' scripts.')
    scripts = config.get_scripts(apiKey, gs_access_token)
    for i in range(len(scripts)):
        filename = 'export-' + apiKey + '/Scripts/' + scripts[i]['type'] + '/' + scripts[i]['name'] + '.js'
        write_file(filename, scripts[i]['script'])

def export_management_snapshot (apiKey, gs_access_token):
    print('Exporting ' + apiKey + ' management screens.')
    snippets = config.get_management_snippets(apiKey, gs_access_token)
    for i in range(len(snippets)):
        snippet = config.get_management_snippet(apiKey, snippets[i]['shortCode'], gs_access_token)
        filename = 'export-' + apiKey + '/Manage/' + snippets[i]['shortCode'] + '.json'
        write_json_file(filename, snippet)

def export_all (apiKey, gs_access_token):
    export_scripts(apiKey, gs_access_token)
    export_management_snapshot(apiKey, gs_access_token)