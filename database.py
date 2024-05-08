# To add any data you need two arguments name(string) and status of the task which by default is 0
# meaning that task is not yet completed (1 means it is completed)
# Update required 3 arguments which are old_name, new_name, task_status(0 or 1)
# data is stored in the form of task_name, task_status and current date

import sqlite3

class DataBase():
    def __init__(self):
        conn = sqlite3.connect("Task_data.db")
        self.conn = conn
        cur = conn.cursor()
        self.cur = cur
        cur.execute(
            """CREATE TABLE IF NOT EXISTS Task_data(
                    name TEXT,
                    status INTEGER,
                    date_added TEXT
                    )"""
        )
        conn.commit()
    
    def return_data(self):
        self.cur.execute("SELECT * FROM Task_data")
        return self.cur.fetchall()

    def add_data(self, name, status=0, current_date = 0):
        try:
            self.cur.execute(
                "INSERT INTO Task_data (name, status, date_added) VALUES (?, ?, ?)",
                (name, status, current_date),
            )
            self.conn.commit()
            return True
        except Exception as e:
            return f"Error occurred while adding data: {e}: "

    def update_data(self, name, new_name, status=0, current_date=0):
        try:
            self.cur.execute(
                "UPDATE Task_data SET name=?, status=?, date_added=? WHERE name=?",
                (new_name, status, current_date, name),
            )
            self.conn.commit()
            return True
        except Exception as e:
            return f"Error occurred while updating data: {e}:"

    def delete_data(self, name):
        try:
            self.cur.execute("DELETE FROM Task_data WHERE name=?", (name,))
            self.conn.commit()
            return True
        except Exception as e:
            return f"Error occurred while deleting data: {e}:"
