import sqlite3




def add_new_wallet(add, pk):
    con = sqlite3.connect('example.db')
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS wallets (address text, privateKey text, value number)""")
    print(pk)
    # Insert a row of data
    cur.execute(f"INSERT INTO wallets VALUES ('{add}', '{pk}')")

    # Save (commit) the changes
    con.commit()

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    con.close()