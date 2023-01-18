import csv
import re
from datetime import date

def main():
    introduction_text = """Welcome to Railway's Online Complaint Registration System!
Press Respective Key to Perform Operations
1: New User
2: User Login
3: Admin Login
4: Register Complaint through PNR
5: Exit"""
    print(introduction_text)
    user_input = get_int(5)

    if user_input == 1:
        print("To create a new account please provide us with the following details.")
        with open("UserLogin.csv", "a", newline = '') as login_file:
            input_list = []
            name = input("Name: ").strip()
            input_list.append(name)
            email = get_email()
            input_list.append(email)
            password = get_password()
            input_list.append(password)
            writer = csv.writer(login_file)
            writer.writerow(input_list)
        print("A New User has been created. To register a complaint, please login in.")
    
    elif user_input == 2:
        login_email = input("Email: ")
        counter = check_email(login_email) 
        if counter != 0:
            with open("UserLogin.csv", "r") as file:
                reader = csv.reader(file)
                rows = list(reader)
                login_password = input("Password: ").strip()
                if login_password == rows[counter][2]:
                    print("Login Successful!")
                    action_text = """What would you like to do?
1: Registering a New Complaint
2: Checking Status of Complaint
3: Logout"""
                    login_input = get_int(3)
                    if login_input == 1:
                        print("Please Provide us with the following details to register a complaint")
                        output_list = []
                        output_list.append(date.today())
                        # Write code for ComplaintID
                        output_list.append(1)
                        name = input("Name: ")
                        output_list.append(name)
                        # Write code for complaint type
                        output_list.append("Other")
                        print("Please provide a description of your complaint")
                        complaint = input("Complaint: ")
                        output_list.append(complaint)
                        output_list.append("Pending")

                    elif login_input == 3:
                        print("Logout Successful")

def get_int(length):
    while True:
        try:
            n = int(input("Input: "))
            if n in range(1, length + 1):
                return n
            else: 
                print("Number greater than 5")
        except ValueError:
            print("Please Enter a Valid Input")

def get_email():
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    while True:
        email = input("Email: ").strip()
        if re.match(pattern, email, re.IGNORECASE):
            return email
        else:
            print("Please enter a valid Email")

def get_password():
    print("Please create a new password.")
    print("A password must contain atleast an lowercase, uppercase, number and a special character")
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]+$'
    while True:
        password = input("Password: ").strip()
        if re.match(pattern, password):
            return password
        else:
            print("Please enter a valid password")


def check_email(login_email):
    flag = 0
    counter = 0
    with open("UserLogin.csv", "r") as file:        
        reader = csv.reader(file)
        for row in reader:
            if row[1] == login_email:
                flag = flag + 1
                break
            counter = counter + 1
    if flag == 1:
        return counter
    else:
        return 0

def generate_complaintID():
    return 0
    
main()
