import getfunctions
import csv

class User:
    def __init__(self, name = '', email = '', password = ''):
        self.name = name
        self.email = email
        self.password = password

    def write_user(self, file_name):
        with open(file_name, "a", newline='') as login_file:
            input_list = [self.name, self.email, self.password]
            writer = csv.writer(login_file)
            writer.writerow(input_list)
    
    @classmethod
    def check_email(cls, login_email, filename):
        flag = 0
        counter = 0
        with open(filename, "r") as file:        
            reader = csv.reader(file)
            for row in reader:
                if row[1] == login_email:
                    flag = flag + 1
                    break
                counter = counter + 1
        if flag == 1:
            return counter
        else:
            while True:
                print("No such email ID was found.")
                print("Please try again or press 1 to exit.")
                email = getfunctions.get_email()
                if email == "1":
                    return 0
                check = cls.check_email(email, filename)
                return check
    
    @classmethod
    def login(cls, email, filename):
        check = cls.check_email(email, filename) 
        if check != 0:
            with open(filename, "r") as file:
                reader = csv.reader(file)
                rows = list(reader)
                login_password = input("Password: ").strip()
                while True:
                    if login_password == rows[check][2]:
                        print("Login Successful!")
                        return True
                    else:
                        print("Entered password is incorrect.")
                        print("Please try again or Press 1 to exit.")
                        login_password = input("Password: ").strip()
                        if login_password == "1":
                            return False
        else:
            return False


def new_user():
    print("To create a new account please provide us with the following details.")
    name = input("Name: ").strip()
    while True:
        email = getfunctions.get_email() 
        found = login_check(email)
        if found == False:
            break
        else:
            print("You already have an account.")
            print("If you want to create a new one, please use a different email ID.") 
    password = getfunctions.get_password()
    return User(name, email, password)


def login_check(email):
    with open("UserLogin.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1] == email:
                return True
    return False     
    
