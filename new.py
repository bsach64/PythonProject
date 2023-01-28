import csv
from datetime import date
import getfunctions

class Complaint:
    def __init__(self, date, complaintID, name, email, complaint, ctype, status):
        self.date = date
        self.complaintID = complaintID
        self.name = name 
        self.email = email
        self.complaint = complaint
        self.ctype = ctype
        self.status = status 
    
    def register_complaint(self):
        output_list = [self.date, self.complaintID, self.name, self.email, self.complaint, self.ctype, self.status]
        with open("complaints.csv", "a", newline = '') as file:
            writer = csv.writer(file)
            writer.writerow(output_list)
        print()
        print("Your complaint has been registered successfully")
        print("Your complaintID is: ", self.complaintID)
        print("Thank You for using our service")
    
    def last_complaint(self):
        with open("complaints.csv", "r") as file:
            reader = csv.reader(file)
            content = []
            for row in reader:
                content.append(row)
        return content[-1]
    
    def generate_complaintID():
        today = str(date.today())
        today_number = today.replace('-','')
        today_number = today_number + "000"
        complaint = Complaint.last_complaint()
        if complaint[1] != "ComplaintID":
            if complaint[0] == today:
                prev_id = int(complaint[1])
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

def new_complaint(login_email):
    print("Please Provide us with the following details to register a complaint")
    complaintID = Complaint.generate_complaintID()
    name = input("Name: ")
    complaint_type = type()
    print("Please provide a description of your complaint")
    complaint = input("Complaint: ")
    return Complaint(str(date.today()), complaintID, name, login_email, complaint_type, complaint, "Pending")





def type():
    complaint_types = ["Other", "Delays and Cancellations", "Overcrowding", "Poor Maintainance", "Ticketing Issues", "Safety Issues"]
    print("Please Choose one of the following categories of complaints")
    for i in range(0, len(complaint_types)):
        print((i + 1), ":", complaint_types[i])
    number = getfunctions.get_int(len(complaint_types))
    ct = complaint_types[number - 1]
    return ct
