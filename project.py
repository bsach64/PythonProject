import csv
from datetime import date
import useraccount
import complaints
import generalfunctions
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
                complaints.register_complaint(login_email)
            elif login_input == 2:
                content = complaints.complaints_as_list()
                complaint_counter = 0
                for element in content:
                    if element[3] == login_email:
                        complaint_counter += 1
                        print("ComplaintID : " ,element[1], ",", "Status :", element[6])
                    if complaint_counter == 0:
                        print("No Complaints Found!")
            elif login_input == 3:
                print("Logout Successful")



main()
