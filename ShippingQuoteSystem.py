"""
You have been hired to build a booking quote system for transporting packages.
You will write this system in Python, as a terminal application.
You will use simple terminal IO (input and print) as a user interface for now.
Another developer in the future will convert this to a server application that is front-ended with a browser (you don’t need to worry about how this happens as it’s not part of your work, but it can and should influence how you build your system).


The application you are building will capture the following information:
Name of the customer.
Package description.
Are the contents dangerous? [Y/N]
Weight (kgs).
Volume (cubic meters).
Required delivery date (month/date/year).
International destination? [Y/N]
The application will then attempt to find the best way to route the package (air / ground / ocean).


The rules it will use are as follows:

Packages can only be shipped if they weigh less than 10Kg or are smaller than 5x5x5 meters (125 cubic meters).
If the package contains dangerous goods it cannot be routed via air.
‘Urgent’ means a package has to be delivered in less than 3 business days.
If the package is urgent it will be routed via air, if possible.
If the package is heavy or large (towards the maximum end of the boundaries set in 1 above), and is not urgent, it can be routed via truck (or even ocean if it is for an international destination).
Air shipments cost $10 per kilogram or $20 per cubic meter, whichever is the highest.
Truck shipments cost a flat rate of $25, or $45 if urgent.
Ocean shipments costs a flat rate of $30.
Your system will apply these rules to the booking and will calculate alternative shipping options (or one, or possibly none, depending on how the above rules affect the booking).
The shipping options must be printed in a clearly understood format, and should be appended to a booking_quotes.csv file. There will be one row in the file for each quote.
This application is to be developed using an object oriented approach.
It will require extensive automated tests to ensure the above rules are correctly applied by the system.


Here is what you need to do:

Use automated testing to validate the system behaves as intended.
Develop the data capture functionality, paying careful attention to any implied data needs.
Make sure the data is validated, so data entry errors can be prevented as much as possible.
Build a menu so the system is easy to use.
Ensure each booking has a unique id.
Make use of formatting techniques to ensure that information reported to the screen is well laid out and easy to understand.
Be sure each booking quote is stored in the csv file.


Submission:

Your submission should include the following:
All Python (.py) files, including tests, that you developed.
The csv file with some quote data in it.
Any other files required to run your code.
Tips

Be creative! Use this as an opportunity to reflect on everything you have learned so far and apply it to application development.
Consider making your user interface fully separated from the rest of the project.
This will make it easier to implement a new web-based interface later on without having to modify the underlying implementation."""

#Assignment shipping calculator
#Author: Name


from datetime import datetime
from datetime import date
from csv import csv

class Package:

    def __init__(self, booking):
        self.booking = booking

    def shipping_info(self):
        self.package_volume()
        self.package_weight()
        self.contents_dangerous()
        self.international()
        self.delivery_date()
        self.contents_dangerous()
        self.shipment_type()
        self.calculate()

    def add_to_csv(self):
        with open(DIR + "database.csv", "w") as f:
            for key in self.booking.keys():
                f.write(self, )


    def package_volume(self):
        while True:
            if self.booking["volume"] <= 125:
                print("This package's volume is an appropriate size to ship.")
                break
            else:
                print("You're package is too large")
                self.booking["volume"] = int(input("Write a package weight (in cubic meters): "))

    def package_weight(self):
        while True:
            if self.booking["weight"] <= 10:
                print("This package is an appropriate weight  to ship.")
                break
            else:
                print("You're package is too heavy")
                self.booking["weight"] = int(input("Write a package weight (in kgs): "))

    def contents_dangerous(self):
        while True:
            if self.booking["contents"] not in ("yn"):
               self.booking["contents"] = input("Are the contents dangerous? (Y/N)").lower()
            else:
               if self.booking["contents"] == "y":
                   print("Your contents cannot ship via air.")
                   break
               else:
                  print("You're content's aren't dangerous and are eligible to ship.")
                  break

    def international(self):
        while True:
            if self.booking["international"] in ("yn"):
                if self.booking["international"] == "y": #This can be removed later
                    print("International Shipping") #This can be removed later
                else: #This can be removed later
                    print("Domestic shipping") #This can be removed later
                break
            else:
                print("Is your package dangerous? Y/N: ")
                self.booking["international"] = input("Are you shipping internationally? (Y/N)").lower()

    def delivery_date(self):
        today = date.today()
        today = today.strftime("%d/%m/%Y")
        start = datetime.strptime(today, "%d/%m/%Y")
        end = datetime.strptime(self.booking["delivery_date"], "%d/%m/%Y")
        # get the difference between wo dates as timedelta object
        diff = (end.date() - start.date())
        self.booking["delivery_date"] = diff.days
        print(f"You want your product to ship in", self.booking["delivery_date"], "days")

    def shipment_type(self):
        if self.booking["delivery_date"] <= 3 and self.booking["weight"] <= 10 and self.booking["volume"] <= 125 and self.booking["contents"] == "n":
            self.booking["shipment_type"] = "air"
            print("Your product can ship through air")
        elif self.booking["contents"] == "y".lower():
            self.booking["shipment_type"] != "air"
        elif self.booking["weight"] <= 9 and self.booking["volume"] <= 124 and self.booking["delivery_date"] >= 3 and self.booking["international"] == "n".lower():
            self.booking["shipment_type"] = "truck"
            print(self.booking["shipment_type"])
        elif self.booking["weight"] <= 9 and self.booking["volume"] <= 124 and self.booking["international"] == "y".lower():
            self.booking["shipment_type"] = "ocean"
            print(self.booking["shipment_type"])
        return self.booking["shipment_type"]

    def calculate(self):
        while True:
          print(self.booking["shipment_type"])
          if self.booking["shipment_type"] == "air":
              cost_per_kg = 10 * self.booking["weight"]
              cost_per_volume = 20 * self.booking["volume"]
              if cost_per_kg > cost_per_volume:
                print(f"Your", self.booking["shipment_type"], "will cost you",{cost_per_kg})
                break
              else:
                print(f"Your", self.booking["shipment_type"], "will cost you",{cost_per_volume})
                break
          elif self.booking["shipment_type"] == "truck":
            if self.booking["delivery_date"] <= 3:
              cost_per_shipment = 45
              print(f"Your shipment will cost {cost_per_shipment}")
              self.booking["shipping_cost"] = cost_per_shipment
              break
            else:
              cost_per_shipment = 25
              print(f"Your shipment will cost {cost_per_shipment}")
              self.booking["shipping_cost"] = cost_per_shipment
              break
          else:
            cost_per_shipment = 30
            print(f"Your shipment will cost {cost_per_shipment}")
            self.booking["shipping_cost"] = cost_per_shipment
            break


def user_input():
    booking = dict()
    booking["name_of_customer"] = input("Name of customer: ")
    booking["volume"] = int(input("Write a package volume (in cubic meters): "))
    booking["weight"] = int(input("Write a package weight (in kgs): "))
    booking["description"] = input("Write a package description: ")
    booking["delivery_date"] = input("Write a desired delivery date (DD/MM/YYYY): ")
    booking["international"] = input("Is this shipping internationally? (Y/N): ").lower()
    booking["contents"] = input("Are the contents dangerous? (Y/N): ").lower()
    booking["shipment_type"] = "truck"
    booking["shipping_cost"] = 0
    return booking

def main():
    while True:
        print('----------------------------------------------\n')
        print('      Welcome to the Shipping estimator     \n')
        print('----------------------------------------------\n')
        print('[1] Add a package: \n')
        print('[2] List packages: \n')
        print('[3] Remove package: \n')
        print('[4] Search packages by type: \n')
        print('[5] Leave: \n')
        user_option = input("Please select an option: ")
        if user_option == "1":
            booking = user_input()
            print(booking)
            packaging = Package(booking)
            packaging.shipping_info()
        elif user_option == "2":
            print('\n' * 3)
            packaging.shipping_info()
            print('\n' * 3)
        elif user_option == "3":
            found = search_id()
            if found == -1:
                print("Employee not found...")
            elif user_option == "4":
                search_package()
            elif user_option == "5":
                print("Goodbye . . .")
                break
            else:
                print("Please select a valid option...")

main()

""" booking = user_input()
    print(booking)
    packaging = Package(booking)
    packaging.shipping_info()"""

