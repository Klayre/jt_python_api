# Python API Samples
Python examples of how to use the Looker API

## What you can find here
- A copy of the Looker API 3.0 SDK
- Sample files of various tasks using the API

## Relevant Articles
**Moving Looks**: https://discourse.looker.com/t/moving-a-look-between-looker-servers-using-the-looker-api-and-the-python-requests-library/

## Getting Started
- Clone/Download the Repo.
- Create a config.yml file with the following format:

```
hosts:
 'localhost':
    host: 'https://domain.looker.com:19999/api/3.0/'
    secret: 'asdfjkl'
    token: 'qweruiop'
```

- Run any file in the shell with `python <<filename>> arg1`

## Scripts

|File|Description|How to|Example
|----|----|----|----|
|delete_look.py|Illustrates how to delete a look or a list of looks delimited by newlines|Make sure you have the host in your config.yml file and adjust the source look variables at the top of the script.|python delete_look.py 14
|delete_dashboard.py|Illustrated how to delete a dashboard or a list of dashboards delimited by newlines|Make sure you have the host in your config.yml file and adjust the source look variables at the top of the script.|python delete_dashboard.py list.txt 
|refactor_look_model.py|Allows you to change the model that a Look (or list of Looks) is powered by|Make sure you have the host in your config.yml file and adjust the source look variables at the top of the script.|python refactor_look_model.py 25 new_model
|get_look.py|Illustrates how to get the data from a look|Make sure you have the host in your config.yml file and adjust the source look variables at the top of the script.|
|move_look.py|Illustrates how to move a look between servers, or between the same server|Make sure you have both hosts in your config.yml file and adjust the source look, destination space variables at the top of the script.|
|get_data_dictionary.py|Put together a list of each field, and various attributes in your data model, this outputs a CSV|Make sure your host is configured in the config.yml file|python 
