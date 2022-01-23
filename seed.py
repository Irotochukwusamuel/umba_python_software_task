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


dummy = [
    {
        "login": "mojombo",
        "id": 1,
        "node_id": "MDQ6VXNlcjE=",
        "avatar_url": "https://avatars.githubusercontent.com/u/1?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/mojombo",
        "html_url": "https://github.com/mojombo",
        "followers_url": "https://api.github.com/users/mojombo/followers",
        "following_url": "https://api.github.com/users/mojombo/following{/other_user}",
        "gists_url": "https://api.github.com/users/mojombo/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/mojombo/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/mojombo/subscriptions",
        "organizations_url": "https://api.github.com/users/mojombo/orgs",
        "repos_url": "https://api.github.com/users/mojombo/repos",
        "events_url": "https://api.github.com/users/mojombo/events{/privacy}",
        "received_events_url": "https://api.github.com/users/mojombo/received_events",
        "type": "User",
        "site_admin": False
    },
    {
        "login": "defunkt",
        "id": 2,
        "node_id": "MDQ6VXNlcjI=",
        "avatar_url": "https://avatars.githubusercontent.com/u/2?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/defunkt",
        "html_url": "https://github.com/defunkt",
        "followers_url": "https://api.github.com/users/defunkt/followers",
        "following_url": "https://api.github.com/users/defunkt/following{/other_user}",
        "gists_url": "https://api.github.com/users/defunkt/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/defunkt/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/defunkt/subscriptions",
        "organizations_url": "https://api.github.com/users/defunkt/orgs",
        "repos_url": "https://api.github.com/users/defunkt/repos",
        "events_url": "https://api.github.com/users/defunkt/events{/privacy}",
        "received_events_url": "https://api.github.com/users/defunkt/received_events",
        "type": "User",
        "site_admin": False
    },
    {
        "login": "pjhyett",
        "id": 3,
        "node_id": "MDQ6VXNlcjM=",
        "avatar_url": "https://avatars.githubusercontent.com/u/3?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/pjhyett",
        "html_url": "https://github.com/pjhyett",
        "followers_url": "https://api.github.com/users/pjhyett/followers",
        "following_url": "https://api.github.com/users/pjhyett/following{/other_user}",
        "gists_url": "https://api.github.com/users/pjhyett/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/pjhyett/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/pjhyett/subscriptions",
        "organizations_url": "https://api.github.com/users/pjhyett/orgs",
        "repos_url": "https://api.github.com/users/pjhyett/repos",
        "events_url": "https://api.github.com/users/pjhyett/events{/privacy}",
        "received_events_url": "https://api.github.com/users/pjhyett/received_events",
        "type": "User",
        "site_admin": False
    },
    {
        "login": "wycats",
        "id": 4,
        "node_id": "MDQ6VXNlcjQ=",
        "avatar_url": "https://avatars.githubusercontent.com/u/4?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/wycats",
        "html_url": "https://github.com/wycats",
        "followers_url": "https://api.github.com/users/wycats/followers",
        "following_url": "https://api.github.com/users/wycats/following{/other_user}",
        "gists_url": "https://api.github.com/users/wycats/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/wycats/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/wycats/subscriptions",
        "organizations_url": "https://api.github.com/users/wycats/orgs",
        "repos_url": "https://api.github.com/users/wycats/repos",
        "events_url": "https://api.github.com/users/wycats/events{/privacy}",
        "received_events_url": "https://api.github.com/users/wycats/received_events",
        "type": "User",
        "site_admin": False
    }]


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
