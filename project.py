import useraccount
import complaints
import texts

def main():
    user_input = texts.program_intro()
    if user_input == 1:
        useraccount.new_user()    
    
    elif user_input == 2:
        login_email = input("Email: ")
        if useraccount.login(login_email) == True:
            login_input = texts.login_actions()
            if login_input == 1:
                complaints.register(login_email)
            elif login_input == 2:
                user_complaints = complaints.status(login_email)
                complaints.print_status(user_complaints)
    elif login_input == 3:
        print("Logout Successful")

main()
