# Inventorybckend
# Created By Rohit Kapuria
# Sqlite3 Database of Pharmacy Management System
import sqlite3


def storeData():
    con = sqlite3.connect("Store.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Store(id INTEGER PRIMARY KEY, ReferenceNo text,DistributorName text,Date text,\
    MobileNo text,ExpDate text,Medicine text,Amount text,Payment text)")
    con.commit()
    con.close()

def addRegRec( ReferenceNo ,DistributorName,Date,MobileNo ,ExpDate,Medicine,Amount,Payment):
    con = sqlite3.connect("Store.db")
    cur = con.cursor()
    cur.execute("INSERT INTO Store VALUES (NULL, ?,?,?,?,?,?,?,?)",( ReferenceNo ,DistributorName,Date ,MobileNo ,ExpDate,Medicine,Amount,Payment))
    con.commit()
    con.close()

def displayData1():
    con=sqlite3.connect("Store.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM Store")
    rows =cur.fetchall()
    con.close()
    return rows

def displayData():
    con=sqlite3.connect("Store.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM Store")
    rows =cur.fetchall()
    con.close()
    return rows

def deleteRecord(id):
    con=sqlite3.connect("Store.db")
    cur=con.cursor()
    cur.execute("DELETE FROM Store WHERE id=?",(id,))
    con.commit()
    con.close()



def update(id, ReferenceNo="" ,DistributorName="",Date="",MobileNo="" ,ExpDate="",Medicine="",Amount="",Payment=""):
    con=sqlite3.connect("Store.db")
    cur=con.cursor()
    cur.execute("UPDATE Store SET ReferenceNo=? OR DistributorName=? OR Date=? OR MobileNo=? OR \
    ExpDate=? OR Medicine=? OR Amount=? OR Payment=? WHERE id=?",\
                ( ReferenceNo ,DistributorName,Date ,MobileNo ,ExpDate,Medicine,Amount,Payment,id))
    con.commit()
    con.close()

storeData()
