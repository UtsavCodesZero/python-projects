# Calculator:

def menu():
    print("""\tWELCOME TO UTSAV'S CALCULATOR\n
You can do following calculations in this calculator:
a. Addition
b. Subtraction
c. Multiplication
d. Division\n""")
    
    calculation_selection = input("Which calculation would you like to do? (a, b, c, d): ").lower()
    if (calculation_selection != "a" and calculation_selection != "b" and calculation_selection != "c" and calculation_selection != "d"):
          print("\nInvalid calculation selection. Please select a or b or c or d.")
          menu()

    value_selection1 = float(input("\nEnter first value: "))
    value_selection2 = float(input("\nEnter second value: "))

    if (calculation_selection == "a"):
        print(f"\nResult:\n{value_selection1} + {value_selection2} = {value_selection1 + value_selection2}\n")

    elif (calculation_selection == "b"):
        print(f"\nResult:\n{value_selection1} - {value_selection2} = {value_selection1 - value_selection2}\n")

    elif (calculation_selection == "c"):
        print(f"\nResult:\n{value_selection1} x {value_selection2} = {value_selection1 * value_selection2}\n")

    elif (calculation_selection == "d"):
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
