import sqlite3


class DatabaseManager:
    name = None

    def __init__(self, base_name="it_happens_base.sqlite"):
        self.name = base_name

    def create_table(self):
        with sqlite3.connect(self.name) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    CREATE TABLE stories 
                    (id, 
                    )
                """)

    def drop_table(self):
        with sqlite3.connect(self.name) as conn:
            with conn.cursor() as cur:
                cur.execute("DROP TABLE `stories`")
