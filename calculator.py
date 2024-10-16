while(True):
    choice = int(input("Enter Choice:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exit\n"))
    if(choice == 5):
        break
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))
    if (choice == 1):
        print("Addition of the numbers is " + (num1 + num2))
    elif (choice == 2):
        print("Subtraction of the numbers is " + (num1 - num2))
    elif (choice == 3):
        print("Multiplication of the numbers is " + (num1 * num2))
    else:
        print("Division of the numbers is " + (num1 / num2))