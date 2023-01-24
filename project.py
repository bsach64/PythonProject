import csv
import re
from datetime import date

def main():
    user_input = program_intro()
    if user_input == 1:
        new_user()    
    
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
1: Register a New Complaint
2: Check Status of Complaint
3: Logout"""
                    print(action_text)
                    login_input = get_int(3)
                    if login_input == 1:
                        print("Please Provide us with the following details to register a complaint")
                        output_list = []
                        output_list.append(str(date.today()))
                        complaintID = generate_complaintID()
                        output_list.append(complaintID)
                        name = input("Name: ")
                        output_list.append(name)
                        output_list.append(login_email)
                        ct = complaint_type()
                        output_list.append(ct)
                        print("Please provide a description of your complaint")
                        complaint = input("Complaint: ")
                        output_list.append(complaint)
                        output_list.append("Pending")
                        with open("complaints.csv", "a", newline = '') as file:
                            writer = csv.writer(file)
                            writer.writerow(output_list)
                        print()
                        print("Your complaint has been registered successfully")
                        print("Your complaintID is: ", complaintID)
                        print("Thank You for using our service")
                    elif login_input == 2:
                        content = complaints_as_list()
                        complaint_counter = 0
                        for element in content:
                            if element[3] == login_email:
                                complaint_counter += 1
                                print("ComplaintID : " ,element[1], ",", "Status :", element[6])
                        if complaint_counter == 0:
                            print("No Complaints Found!")
                    elif login_input == 3:
                        print("Logout Successful")
                
                else:
                    print("Password is incorrect.")
        else:
            print("No such email ID found")

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
    today = str(date.today())
    today_number = today.replace('-','')
    today_number = today_number + "000"
    content = complaints_as_list()
    if content[-1][1] != "ComplaintID":
        if content[-1][0] == today:
            prev_id = int(content[-1][1])
            x = prev_id - int(today_number)
            x = x + 1
            answer = int(today_number)
            answer = answer + x
            return answer
        else:
            answer = int(today_number)
            return answer
    else:
        answer = int(today_number)
        return answer

def complaints_as_list():
    with open("complaints.csv", "r") as file:
        reader = csv.reader(file)
        content = []
        for row in reader:
            content.append(row)
    return content

def complaint_type():
    complaint_types = ["Other", "Delays and Cancellations", "Overcrowding", "Poor Maintainance", "Ticketing Issues", "Safety Issues"]
    print("Please Choose one of the following categories of complaints")
    for i in range(0, len(complaint_types)):
        print((i + 1), ":", complaint_types[i])
    
    number = get_int(len(complaint_types))
    ct = complaint_types[number - 1]
    return ct

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

def program_intro():
    introduction_text = """Welcome to Railway's Online Complaint Registration System!
Press Respective Key to Perform Operations
1: New User
2: User Login
3: Admin Login
4: Register Complaint through PNR
5: Exit"""
    print(introduction_text)
    user_input = get_int(5)
    return user_input


main()
