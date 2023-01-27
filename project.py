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
                print("Please Provide us with the following details to register a complaint")
                output_list = []
                output_list.append(str(date.today()))
                complaintID = complaints.generate_complaintID()
                output_list.append(complaintID)
                name = input("Name: ")
                output_list.append(name)
                output_list.append(login_email)
                ct = complaints.complaint_type()
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
