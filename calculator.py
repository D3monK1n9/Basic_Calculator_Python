print("--------------Calculator--------------")


while True:
    first_number = float(input("Enter The First Number (only number) : "))                      # First Number for the equation
    second_number = float(input("Enter The Second Number (only number) : "))                    # Second Number for the equation
    num = input("Enter The Equation Operator : (+,-,*,**,/,//,%) or press \'q' for quit : ")       # exponentiation operator symbol enter

    if (num=="+"):
        print("Addition of", first_number, "+", second_number, "=", first_number+second_number)             # for addition
    elif(num == "-"):
        print("Subtraction of", first_number, "-", second_number, "=", first_number-second_number)          # for Subtraction
    elif(num=="*"):
        print("Multiplication of", first_number, "X", second_number, "=", first_number*second_number)       # for Multiplication
    elif(num=="**"):
        print("Square root of", first_number, "&", second_number, "=", first_number**second_number)         # for Square root
    elif(num=="%"):
        print("Modulus of", first_number, "%", second_number, "=", first_number%second_number)              # for Modulus
    elif num == "/":
        if second_number != 0:                                                                              # Valid Check
            print("Division of", first_number, "/", second_number, "=", first_number / second_number)       # for Division of
        else:
            print("Error: Division by zero is not allowed.")                                                # Divition error handler
    elif num == "//":
        if second_number != 0:                                                                                      # Valid Check
            print("Floor Division of", first_number, "//", second_number, "=", first_number // second_number)       # for floor devition
        else:
            print("Error: Floor Division by zero is not allowed.")                                          # Divition error handler
    elif num == "q":
        print("Exiting The Calculator")
        break
    elif num == "Q":
        print("Exiting The Calculator")
        break
    else:
        print("Equatoin is Invalid")                                                                        # Code Error handler

    print("______________________________________\n")
