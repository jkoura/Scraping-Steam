# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


# alter cote: class QuotetutorialPipeline:
# def process_item(self, item, spider):
# return item

#Felix Code
import sqlite3


class WorkshopCommentsPipeline:

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect("comments_mod.db")
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("DROP TABLE IF  EXISTS comments_tb")
        self.curr.execute("""CREATE TABLE comments_tb (
                         time text,
                         comments text
                            )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute("""INSERT INTO comments_tb VALUES (?,?)""", (
            item['post_author'][0],
            item['post_time'][0],
            item['post_content'][0]
        ))

        self.conn.commit()
