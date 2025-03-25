num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
choice = input("Enter choice: add-1, sub-2, mul-3, div-4: ")
if choice == "1":
    print("Addition is: ", num1 + num2)
elif choice == "2":
    print("Subtraction is: ", num1 - num2)
elif choice == "3":
    print("Multiplication is: ", num1 * num2)
elif choice == "4":
    print("Division is: ", num1 / num2)
else:
    print("Invalid choice...!!")