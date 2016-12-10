from __future__ import print_function, division
import json
from pymongo import MongoClient

def get_config():
    with open('dbconfig.json') as config_file:    
        config = json.load(config_file)
        return config

def get_db_string():
    config = get_config()
    db_string = ""
    
    if config["username"]:
        db_string = "mongodb://{0}:{1}@{2}/{3}".format(config["username"], config["password"], config["url"], config["db"])
    else:
        db_string = "mongodb://{0}/{1}".format(config["url"], config["db"])

    return db_string

def get_db_client():
    client = MongoClient(get_db_string())
    db = client[get_config()["db"]]
    return db