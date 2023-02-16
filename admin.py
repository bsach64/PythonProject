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
                        row[6] = done
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
        sorted_content = []
        with open("complaints.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[6] == "Pending":
                    sorted_content.append(row)
        
        with open("complaints.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[6] == "Done":
                    sorted_content.append(row)

        x = PrettyTable()
        x.field_names = ["Date","ComplaintID","Name","Email","Complaint","Complaint Type","Status"]
        for row in sorted_content:
            x.add_row(row)
        print(x)
        

    @classmethod
    def filter(cls, complaint_type):
        filtered_content = []
        with open("complaints.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[4] == complaint_type:
                    filtered_content.append(row)
        x = PrettyTable()
        x.field_names = ["Date","ComplaintID","Name","Email","Complaint","Complaint Type","Status"]
        for row in filtered_content:
            x.add_row(row)
        print(x)

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
    def add_type(cls):
        new_complaint_type = input("Enter New Complaint Type: ").strip()
        content = []
        with open("types.txt", "r", newline='') as file:
            for row in file:
                content.append(row)
        content.append(new_complaint_type + '\r\n')
        with open("types.txt", "w", newline='') as file:
            file.writelines(content)
        print("New Complaint Type Added")
        

        



        
