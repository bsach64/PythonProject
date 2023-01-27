import generalfunctions

def program_intro():
    introduction_text = """Welcome to Railway's Online Complaint Registration System!
Press Respective Key to Perform Operations
1: New User
2: User Login
3: Admin Login
4: Register Complaint through PNR
5: Exit"""
    print(introduction_text)
    user_input = generalfunctions.get_int(5)
    return user_input

def login_actions():
    action_text = """What would you like to do?
1: Register a New Complaint
2: Check Status of Complaint
3: Logout"""
    print(action_text)
    login_input = generalfunctions.get_int(3)
    return login_input