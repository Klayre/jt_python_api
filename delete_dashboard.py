import sys
import os
import yaml  ### YOU NEED THE pyyaml PACKAGE : [sudo] pip install pyyaml
#from lookerapi import LookerApi
import looker
from pprint import pprint as pp
import json
import string

### ------- HERE ARE PARAMETERS TO CONFIGURE -------

dashboards_to_delete = sys.argv[1]
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

# instantiate the API
queryApi = looker.QueryApi(client)
lookApi = looker.LookApi(client)

### ------- HANDLE ARGUMENT FILELIST OR SINGLE LOOK -------

if os.path.isfile(dashboards_to_delete):
	filelist = open(dashboards_to_delete)
	for i in filelist:
		print "deleting dashboard id: " + i
		data = lookApi.delete_dashboard(i)
else:
	data = lookApi.delete_dashboard(dashboards_to_delete)

### ------- Done -------

print "Done"

