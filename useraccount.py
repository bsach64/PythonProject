import csv 
import re

def new_user():
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
        while True:
            print("No such email ID was found.")
            print("Please try again or press 1 to exit.")
            email = get_email()
            if email == "1":
                return 0
            check = check_email(email)
            return check


def login(login_email):
    check = check_email(login_email) 
    if check != 0:
        with open("UserLogin.csv", "r") as file:
            reader = csv.reader(file)
            rows = list(reader)
            login_password = input("Password: ").strip()
            while True:
                if login_password == rows[check][2]:
                    print("Login Successful!")
                    return True
                else:
                    print("Entered password is incorrect.")
                    print("Please try again or Press 1 to exit.")
                    login_password = input("Password: ").strip()
                    if login_password == "1":
                        return False
    else:
        return False