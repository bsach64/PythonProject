import complaints
import texts
from user import User
import user

def main():
    user_input = texts.program_intro()
    if user_input == 1:
        new_account =  user.new_user()
        new_account.write_user()    
    
    elif user_input == 2:
        email = input("Email: ")
        if user.login(email) == True:
            login_input = texts.login_actions()
            if login_input == 1:
                complaints.register(email)
            elif login_input == 2:
                user_complaints = complaints.status(email)
                complaints.print_status(user_complaints)
    elif login_input == 3:
        print("Logout Successful")

main()
