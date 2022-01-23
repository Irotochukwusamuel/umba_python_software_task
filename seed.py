import requests
from requests.exceptions import ConnectionError
import sqlite3
import os.path
import logging

import root
from modules.table_models import Model

url_link = requests.get("https://api.github.com/users?accept=application/vnd.github.v3+json&per_page=100")

# Instantiate the Table Model objects
model = Model()

# create a table
model.create_table(root.table_name)

total = 100  # default total number of users


def StimulateApi(total_number_of_users=150):
    interval = 0  # number of times to make the request

    while interval < total_number_of_users:

        # converting the return data in a json data

        res = url_link.json()

        # adding each data into
        for x in res:
            model.insertData(f"insert into {root.table_name}(username,avatar_url,type,url) values (?,?,?,?)",
                             values=(x["login"], x["avatar_url"], x["type"], x["url"]))
            interval += 1

            if interval >= total_number_of_users:
                break


try:
    StimulateApi(total)
except NameError:
    StimulateApi()
