employees = []  # note naming style
names = []
# counter = 0
# DIR = r"C:\Users\ebara\Downloads\"
DIR = ""


def export_employees():
    print(employees)
    with open(DIR + "database.csv", "w") as output:
        for employee in employees:
            output.write(', '.join(employee) + '\n')

def search_id():
    id = input("Enter employee ID: ")
    for employee in employees:
        if id == employee[10]:
            print("--------------" + employee[0] + "---------------")
            print("SSN: " + employee[1])
            print("Phone: " + employee[2])
            print("Email: " + employee[3])
            print("Salary: $" + employee[4])
            print("Address" + employee[5])
            print("Date of Birth: " + employee[6])
            print("Job Title: " + employee[7])
            print("Start Date: " + employee[8])
            print("End Date: " + employee[9])
            print("Employee ID: " + employee[10])
            return employee
    return -1

def edit_employee():
    name = input("Enter the new Name of employee: ")
    ssn = input("Enter the new SSN of employee: ")
    phone = input("Enter the new Phone Number of employee: ")
    email = input("Enter the new Email of employee: ")
    salary = input("Enter the new Salary of employee: ")
    address = input("Enter the new Address of employee: ")
    date_of_birth = input("Enter the new Date of Birth of employee: ")
    job_title = input("Enter the new Job Title of employee: ")
    start_date = input("Enter the new Start Date of employee: ")
    end_date = input("Enter the new End Date of employee: ")
    employee_id = input("Enter the new ID of employee: ")
    search[0] = name
    search[1] = ssn
    search[2] = phone
    search[3] = email
    search[4] = salary
    search[5] = address
    search[6] = date_of_birth
    search[7] = job_title
    search[8] = start_date
    search[9] = end_date
    search[10] = employee_id


def add_employee():
    counter = len(employees)
    while True:
        print("----------------------------------------------\n")
        print("         Number of Employee ({0:d})".format(counter))
        print("----------------------------------------------\n")
        name = input("Enter employee Name (q to quit): ")
        if name == "q":
            break
        names.insert(counter, name)
        ssn = input("Enter employee SSN: ")
        phone = input("Enter employee Phone Number: ")
        email = input("Enter employee Email: ")
        salary = input("Enter employee Salary: ")
        address = input("Enter employee Address: ")
        date_of_birth = input("Enter employee Date of Birth: ")
        job_title = input("Enter employee Job Title: ")
        start_date = input("Enter employee Start Date: ")
        end_date = input("Enter employee End Date: ")
        employee_id = input("Enter employee ID: ")

        employees.append(
            [name, ssn, phone, email, salary, address, date_of_birth, job_title, start_date, end_date, employee_id])
        counter = counter + 1

def print_employee():
    for employee in employees:
        print("--------------" + employee[0] + "---------------")
        print("SSN: " + employee[1])
        print("Phone: " + employee[2])
        print("Email: " + employee[3])
        print("Salary: $" + employee[4])
        print("Address: " + employee[5])
        print("Date of Birth: " + employee[6])
        print("Job Title: " + employee[7])
        print("Start Date: " + employee[8])
        print("End Date: " + employee[9])


def main():
    while True:
        print('----------------------------------------------\n')
        print('      Welcome to the Employee Data System     \n')
        print('----------------------------------------------\n')
        print('[1] Add an Employee: \n')
        print('[2] View All Employees: \n')
        print('[3] Search Employees by Employee ID: \n')
        print('[4] Edit Employees information: \n')
        print('[5] Export Employees information: \n')
        print('[x] Exit: \n')
        user_option = input("Please select an option: ")
        if user_option == "x":
            break
        elif user_option == "1":
            add_employee()
        elif user_option == "2":
            print('\n' * 3)
            print_employee()
            print('\n' * 3)
        elif user_option in "34":
            found = search_id()
            if found == -1:
                print("Employee not found...")
            else:
                if user_option == "4":
                    edit_employee()
        elif user_option == "5":
            export_employees()
        else:
            print("Please select a valid option...")

    print("Goodbye")


if __name__ == "__main__":
    main()