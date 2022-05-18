import sqlite3
conn = sqlite3.connect('company.sqlite')

def get_input():
    input_data = []
    while True:
        empid = input('Input the ID of the user, 99 to quit')
        if empid == '99':
            break
        first_name = input('Write the user\'s first name')
        last_name = input('Write the user\'s last name')
        input_data.append((empid, first_name, last_name))
    return input_data

def insert_to_database(records):
    for empid, first_name, last_name in records:

        cur.execute(f'INSERT INTO employee (empid, ename, designation) VALUES ({empid}, {first_name}, {last_name})')

def main():
    cur = conn.cursor()
    results = get_input()
    print(results)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()

"""cur.execute('INSERT INTO employee (empid, ename, designation) VALUES (?,?,?)', (210, 'Ahmed', 'Instructor'))

    cur.execute('INSERT INTO employee (empid, ename, designation) VALUES (?,?,?)', (211, 'Kamal', 'Instructor'))

    cur.execute('INSERT INTO employee (empid, ename, designation) VALUES (?,?,?)', (212, 'Zeeshan', 'Instructor'))

    cur.execute('INSERT INTO employee (empid, ename, designation) VALUES (?,?,?)', (213, 'Zunaina', 'Instructor'))

    cur.execute('INSERT INTO employee (empid, ename, designation) VALUES (?,?,?)', (214, 'Qaiser', 'Professor'))

    cur.execute('INSERT INTO employee (empid, ename, designation) VALUES (?,?,?)',
                (215, 'Shakeel', 'Assistant Professor'))"""