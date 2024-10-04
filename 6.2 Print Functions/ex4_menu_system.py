# This function prints the menu
def print_menu():
    print("Today's Menu:")  # Prints the title for the menu
    print('  1) Gumbo')  # Option 1 for Gumbo
    print('  2) Jambalaya')  # Option 2 for Jambalaya
    print('  3) Quit\n')  # Option 3 to quit the program

# We use this variable to control when the program should stop
quit_program = False

# This loop keeps showing the menu until the user chooses to quit
while not quit_program:
    print_menu()  # Show the menu
    # Ask the user for their choice, making sure to convert it to a number
    choice = int(input('Enter choice: '))
    
    # If the user chooses option 3, we stop the program
    if choice == 3:
        print('Goodbye')  # Say goodbye
        quit_program = True  # Set quit_program to True, which ends the loop
    else:
        # If they choose 1 or 2, we print their order
        print('Order: ', end='')  # Start the order message
        if choice == 1:
            print('Gumbo')  # Print Gumbo if they chose 1
        elif choice == 2:
            print('Jambalaya')  # Print Jambalaya if they chose 2
        # Print a blank line to separate each order
        print()
