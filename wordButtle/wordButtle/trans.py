from translate import Translator
import translators as ts
import time
from deep_translator import GoogleTranslator, PonsTranslator, LingueeTranslator, PonsTranslator
import sqlite3
from sqlite3 import Error

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(r"D:\RestApi\wordButtle\wordButtle\wordButtle\wordButtle\db.sqlite")
    except Error as e:
        print(e)

    return conn

def update_task(conn, task):
    conn.execute('SELECT * from rus')
    sql = ''' UPDATE rus
              SET eng = ? ,
                  ger = ?
              WHERE word = ?'''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()

conn = create_connection()
conn.execute('SELECT * from rus')

wordsl = conn.execute('SELECT * from rus')
i = 0;
j = 0;
max = 1;
line = "";
for word in wordsl:
    if i>=79436:
        eng = ts.bing(word[1], if_use_cn_host=False)
        ger = ts.bing(word[1], if_use_cn_host=False, to_language = 'de')
        with conn:
            update_task(conn, (eng, ger, word[1]))
        print(i)
        if i%500 == 0:
            time.sleep(30)
    i+=1

input()