from database import db
import root


class Model:
    def __init__(self):
        self.cursor = db.cursor()

    def create_table(self, tablename, col1="username", col2="avatar_url", col3="type", col4="url"):
        """
            Checks if the table exist

            1. if table exist, it drops the table.
            2. if table does not exist, it creates a new table.
        """
        if not self.check_if_table_exist(tablename):
            sql = f"""create table {tablename}  (
                    id integer primary key autoincrement not null,
                    {col1} varchar(225) not null,
                    {col2} varchar(225) not null,
                    {col3} varchar(50) not null,
                    {col4} varchar(200) not null
                );"""
            self.cursor.execute(sql)
        else:
            self.cursor.execute(f'delete from {tablename}')
            self.cursor.execute(f'UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME="{tablename}"')
            db.commit()

    def check_if_table_exist(self, table_name):

        """
            Checks if table exists

        :return: boolean ( True or False)

        """
        res = self.selectOneData(f" SELECT count(name) FROM sqlite_master WHERE type=? AND name=?",
                                 value=('table', table_name))
        return bool(res)

    def insertData(self, sql, values):
        """
            Checks if table exist and if table doesn't exist,
            it creates table, and then it can write into table successfully

        :param sql: The sql statement to execute
        :param values: The values to execute inside the sql statement
        :return: boolean (True or False)
        """

        sql = sql
        val = values
        self.cursor.execute(sql, val)
        db.commit()
        if self.cursor.rowcount == 1:
            return True
        else:
            return False

    def selectOneData(self, sql, value):

        """
            This method gets a single data from the designated column of the database.

        :param sql: The sql statement to execute
        :param value: The values to execute inside the sql statement
        :return: if the data is found it returns a string or int else it returns a False
        """
        sql = sql
        val = value
        self.cursor.execute(sql, val)
        result = self.cursor.fetchone()
        if result is not None:
            for x in result:
                return x
            else:
                return False
        else:
            return False

    def selectMultipleData(self, sql, value):

        """
            This method gets multiple datas from the designated row of the table

        :param sql: The sql statement to execute
        :param value: The values to execute inside the sql statement
        :return: if the data is found it returns a List containing the data  else it returns a False

        """

        sql = sql
        val = value
        self.cursor.execute(sql, val)
        result = self.cursor.fetchall()
        if result is not None:
            return result
        else:
            return False

    def cleanup(self, table_name):
        self.cursor.execute(f'drop table {table_name}')
        db.commit()
        self.cursor.close()
