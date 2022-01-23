import os
import sqlite3 as sqlite_db
import root

DEFAULT_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                            root.database_name)  # creating the database on the root directory of this file.

db = sqlite_db.connect(DEFAULT_PATH, check_same_thread=False)
