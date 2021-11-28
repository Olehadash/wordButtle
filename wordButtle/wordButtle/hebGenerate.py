
import time
import sqlite3

letters = {"a" : 0, "b" : 1, "c":2, "d":3, "e":4,"f":5, "g":6, "h":7, "i":8,
          "j" :9,"k":10, "l":11, "m":12, "n":13, "o":14,"p":15, "q":16, "r":17, 
          "s":18, "t":19, "u":20, "v":21, "w":22, "x":23, "y":24,"z":25}
letters = list (letters.keys())

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(r"D:\RestApi\wordButtle\wordButtle\wordButtle\wordButtle\db.sqlite")
    except Error as e:
        print(e)

    return conn

def update_many_task(conn, task):
    conn.execute('SELECT * from eng')
    sql = ''' INSERT INTO heb (word)
                      VALUES(?) '''
    cur = conn.cursor()
    cur.executemany(sql, task)
    conn.commit()

def isHeb(word):
    for letter in word:
        if letter.lower() in letters:
            return False;
    return True

conn = create_connection()
wordsl = conn.execute('SELECT heb from eng')

heb_list = [];

for word in wordsl:
    cur_word = word[0]
    if cur_word == " " or cur_word == "" or cur_word == None: continue
    if isHeb(cur_word):
        heb_list.append(cur_word)

heb_list = sorted(set(heb_list))
insert_tuple = []

for w in heb_list:
    insert_tuple.append((w,))

update_many_task(conn,tuple(insert_tuple))