import sqlite3
from sqlite3 import Error

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(r"D:\RestApi\wordButtle\wordButtle\wordButtle\wordButtle\db.sqlite")
    except Error as e:
        print(e)

    return conn

def update_task(col, id):
    coll = conn.execute("SELECT '"+col+"' from rusLTab WHERE id = '"+id+"'")
    sql = " UPDATE rusLTab SET '"+col+"' = "+ (coll+1) +" WHERE id = '"+id+"'"
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()

conn = create_connection()
wordsl = conn.execute('SELECT * from rus')

letters = ["а", "б", "в", "г", "д","е", "ё", "ж", "з", "и","й", "к", "л", "м", "н","о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч","ш", "щ", "ъ", "ь", "э", "ю", "я"]

def isLetter(let):
    for l in letters:
        if (l== let):
            return True
    return False
        
count = 0
for word in wordsl:
    
    print(word[1])
    for i in range(len(word[1])-1):

        if(isLetter(word[1][i]) and isLetter(word[1][i+1])):
            coll = conn.execute("SELECT "+word[1][i]+" from rusLTab WHERE id = '"+word[1][i+1]+"'")
            try:
                num =int(coll.fetchone()[0])
                sql = " UPDATE rusLTab SET "+word[1][i]+" = "+ str(num+1) +" WHERE id = '"+word[1][i+1]+"'"
                cur = conn.cursor()
                cur.execute(sql)
                conn.commit()
                ##update_task(word[1][i], word[1][i+1])
                count = count+1
            except:
                print("Error")
print (count)
print ("All Count is %d", count)

