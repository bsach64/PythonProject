from user import User
from user import new_user
from complaints import Complaint
from complaints import new_complaint
import getfunctions
from admin import Admin

def main():
    introduction_text = """Welcome to Railway's Online Complaint Registration System!
Press Respective Key to Perform Operations
1: New User
2: User Login
3: Admin Login
4: New Admin
5: Exit"""
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
            user_input = 2

    if user_input == 2:
        email = input("Email: ")
        if User.login(email, "UserLogin.csv") == True:
            while True:
                action_text = """What would you like to do?
1: Register a New Complaint
2: Check Status of Complaint
3: Logout"""
                print(action_text)
                login_input = getfunctions.get_int(3)
                if login_input == 3:
                    print("Logout Successful")
                    break
                else:
                    user_login_actions(login_input, email)

    if user_input == 3:
        email = input("Email: ")
        if Admin.login(email, "AdminLogin.csv") == True:
            while True:
                admin_text = """What would you like to do?
1: Print  All Complaints
2: Print Sorted Complaints 
3: Filter Complaints Based on Type
4: Delete a Complaint
5: Add New Complaint Type
6: Update Status of Complaint
7: Logout"""
                print(admin_text)
                admin_input = getfunctions.get_int(7)
                admin_login_actions(admin_input, email)
                if admin_input == 7:
                    print("Logout Successful")
                    break
    
    if user_input == 4:
        new_admin_account = new_user()
        new_admin_account.write_user("AdminLogin.csv")
        
def user_login_actions(login_input, email):
    if login_input == 1:
        new = new_complaint(email)
        new.register_complaint()
    elif login_input == 2:
        user_complaints = Complaint.complaint_status(email)
        Complaint.print_status(user_complaints)
        
def admin_login_actions(admin_input, email):
    if admin_input == 1:
        Admin.print_complaints()
    if admin_input == 2:
        Admin.sort()
    if admin_input == 3:
        ct = Complaint.type()
        Admin.filter(ct)
    if admin_input == 4:
        complaintID = getfunctions.get_complaintID()
        Admin.delete(complaintID)
    if admin_input == 5:
        Admin.add_type()
    if admin_input == 6:
        complaintID = getfunctions.get_complaintID()
        Admin.change_status(complaintID)

if __name__ == "__main__":
    main()
