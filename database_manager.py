import sqlite3


class DatabaseManager:
    name = None

    def __init__(self, base_name="it_happens_base.sqlite"):
        self.name = base_name

    def create_table(self):
        conn = sqlite3.connect(self.name)
        cur = conn.cursor()
        cur.execute("""
                    CREATE TABLE stories 
                    (id integer primary key , headline text, timestamp integer, tags_pairs text, story_text text, 
                    likes_cnt integer 
                    );
                """)
        conn.close()

    def drop_table(self):
        conn = sqlite3.connect(self.name)
        cur = conn.cursor()
        cur.execute("DROP TABLE stories;")
        conn.close()

    def insert_story(self, story_data_tuple):
        conn = sqlite3.connect(self.name)
        cur = conn.cursor()
        cur.execute(
            f"""INSERT INTO stories ( id, headline, timestamp, tags_pairs, story_text, likes_cnt ) 
                            VALUES ( ?, ?, ?, ?, ?, ? );""", story_data_tuple)
        conn.commit()
        conn.close()

    def get_story(self, story_id):
        conn = sqlite3.connect(self.name)
        cur = conn.cursor()
        cur.execute(f"""SELECT * FROM stories WHERE id == ?;""", (story_id,))
        results = cur.fetchall()
        conn.close()
        return results
