import unittest
from modules.table_models import Model


class TestModel(unittest.TestCase):

    def setUp(self):
        self.table_name = "test_table"
        self.model = Model()
        self.user_data = [
            {
                "username": "dummy_username1",
                "avatar_url": "https://dummy_avatar_url1",
                "type": "dummy_organization1",
                "url": "https://dummy_url1"
            },
            {
                "username": "dummy_user2",
                "avatar_url": "https://dummy_avatar_url2",
                "type": "dummy_organization2",
                "url": "https://dummy_url2"
            }
        ]

    def tearDown(self):
        self.model.cleanup(self.table_name)

    def test_model(self):
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

        # test when trying to select the username of none existing ID  and result should return False
        res = self.model.selectOneData(f"select username from {self.table_name} where id=?", value=(2,))
        self.assertFalse(res, 0)

        # test adding a second data into row
        res = self.model.insertData(f"insert into {self.table_name} (username,avatar_url,type,url) values (?,?,?,?)",
                                    values=(self.user_data[1]["username"],
                                            self.user_data[1]["avatar_url"],
                                            self.user_data[1]["type"],
                                            self.user_data[1]["url"]))
        self.assertTrue(res)

        # test when trying to get a data from a column of  existing ID and the result return should be list and greater than 0
        res = self.model.selectOneData(f"select username from {self.table_name} where id=?", value=(2,))
        self.assertGreater(len(res), 0)

        # test select multiple data from a row
        res = self.model.selectMultipleData(f"select * from {self.table_name} where id=?", value=(2,))
        self.assertGreater(len(res), 0)


if __name__ == "__main__":
    unittest.main()
