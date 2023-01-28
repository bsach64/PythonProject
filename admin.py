from complaints import Complaint
from user import User
import csv
from prettytable import PrettyTable

class Admin(User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)

    @classmethod
    def print_complaints(cls):
        content = []
        with open("complaints.csv", "r") as file:
            reader = csv.reader(file)
            x = PrettyTable()
            x.field_names = next(reader)
            for row in reader:
                x.add_row(row)
        print(x)
        
    
    @classmethod
    def change_status(cls, complaintID):
        ...

    @classmethod
    def sort(cls):
        ...

    @classmethod
    def delete(cls):
        ...

    @classmethod
    def add_type(self):
        ...


def get_complaintID():
    while True:
        try:
            complaintID_string = input("Enter Complaint ID: ")
            complaintID_integer = int(complaintID_string)
            if len(ComplaintID_string) == 11:
                return complaintID_integer
            else:
                print("Please enter a valid Complaint ID")
        except ValueError:
            print("Please enter an integer")

        
