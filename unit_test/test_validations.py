import math
import unittest
from modules.table_models import Model
from modules.validations import Validation


class TestValidation(unittest.TestCase):

    def setUp(self):
        self.table_name = "test_table"
        self.model = Model()
        self.validate = Validation()
        self.user_data = [
            {"id": 1,
             "username": "dummy_username1",
             "avatar_url": "https://dummy_avatar_url1",
             "type": "dummy_organization1",
             "url": "https://dummy_url1"
             },
            {
                "id": 2,
                "username": "dummy_user2",
                "avatar_url": "https://dummy_avatar_url2",
                "type": "dummy_organization2",
                "url": "https://dummy_url2"
            }
        ]

    def tearDown(self):
        self.model.cleanup(self.table_name)

    def test_validation(self):
        # the expected results from the database
        db_data1 = {"id": self.user_data[0]["id"],
                    "username": self.user_data[0]["username"],
                    "avatar_url": self.user_data[0]["avatar_url"],
                    "type": self.user_data[0]["type"],
                    "url": self.user_data[0]["url"]
                    }

        db_data2 = {"id": self.user_data[1]["id"],
                    "username": self.user_data[1]["username"],
                    "avatar_url": self.user_data[1]["avatar_url"],
                    "type": self.user_data[1]["type"],
                    "url": self.user_data[1]["url"]
                    }

        # if table doesn't exist
        self.assertFalse(self.model.check_if_table_exist(self.table_name),
                         f"table {self.table_name} does not exist")

        # creating table and test if exist
        self.model.create_table(self.table_name)
        self.assertTrue(self.model.check_if_table_exist(self.table_name), f"table {self.table_name} does exist")

        # test adding record into row
        res = self.model.insertData(f"insert into {self.table_name} (username,avatar_url,type,url) values (?,?,?,?)",
                                    values=(self.user_data[0]["username"],
                                            self.user_data[0]["avatar_url"],
                                            self.user_data[0]["type"],
                                            self.user_data[0]["url"]))
        self.assertTrue(res)

        # test filter by page
        res = self.validate.filter_API_By_Pagination_And_Page(self.table_name, page=1)
        self.assertEqual(res, {"data": [db_data1]})

        # test if page is greater than max page
        res = self.validate.filter_API_By_Pagination_And_Page(self.table_name, page=33)
        self.assertEqual(res, {'error': 'The Page you entered exceeds the total pages (4) '})

        # test filter by pagination
        res = self.validate.filter_API_By_Pagination_And_Page(self.table_name, pagination=1)
        self.assertEqual(res, {"data": [db_data1]})

        # test adding second record into row
        res = self.model.insertData(f"insert into {self.table_name} (username,avatar_url,type,url) values (?,?,?,?)",
                                    values=(self.user_data[1]["username"],
                                            self.user_data[1]["avatar_url"],
                                            self.user_data[1]["type"],
                                            self.user_data[1]["url"]))
        self.assertTrue(res)

        # test filter by page II
        res = self.validate.filter_API_By_Pagination_And_Page(self.table_name, page=1)
        self.assertEqual(res, {"data": [db_data1, db_data2]})

        # test filter by pagination II
        res = self.validate.filter_API_By_Pagination_And_Page(self.table_name, pagination=2)
        self.assertEqual(res, {"data": [db_data1, db_data2]})

        # test filter by pagination and page
        res = self.validate.filter_API_By_Pagination_And_Page(self.table_name, pagination=2, page=1)
        self.assertEqual(res, {"data": [db_data1, db_data2]})

        # test the fetch api method with value username
        res = self.validate.fetch_API(self.table_name, username=self.user_data[0]["username"])
        self.assertEqual(res, {"data": [db_data1]})

        # test the fetch api method with value username and id
        res = self.validate.fetch_API(self.table_name, username=self.user_data[0]["username"],
                                      user_id=self.user_data[0]["id"])
        self.assertEqual(res, {"data": [db_data1]})

        # test the fetch api method with value pagination
        res = self.validate.fetch_API(self.table_name, username=self.user_data[0]["username"],
                                      user_id=self.user_data[0]["id"])
        self.assertEqual(res, {"data": [db_data1]})

        # test when username does not exist
        res = self.validate.fetch_API(self.table_name, username="ajshajkshjh", page=1)
        self.assertFalse(type(res['data']) == list)

        # test order by id
        res = self.validate.fetch_API(self.table_name, order_by="type")
        self.assertEqual(res, {"data": [db_data1, db_data2]})

        # test the end result method
        res = self.validate.endResult([(self.user_data[0]["id"],
                                       self.user_data[0]["username"],
                                       self.user_data[0]["avatar_url"],
                                       self.user_data[0]["type"],
                                       self.user_data[0]["url"])])
        self.assertEqual(res, {"data": [db_data1]})


if __name__ == "__main__":
    unittest.main()
