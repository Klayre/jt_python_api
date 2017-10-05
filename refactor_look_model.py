# -*- coding: UTF-8 -*-
import sys
import os
import yaml  ### YOU NEED THE pyyaml PACKAGE : [sudo] pip install pyyaml
#from lookerapi import LookerApi
import looker
from pprint import pprint as pp
import json
import string

### ------- HERE ARE PARAMETERS TO CONFIGURE -------

looks_to_modify = sys.argv[1]
new_model_name = sys.argv[2]
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


### ------- GET THE SOURCE LOOK -------

if os.path.isfile(looks_to_modify):
        filelist = open(looks_to_modify)
        for i in filelist:
                print "refactoring lookid: " + str(i)

                lwq = lookApi.look(i)
                look_query_id = lwq.query_id

                print "original query_id: " + str(look_query_id)

                query_object = queryApi.query(look_query_id)
                query_object.model = new_model_name
                query_object.client_id = None 

                new_query = queryApi.create_query(body=query_object)

                print "new query_id: " + str(new_query.id)
                data = {}
                data["query_id"] = new_query.id
                output = lookApi.update_look(i, data)

                print "Done"

else:
	lwq = lookApi.look(looks_to_modify)
        look_query_id = lwq.query_id

        print "original query_id: " + str(look_query_id)
	
	query_object = queryApi.query(look_query_id)
        query_object.model = new_model_name
        query_object.client_id = None

#        pp(query_object.to_str)

	new_query = queryApi.create_query(body=query_object)

#	print "new query is" + json.dumps(new_query)

        print "new query_id: " + str(new_query.id)

	data = {}
	data["query_id"] = new_query.id

	output = lookApi.update_look(looks_to_modify, data)
	
#	pp(output.to_str)	
        
        print "Done"

### ------- DONE -------

print "Finished Operation...Exiting"

