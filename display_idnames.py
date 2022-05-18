import sqlite3
def main():
    conn = sqlite3.connect('company.sqlite')
    cur = conn.cursor()
    print('Data')
    cur.execute('SELECT empid,ename FROM employee')
    for row in cur:
            print(row)
    conn.close()
if __name__ == '__main__': main()