# -*- coding: UTF-8 -*-
import sys
import os
import yaml  ### YOU NEED THE pyyaml PACKAGE : [sudo] pip install pyyaml
#from lookerapi import LookerApi
import looker
from pprint import pprint as pp
import json
import string
import datetime

### ------- HERE ARE PARAMETERS TO CONFIGURE -------

# This references the log file from a recent look refactor
logs_file = sys.argv[1]
host = 'localhost'


### ------- OPEN THE CONFIG FILE and INSTANTIATE API -------

f = open('config.yml')
params = yaml.load(f)
f.close()

my_host = params['hosts'][host]['host']
my_secret = params['hosts'][host]['secret']
my_token = params['hosts'][host]['token']

# replace with your custom Looker API Host domain and port, if applicable.
base_url = my_host
client_id = my_token
client_secret = my_secret

# instantiate Auth API
unauthenticated_client = looker.ApiClient(base_url)
unauthenticated_authApi = looker.ApiAuthApi(unauthenticated_client)

# authenticate client
token = unauthenticated_authApi.login(client_id=client_id, client_secret=client_secret)
client = looker.ApiClient(base_url, 'Authorization', 'token ' + token.access_token)

queryApi = looker.QueryApi(client)
lookApi = looker.LookApi(client)

f = open(logs_file)
logs = json.loads(f.read())

for i in logs:
    look_id = str(i['look_id'])
    print "Reverting chages made to Look " + look_id
    original_query_id = i['original_query_id']
    lwk = lookApi.look(look_id)
    output = lookApi.update_look(look_id,{"query_id":original_query_id})
    print "Done"

### ------- DONE -------

print "Finished Operation...Exiting"
