import re

def get_int(length):
    while True:
        try:
            n = int(input("Input: "))
            if n in range(1, length + 1):
                return n
            else: 
                print("Number greater than ", length)
        except ValueError:
            print("Please Enter an Integer")

def get_email():
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    while True:
        email = input("Email: ").strip()
        if re.match(pattern, email, re.IGNORECASE):
            return email
        else:
            print("Please enter a valid Email")

def get_password():
    print("A password must contain atleast an lowercase, uppercase, number and a special character")
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]+$'
    while True:
        password = input("Password: ").strip()
        if re.match(pattern, password):
            return password
        else:
            print("Please enter a valid password")


def get_complaintID():
    while True:
        try:
            complaintID_string = input("Enter Complaint ID: ")
            complaintID_integer = int(complaintID_string)
            if len(complaintID_string) == 11:
                return complaintID_integer
            else:
                print("Please enter a valid Complaint ID")
        except ValueError:
            print("Please enter an integer")
            