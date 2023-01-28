from complaints import Complaint
from user import User
import csv
from prettytable import PrettyTable
import getfunctions

class Admin(User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)

    @classmethod
    def print_complaints(cls):
        with open("complaints.csv", "r") as file:
            reader = csv.reader(file)
            x = PrettyTable()
            x.field_names = next(reader)
            for row in reader:
                x.add_row(row)
        print(x)
        
    
    @classmethod
    def change_status(cls, complaintID):
        change_text = """What would you like the new status to be?
1: Done
2: Pending"""
        print(change_text)
        change_input = getfunctions.get_int(2)
        done = "Done"
        pending = "Pending"
        found = False
        with open("complaints.csv", "r") as file:
            reader = csv.reader(file)
            content = []
            for row in reader:
                if str(complaintID) == row[1]:
                    found = True
                    if change_input == 1:
                        print(row[6])
                        row[6] = done
                        print(row[6])
                    if change_input == 2:
                        row[6] = pending
                content.append(row)
        
        if found == False:
            print("No such complaint exists!")

        if found == True:
            with open("complaints.csv", "w+", newline='') as file:
                writer = csv.writer(file)
                writer.writerows(content)
            print("Status Changed Successfully!")


    @classmethod
    def sort(cls):
        ...

    def filter(cls):
        ...

    @classmethod
    def delete(cls, complaintID):
        found = False
        with open("complaints.csv", "r") as file:
            reader = csv.reader(file)
            content = []
            for row in reader:
                if str(complaintID) == row[1]:
                    found = True
                else:
                    content.append(row)
            
        if found == False:
            print("No such complaint exists!")
        
        if found == True:
            with open("complaints.csv", "w+", newline='') as file:
                writer = csv.writer(file)
                writer.writerows(content)
            print("Complaint Deleted Successfully!")
        

    @classmethod
    def add_type(self):
        ...



        
