import json

import root
import seed

from modules.table_models import Model
from database import db
import math
import logging

logging.basicConfig(level=logging.DEBUG)


class Validation:

    def __init__(self):
        self.model = Model()
        self.cursor = db.cursor()

    def filter_API_By_Pagination_And_Page(self, table, pagination=25, page=1):
        """

        :param pagination: maximum number of records to return from table

        :param page: number of rows to skip before returning data

        :return: json data of all the results retrieve from the table
        """

        # if pagination value has 0 or negative value it resets the value to default (25)
        if int(pagination) <= 0:
            pagination = 25

        # if page value has 0 or negative value it resets the value to default (0)
        if int(page) <= 0:
            page = 0

        res = self.model.selectMultipleData(f"select * from {table} order by id limit ? offset ?",
                                            value=(pagination, (page - 1) * pagination))

        data_arr = []  # an array to store datas
        if len(res) <= 0:
            return {
                "error": f"The Page you entered exceeds the total pages ({int(math.ceil(seed.total / int(pagination)))}) "}
        else:
            for x in res:
                data_arr.append({
                    "id": x[0],
                    "username": x[1],
                    "avatar_url": x[2],
                    "type": x[3],
                    "url": x[4]
                })
            return {
                "data": data_arr
            }  # dumps the data as json

    def fetch_API(self, table, page=1, pagination=25, username=None, user_id=None, order_by="id"):

        query = []

        if (type(username) == str) and (username is not None):
            query.append(f"where username='{username}'")  # append this value if username is not None and is a string

        # validating the id value. check if id is integer and if it is greater than the max id on the table
        if username is not None and type(username) == str:
            if user_id is not None and type(user_id) == int:
                query.append(f"id={user_id}")  # appends this value if username and user_id meets the statement criteria

        else:
            if user_id is not None and type(user_id) == int:
                if int(user_id) <= seed.total:
                    query.append(
                        f"where id={user_id}")  # appends this value if username and user_id meets the statement criteria
                else:
                    logging.info(f"The id is greater than the max id {seed.total} currently fetched from the API")

        # checking if page value is number and if it is greater than the max page limit
        if type(page) != int:
            logging.info("The page value is not a number..resetting it value to 0")
            page = 0  # resetting the value to 0
        else:
            max_page = int(math.ceil(seed.total / int(pagination)))
            if int(page) > max_page:
                logging.info(f"The page value is greater than the max value : {max_page} ..resetting it value to 0")
                page = 0  # resetting the value to 0
            if int(page) <= 0:
                logging.info(f"Invalid page value : {page} ..resetting it value to 0")
                page = 0  # resetting the value to 0

        # checking if values in order_by has id or type
        if order_by.lower() not in ["id", "type"] and type(order_by) != str:
            logging.info(f"Invalid order type value : {order_by} ..resetting it value to id")
            order_by = "id"  # resetting the value to 0

        # final fetching of data
        res = self.model.selectMultipleData(f"select * from {table} {' and '.join(query)} order by ? limit ? offset ?",
                                            value=(order_by, pagination, (page - 1) * pagination))

        return self.endResult(res)  # returns data as a dict

    @staticmethod
    def endResult(data):
        empty_arr = []
        for x in data:
            empty_arr.append({
                "id": x[0],
                "username": x[1],
                "avatar_url": x[2],
                "type": x[3],
                "url": x[4]
            })
        if len(empty_arr) <= 0:
            return {
                "data": "NOT FOUND!, Please check your input"
            }  # dumps the data as json
        else:
            return {
                "data": empty_arr
            }  # dumps the data as json



