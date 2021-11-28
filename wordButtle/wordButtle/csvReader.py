import pandas as pd
import sqlite3
from sqlite3 import Error


def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(r"D:\RestApi\wordButtle\wordButtle\wordButtle\wordButtle\db.sqlite")
    except Error as e:
        print(e)

    return conn

conn = create_connection()

letters = ["f", "g", "h", "e", "j","k", "l", "m", "n", "o","p", "q", "r", "s", "t", "u", "v", "w", "x", "y","z"]
folse_n = "D:\RestApi\wordButtle\wordButtle\wordButtle\wordButtle\wlcsv\\"

p_word = ""
for l in letters:
    letter = str(l)
    letter = letter.upper()
    filepath = folse_n + letter +'word.csv'
    df = pd.read_csv(folse_n + letter +'word.csv', delimiter=',',engine='python', error_bad_lines=False , quotechar='"',encoding='cp1252')

    # User list comprehension to create a list of lists from Dataframe rows
    list_of_rows = [list(row) for row in df.values]

    print (letter)
    coun = 0
    # Print list of lists i.e. rows
    for w in list_of_rows:
        word = str(w)
        word = word.replace("[", "")
        word = word.replace("]", "")
        word = word.replace("'", "")
        word = word.replace(" ", "")
        if(p_word != word):
            coun = coun+1
            sql = ''' INSERT INTO eng (word)
                      VALUES(?) '''
            data_tuple = (word,)
            cur = conn.cursor()
            cur.execute(sql, data_tuple)
            conn.commit()
            
        p_word = word
        if coun == 100:
            print(word)
            coun = 0

