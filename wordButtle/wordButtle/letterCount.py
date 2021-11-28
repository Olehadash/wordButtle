import sqlite3
from sqlite3 import Error

lettabname = "hebltab"

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(r"D:\RestApi\wordButtle\wordButtle\wordButtle\wordButtle\db.sqlite")
    except Error as e:
        print(e)

    return conn

def update_task(col, id):
    coll = conn.execute("SELECT '"+col+"' from "+lettabname+" WHERE id = '"+id+"'")
    sql = " UPDATE "+lettabname+" SET '"+col+"' = "+ (coll+1) +" WHERE id = '"+id+"'"
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()

conn = create_connection()
wordsl = conn.execute('SELECT * from heb')

#letters = ["а", "б", "в", "г", "д","е", "ё", "ж", "з", "и","й", "к", "л", "м", "н","о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч","ш", "щ", "ъ", "ь", "э", "ю", "я"]
#letters = {"a" : 0, "b" : 1, "c":2, "d":3, "e":4,"f":5, "g":6, "h":7, "i":8,
#          "j" :9,"k":10, "l":11, "m":12, "n":13, "o":14,"p":15, "q":16, "r":17, 
#          "s":18, "t":19, "u":20, "v":21, "w":22, "x":23, "y":24,"z":25}

letters = {"א" : 0, "ב" : 1, "ג":2, "ד":3, "ה":4,"ז":5, "ח":6, "ט":7, "י":8,
          "כ" :9,"ך":10, "ל":11, "מ":12, "ם":13, "נ":14,"ן":15, "ס":16, "ע":17, 
          "פ":18, "ף":19, "צ":20, "ץ":21, "ק":22, "ר":23, "ש":24,"ת":25}

keys = list(letters.keys())
table = []

def update_many_task(conn, task):
    conn.execute('SELECT * from hebltab')
    sql = ''' UPDATE hebltab 
              SET l1 = ?, l2 = ?,
              l3 = ?, l4 = ?,
              l5 = ?, l6 = ?,
              l7 = ?, l8 = ?,
              l9 = ?, l10 = ?,
              l11 = ?, l12 = ?,
              l13 = ?, l14 = ?,
              l15 = ?, l16 = ?,
              l17 = ?, l18 = ?,
              l19 = ?, l20 = ?,
              l21 = ?, l22 = ?,
              l23 = ?, l24 = ?,
              l25 = ?, l26 = ?
              WHERE id = ?'''
    cur = conn.cursor()
    cur.executemany(sql, task)
    conn.commit()

def insertTable():
    multilist = [];
    i=0;
    for line in  table:
        line.append(keys[i])
        multilist.append(tuple(line))
        i = i+1
    return multilist

def buildLine ():
    line = []
    for i in range(0,26):
        line.append(0)
    return line


def isLetter(let):
    for l in letters:
        if (l== let):
            return True
    return False
        
count = 0


for i in range(0,26):
    table.append(buildLine())



for word in wordsl:
    
    print(str(count) + ":"+ word[1])
    for i in range(len(word[1])-1):

        if(isLetter(word[1][i]) and isLetter(word[1][i+1])):
            symbol = word[1][i]
            nex_symbol = word[1][i+1]
            #coll = conn.execute("SELECT "+word[0][i]+" from "+lettabname+" WHERE id = '"+word[0][i+1]+"'")
            num =letters[symbol]
            numN = letters[nex_symbol]
            table[num][numN] = table[num][numN] +1
            count = count+1

update_many_task(conn, insertTable())
print (count)
print ("All Count is %d", count)

