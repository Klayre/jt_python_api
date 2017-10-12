# -*- coding: UTF-8 -*-
import sys
import os
import yaml  ### YOU NEED THE pyyaml PACKAGE : [sudo] pip install pyyaml
#from lookerapi import LookerApi
import looker
from pprint import pprint as pp
import json
import string
import ast
from ast import NodeVisitor

### ------- HERE ARE PARAMETERS TO CONFIGURE -------

looks_to_modify = sys.argv[1]
new_explore_name = sys.argv[2]
host = 'meta'


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

### ------- DEFINE REFACTORING METHODS ------- ###

#input: List, List
def refactor_remove_filter(refactor_target, items_to_remove):
        for key in refactor_target.keys():
                if any(x in key for x in items_to_remove):
                        print "deleting non-existent filter_config..."
                        del refactor_target[key]

#input: List
def refactor_rename_fields(refactor_target):
        field_list = refactor_target
        for index, field in enumerate(field_list):
                print str(field)

                if "client_period_health_score" in field:
                        qualified_field = field.split(".")
                        new_field = "client_daily_health_score" + "." + qualified_field[1]
                        field_list[index] = new_field                       

                if "account_period_status" in field:
                        qualified_field = field.split(".")
                        new_field = "account_daily_status" + "." + qualified_field[1]
                        field_list[index] = new_field

                if "cs_health_calendar" in field:
                        qualified_field = field.split(".")
                        if "periods_ago" in qualified_field[1]:
                                new_field = "cs_health_calendar_daily.calendar_month"
                        else:
                                new_field = "cs_health_calendar_daily" + "." + qualified_field[1]
                        field_list[index] = new_field

                if "user_daily_activity.user_count_by" in field:
                        new_field = "client_daily_health_score.user_count"
                        field_list[index] = new_field

                if "license_status.name" in field:
                        new_field = "license_facts.license_status_name"
                        field_list[index] = new_field   

                if "license_type.name" in field:
                        new_field = "license_facts.license_type_name"
                        field_list[index] = new_field     

                if "account_current_facts." in field:
                        qualified_field = field.split(".")
                        new_field = "account_facts" + "." + qualified_field[1]
                        field_list[index] = new_field    

                if "license_monthly_active_users.total_active_users" in field:
                        new_field = 'client_daily_health_score.user_count'
                        field_list[index] = new_field     



### ------- GET THE SOURCE LOOK -------

if os.path.isfile(looks_to_modify):
        filelist = open(looks_to_modify)
        for i in filelist:
                print "refactoring lookid: " + str(i)

                lwq = lookApi.look(i)
                look_query_id = lwq.query_id

                print "original query_id: " + str(look_query_id)

                query_object = queryApi.query(look_query_id)


                query_object.view = new_explore_name
                query_object.client_id = None 

                pp(query_object.to_str())

                new_query = queryApi.create_query(body=query_object)

                print "new query_id: " + str(new_query.id)
                data = {}
                data["query_id"] = new_query.id
                output = lookApi.update_look(i, data)

                print "Done"

else:
        # --- DEFINE REPLACEMENT DICTS --- #
        items_to_remove = []
        items_to_replace = ["license_status","license_type.license_type_name"]

        # -- GET QUERY UNDERLYING THE LOOK --- #

	lwq = lookApi.look(looks_to_modify)
        look_query_id = lwq.query_id

        print "original query_id: " + str(look_query_id)
	
	query_object = queryApi.query(look_query_id)
        query_object.view = new_explore_name
        query_object.client_id = None

        # --- REFACTOR FIELDS PARAM --- #

        print "---BEGIN: Refactoring Fields, Fill Fields, Pivots, and Sorts ---"

        field_list = query_object.fields
        refactor_rename_fields(field_list)

        if query_object.fill_fields is not None:
                field_list = query_object.fill_fields
                refactor_rename_fields(field_list)
       
        if query_object.sorts is not None:
                field_list = query_object.sorts
                refactor_rename_fields(field_list)

        if query_object.pivots is not None:
                field_list = query_object.pivots
                refactor_rename_fields(field_list)

        print "---END: Refactoring Fields, Fill Fields, Pivots, and Sorts ---"
        
        print "---BEGIN: Refactoring Filter Config---"

        fc_dict = query_object.filter_config
        fc_itr = items_to_replace
        refactor_remove_filter(fc_dict, items_to_remove)
        for key in fc_dict.keys():     
                print key
                if "cs_health_calendar.current_period_only" in key:                        
                        root = ast.literal_eval(fc_dict[key])
                        root[0]["type"] = "advanced"
                        root[0]["values"][0]["constant"] = "yesterday"
                        fc_dict[key] = root
                        fc_dict["cs_health_calendar_daily.calendar_date"] = fc_dict.pop(key)


                if "calendar.current_period_only" == key:                        
                        root = ast.literal_eval(fc_dict[key])
                        root[0]["type"] = "advanced"
                        root[0]["values"][0]["constant"] = "yesterday"
                        fc_dict[key] = root
                        fc_dict["cs_health_calendar_daily.calendar_date"] = fc_dict.pop(key)


                if "cs_health_calendar.periods_ago" in key:                        
                        root = ast.literal_eval(fc_dict[key])
                        root[0]["type"] = "advanced"
                        root[0]["values"][0]["constant"] = "yesterday"
                        fc_dict[key] = root
                        fc_dict["cs_health_calendar_daily.calendar_date"] = fc_dict.pop(key)


                if "calendar.periods_ago" == key:                        
                        root = ast.literal_eval(fc_dict[key])
                        root[0]["type"] = "advanced"
                        root[0]["values"][0]["constant"] = "yesterday"
                        fc_dict[key] = root
                        fc_dict["cs_health_calendar_daily.calendar_date"] = fc_dict.pop(key)


                if "account_current_facts.next_renewal_month" in key:
                        fc_dict["account_facts.next_renewal_month"] = fc_dict.pop(key) 
                if "account_current_facts.next_renewal_month" in key:
                        fc_dict["account_facts.next_renewal_date"] = fc_dict.pop(key)             
                if "license_status.name" in key:
                        fc_dict["license_facts.license_status_name"] = fc_dict.pop("license_status.name")             
                if "license_type.name" in key:
                        fc_dict["license_type.license_type_name"] = fc_dict.pop("license_type.name")             
        
        

        print "---END: Refactoring Filter Config---"

        print "---BEGIN: Refactoring Filters---"

        filter_dict = query_object.filters 
        filter_itr = items_to_replace
        refactor_remove_filter(filter_dict, items_to_remove)
        for key in filter_dict.keys():
                if "cs_health_calendar.current_period_only" in key:
                        filter_dict["cs_health_calendar_daily.calendar_date"] = filter_dict.pop(key)

                if "calendar.current_period_only" == key:
                        filter_dict["cs_health_calendar_daily.calendar_date"] = filter_dict.pop(key)

                if "cs_health_calendar.periods_ago" in key:
                        filter_dict["cs_health_calendar_daily.calendar_date"] = filter_dict.pop(key)

                if "calendar.periods_ago" == key:
                        filter_dict["cs_health_calendar_daily.calendar_date"] = filter_dict.pop(key)

                if "license_status.name" in key:
                        filter_dict["license_facts.license_status_name"] = filter_dict.pop("license_status.name")             
                if "license_type.name" in key:
                        filter_dict["license_type.license_type_name"] = filter_dict.pop("license_type.name")  
                if "account_current_facts.next_renewal_month" in key:
                        filter_dict["account_facts.next_renewal_month"] = filter_dict.pop(key)             
                if "account_current_facts.next_renewal_date" in key:
                        filter_dict["account_facts.next_renewal_date"] = filter_dict.pop(key)              

        print "---END: Refactoring Filters---"
        
        # --- REFACTOR VIZ_CONFIG PARAM --- #

        vc_dict = query_object.vis_config

        if vc_dict.get("hidden_fields") is not None:
                hidden_fields = vc_dict["hidden_fields"]
                hf_dict = eval(hidden_fields)
                for index, field in enumerate(hf_dict):
                        print str(field)

                        if "calendar.periods_ago" in field:
                                new_field = "calendar.calendar_month"
                                hf_dict[index] = new_field

                        if "account_period_health_score" in field:
                                qualified_field = field.split(".")
                                new_field = "account_daily_health_score" + "." + qualified_field[1]
                                hf_dict[index] = new_field  

                        if "account_period_status" in field:
                                qualified_field = field.split(".")
                                new_field = "account_daily_status" + "." + qualified_field[1]
                                hf_dict[index] = new_field  

                        if "user_daily_activity.user_count_by" in field:
                                new_field = "client_daily_health_score.user_count"
                                hf_dict[index] = new_field

                vc_dict["hidden_fields"] = str(hf_dict)
        

        print "---Refactoring Hidden Fields Complete---"
        
        print " ----------- QUERY BODY ------------- "

        df_join = "".join(query_object.dynamic_fields)     
        query_object.dynamic_fields = df_join

        #json_query_object = json.dumps(query_object.__dict__)

        print query_object

	new_query = queryApi.create_query(body=query_object)

        print "new query_id: " + str(new_query.id)

	data = {}
	data["query_id"] = new_query.id

	output = lookApi.update_look(looks_to_modify, data)
        
        print "Done"

### ------- DONE -------

print "Finished Operation...Exiting"

