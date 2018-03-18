#!/usr/bin/env python3

# Steve Callaghan <scalla[at]amazon.com>
# 2018/03/16

import sys
import auth
import json
import export
import config

def print_json (jsonMsg):
    print json.dumps(jsonMsg, indent=4, sort_keys=False)

def fail_with_error (msg):
    print('Fatal Error: ' + msg)
    sys.exit()

def print_help (filename):
    print('--- ' + filename + ' usage guide.')
    print('--- Configure and Help')
    print(' - ' + filename + ' configure -- Configure Credentails.')
    print(' - ' + filename + ' help -- Print this help screen.')
    print('--- Export Options')
    print(' - ' + filename + ' exportScripts -- Export Scrpts')
    print(' - ' + filename + ' exportManagementSnapshot -- Export the Management Screens')
    print(' - ' + filename + ' exportAll -- Export the entire current configuration')

# Main
if len(sys.argv) <= 1 or sys.argv[1] == 'help':
    print_help(sys.argv[0])

elif sys.argv[1] == 'configure':
    auth.configure()

elif sys.argv[1] == 'sanitize':
    print('Sanitize not yet implemented.')

else:
    if sys.argv[1] == 'getSnapshot':  # Get Snapshot
        if (len(sys.argv) <= 2):
            fail_with_error('Invalid parameters. Missing parameter snapshotId.')
        print(config.get_snapshot(auth.get_configured_apikey(), sys.argv[2], auth.get_gs_access_token()))
    elif sys.argv[1] == 'getManagementScreens': # Get Management Screens
        print_json(config.get_management_screens(auth.get_configured_apikey(), auth.get_gs_access_token()))
    elif sys.argv[1] == 'getManagementSnippets': # Get Management Snippets
        print_json(config.get_management_snippets(auth.get_configured_apikey(), auth.get_gs_access_token()))
    elif sys.argv[1] == 'getManagementSnippet': # Get Management Snippet
        if len(sys.argv) <= 2:
            fail_with_error('Invalid parameters. Missing parameter snippet shortCode.')
        print_json(config.get_management_snippet(auth.get_configured_apikey(), sys.argv[2], auth.get_gs_access_token()))
    elif sys.argv[1] == 'exportScripts':
        export.export_scripts(auth.get_configured_apikey(), auth.get_gs_access_token())
    elif sys.argv[1] == 'exportManagementSnapshot': # Export Management Screens
        export.export_management_snapshot(auth.get_configured_apikey(), auth.get_gs_access_token())
    elif sys.argv[1] == 'exportAll':
        export.export_all(auth.get_configured_apikey(), auth.get_gs_access_token())
    else:
        print_help(sys.argv[0])