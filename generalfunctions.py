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