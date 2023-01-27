import re

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
