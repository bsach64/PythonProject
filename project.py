import complaints
from user import User
from user import new_user
from complaints import Complaint
from complaints import new_complaint
import getfunctions

def main():
    introduction_text = """Welcome to Railway's Online Complaint Registration System!
Press Respective Key to Perform Operations
1: New User
2: User Login
3: Admin Login
4: Register Complaint through PNR
5: New Admin
6: Exit"""
    print(introduction_text)
    user_input = getfunctions.get_int(5)
    if user_input == 1:
        new_account = new_user()
        new_account.write_user("UserLogin.csv")
        after_new_account = """ A new account has been created. What would you like to do next?
1: Login and Register a Complaint
2: Exit"""    
        print(after_new_account)
        new_input = getfunctions.get_int(2)
        if new_input == 1:
            user_login()

    elif user_input == 2:
        user_login()
    
    elif user_input == 5:
        new_admin_account = new_user()
        new_admin_account.write_user("AdminLogin.csv")

def user_login():
    email = input("Email: ")
    if User.login(email) == True:
        action_text = """What would you like to do?
1: Register a New Complaint
2: Check Status of Complaint
3: Logout"""
        print(action_text)
        login_input = getfunctions.get_int(3)
        if login_input == 1:
            new = new_complaint(email)
            new.register_complaint()
        elif login_input == 2:
            user_complaints = Complaint.complaint_status(email)
            Complaint.print_status(user_complaints)
        elif login_input == 3:
            print("Logout Successful")

main()
