import sqlite3
from web3 import Web3
from dotenv import load_dotenv   
import os
load_dotenv()

LINK = os.environ.get("LINK")
GANACHE = os.environ.get("GANACHE")

w3 = Web3(Web3.HTTPProvider(GANACHE))



def add_new_wallet(add, pk):
    con = sqlite3.connect('db.db')
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS wallets (address text, privateKey text, value text)""")
    print(pk)
    # Insert a row of data
    cur.execute(f"INSERT INTO wallets VALUES ('{add}', '{pk}', 0)")

    # Save (commit) the changes
    con.commit()

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    con.close()

def update_bal(add):
    print(add)
    con = sqlite3.connect('db.db')
    cur = con.cursor()
    raw_val = w3.eth.getBalance(add)
    eth_val = w3.fromWei(raw_val, 'ether')
    print(eth_val)
    sql_update_query = """Update wallets set value = ? where address = ?"""
    data = (str(eth_val), add)
    cur.execute(sql_update_query, data)
    con.commit()
    con.close()