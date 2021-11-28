import time
import sqlite3
from sqlite3 import Error
import translators as ts
from translate import Translator
from deep_translator import GoogleTranslator

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(r"D:\RestApi\wordButtle\wordButtle\wordButtle\wordButtle\db.sqlite")
    except Error as e:
        print(e)

    return conn

def update_task(conn, task):
    conn.execute('SELECT * from eng')
    sql = ''' UPDATE eng
              SET heb = ?
              WHERE word = ?'''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()

def update_many_task(conn, task):
    conn.execute('SELECT * from eng')
    sql = ''' UPDATE eng
              SET heb = ?
              WHERE word = ?'''
    cur = conn.cursor()
    cur.executemany(sql, task)
    conn.commit()

conn = create_connection()
wordsl = conn.execute('SELECT * from eng')
i = 0;
j = 0;
max = 1;
line = "";

heb_List = []
hebarray = []
trans_line ="";
wline = []

curent_block = 50
last_position = 106950
translator= Translator(to_lang="Hebrew")
for word in wordsl:
    if i <last_position:
        i= i+1
        continue

    try: 
        trans_line = trans_line + word[0] + ",";
        #with conn:
        #    update_task(conn, (eng, ger, word[1]))
        if i%curent_block ==0 or i == 106974:
            #heb_line = ts.bing(trans_line, to_language = "he", if_use_cn_host=False)
            #heb_line = translator.translate(trans_line)
            heb_line = GoogleTranslator(source='auto', target='hebrew').translate(trans_line)
            hebarray = heb_line.split(",")
            wline = trans_line.split(",")
            j = 0
            for heb in hebarray:
                if j > curent_block:
                    break;
                heb_tup = (heb, wline[j])
                heb_List.append(heb_tup)
                j = j+1
            update_many_task(conn, heb_List)
            wline = []
            hebarray = []
            trans_line = ""
            heb_List = []
            hebarray = []
            print (i)
            time.sleep(1)
        i= i+1
    except:
        break;
print (i)

update_many_task(conn, heb_List)

#input()