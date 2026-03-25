# Calculator:

def menu():
    print("""\tWELCOME TO UTSAV'S CALCULATOR\n
You can do following calculations in this calculator:
+  Addition
-  Subtraction
*  Multiplication
/  Division\n""")
    
    calculation_selection = input("Which calculation would you like to do? (+, -, *, /): ")
    if (calculation_selection != "+" and calculation_selection != "-" and calculation_selection != "*" and calculation_selection != "/"):
          print("\nInvalid calculation selection. Please select +, -, *, or /.")
          menu()
          return

    value_selection1 = float(input("\nEnter first value: "))
    value_selection2 = float(input("\nEnter second value: "))

    if (calculation_selection == "+"):
        print(f"\nResult:\n{value_selection1} + {value_selection2} = {value_selection1 + value_selection2}\n")

    elif (calculation_selection == "-"):
        print(f"\nResult:\n{value_selection1} - {value_selection2} = {value_selection1 - value_selection2}\n")

    elif (calculation_selection == "*"):
        print(f"\nResult:\n{value_selection1} * {value_selection2} = {value_selection1 * value_selection2}\n")

    elif (calculation_selection == "/"):
        if (value_selection2 == 0):
             print("Error: Cannot divide by zero!\n")
             ask_continue()
             return
        print(f"\nResult:\n{value_selection1} / {value_selection2} = {value_selection1 / value_selection2}\n")

    ask_continue()
    return

def ask_continue():
    thank_you = input("Would you like to do another calculation? (y/n): ").lower()
    if (thank_you == "y"):
        menu()
    elif (thank_you == "n"):
        print("\nThank you for using Utsav's calculator.\nWe hope you have a great day ahead.")

menu()
