print("---------------------Calculator---------------------")

while True:
    first_number = input("Enter the First Number (or press 'q' for quit) : ")
    if first_number.lower() == "q":
        print("Exiting the calculator.")
        break
    first_number = float(first_number)
    
    second_number = input("Enter the Second Number (or press 'q' for quit) : ")
    if second_number.lower() == "q":
        print("Exiting the calculator.")
        break
    second_number = float(second_number)

    print("1 for Addition")
    print("2 for Subtraction")
    print("3 for Multiplication")
    print("4 for Square root")
    print("5 for Division")
    print("6 for Floor Division")
    print("7 for Modulus")

    num = input("Enter The Equation Operator : (+,-,*,**,/,//,%) or press \'q' for quit : ")

    if num in ["1", "+"]:
        print("Addition of", first_number, "+", second_number, "=" , first_number+second_number)
    elif num in ["2", "-"]:
        print("Subtraction of", first_number, "-", second_number, "=" , first_number-second_number)
    elif num in ["3", "*"]:
        print("Multiplication", first_number, "X", second_number, "=" , first_number*second_number)
    elif num in ["4", "**"]:
        print("Square root of", first_number, "&", second_number, "=" , first_number**second_number)
    elif num in ["5", "/"]:
        if second_number !=0:
            print("Divition of", first_number, "/", second_number, "=" , first_number/second_number)
        else:
            print("Error: Division by zero is not allowed.")
    elif num in ["6", "//"]:
        if second_number !=0:
            print("Floor Divition of", first_number, "&", second_number, "=", first_number//second_number)
        else:
            print("Error: Division by zero is not allowed.")
    elif num in ["7", "%"]:
        print("Modulus of", first_number, "&", second_number, "=" , first_number%second_number)
    elif num in "q":
        print("Exiting the calculator.")
        break
    elif num in "Q":
        print("Exiting the calculator.")
        break
    else:
        print("Error : Equation is invalid.")

    print("____________________________________________________\n")
