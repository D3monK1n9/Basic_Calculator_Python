print("---------------------Calculator---------------------")

while True:
    # Input first number (with quit option)
    first_number = input("Enter the First Number (or 'q' to quit): ")
    if first_number.lower() == "q":
        print("Exiting the calculator.")
        break
    first_number = float(first_number)

    # Input second number (with quit option)
    second_number = input("Enter the Second Number (or 'q' to quit): ")
    if second_number.lower() == "q":
        print("Exiting the calculator.")
        break
    second_number = float(second_number)

    # Show menu
    print("1 for Addition (+)")
    print("2 for Subtraction (-)")
    print("3 for Multiplication (*)")
    print("4 for Power (**)")
    print("5 for Division (/)")
    print("6 for Floor Division (//)")
    print("7 for Modulus (%)")

    num = input("Enter The Operator (1-7 or symbol) or press 'q' to quit: ")
    if num.lower() == "q":
        print("Exiting the calculator.")
        break

    if num in ["1", "+"]:
        print("Addition =", first_number + second_number)
    elif num in ["2", "-"]:
        print("Subtraction =", first_number - second_number)
    elif num in ["3", "*"]:
        print("Multiplication =", first_number * second_number)
    elif num in ["4", "**"]:
        print("Power =", first_number ** second_number)
    elif num in ["5", "/"]:
        if second_number != 0:
            print("Division =", first_number / second_number)
        else:
            print("Error: Division by zero is not allowed.")
    elif num in ["6", "//"]:
        if second_number != 0:
            print("Floor Division =", first_number // second_number)
        else:
            print("Error: Division by zero is not allowed.")
    elif num in ["7", "%"]:
        if second_number != 0:
            print("Modulus =", first_number % second_number)
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Error: Invalid operator.")

    print("____________________________________________________\n")
