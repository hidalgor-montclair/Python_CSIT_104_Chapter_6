# This function prints a summary of an order
# It takes 3 pieces of information: the order ID (oid), number of items, and price
def print_summary(oid, items, price):
    # Print the order ID
    print(f'Order {oid}:')
    # Print how many items are in the order
    print(f'    Items: {items}')
    # Print the total price of the order, formatted to 2 decimal places (like $13.99)
    print(f'    Total: ${price:.2f}')

# Now, let's assume we have the following information:
# The order ID is 42, the number of items is 4, and the total price is 13.99
oid = 42  # Order ID
items = 4  # Number of items
price = 13.99  # Total price

# Call the function to print the order summary with the given information
print_summary(oid, items, price)

# The program continues after printing the summary
