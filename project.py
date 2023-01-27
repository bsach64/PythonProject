import complaints
import user
import getfunctions

def main():
    introduction_text = """Welcome to Railway's Online Complaint Registration System!
Press Respective Key to Perform Operations
1: New User
2: User Login
3: Admin Login
4: Register Complaint through PNR
5: Exit"""
    print(introduction_text)
    user_input = getfunctions.get_int(5)
    if user_input == 1:
        new_account =  user.new_user()
        new_account.write_user()
        after_new_account = """ A new account has been created. What would you like to do next?
1: Login and Register a Complaint
2: Exit
        """    
        print(after_new_account)
        new_input = getfunctions.get_int(2)
        if new_input == 1:
            to_login()

    elif user_input == 2:
        to_login()

def to_login():
    email = input("Email: ")
    if user.login(email) == True:
        action_text = """What would you like to do?
1: Register a New Complaint
2: Check Status of Complaint
3: Logout"""
        print(action_text)
        login_input = getfunctions.get_int(3)
        if login_input == 1:
            complaints.register(email)
        elif login_input == 2:
            user_complaints = complaints.status(email)
            complaints.print_status(user_complaints)
        elif login_input == 3:
            print("Logout Successful")

main()
