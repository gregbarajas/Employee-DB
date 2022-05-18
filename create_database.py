import sqlite3

def main():
    conn = sqlite3.connect('company.sqlite')
    cur = conn.cursor()
    cur.execute('DROP TABLE IF EXISTS employee')
    cur.execute('CREATE TABLE employee (empid INT, ename TEXT, designation TEXT) ')
    conn.close()
if __name__ == '__main__':
   main()