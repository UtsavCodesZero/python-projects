# PROJECT 2: CALCULATOR

user_input_sign = input('''What do you want to do:
- Addition (+)
- Subtraction (-)
- Multiplication (*)
- Division (/)

Enter your choice: ''')

valid_operators = ["+", "-", "*", "/"]

if user_input_sign not in valid_operators:
    print("Invalid operator. Please choose from +, -, *, or /.")

else:
    user_input1 = float(input("Enter number 1: "))
    user_input2 = float(input("Enter number 2: "))

    if user_input_sign == "+":
        print(f"{user_input1} + {user_input2} = {user_input1 + user_input2}")

    elif user_input_sign == "-":
        print(f"{user_input1} - {user_input2} = {user_input1 - user_input2}")

    elif user_input_sign == "*":
        print(f"{user_input1} x {user_input2} = {user_input1 * user_input2}")

    elif user_input_sign == "/":
        if user_input2 == 0:
            print("Error: Division by 0 is not allowed.")
        else:
            print(f"{user_input1} / {user_input2} = {user_input1 / user_input2}")
