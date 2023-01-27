from datetime import date
import csv
import generalfunctions

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

def complaint_type():
    complaint_types = ["Other", "Delays and Cancellations", "Overcrowding", "Poor Maintainance", "Ticketing Issues", "Safety Issues"]
    print("Please Choose one of the following categories of complaints")
    for i in range(0, len(complaint_types)):
        print((i + 1), ":", complaint_types[i])
    
    number = generalfunctions.get_int(len(complaint_types))
    ct = complaint_types[number - 1]
    return ct

def complaints_as_list():
    with open("complaints.csv", "r") as file:
        reader = csv.reader(file)
        content = []
        for row in reader:
            content.append(row)
    return content

def register_complaint(login_email):
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