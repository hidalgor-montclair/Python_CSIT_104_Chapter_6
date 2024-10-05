# This function prints a human head using text characters.
def print_human_head():
    print('  |||||  ')  # The hair
    print('   o  o')   # The eyes
    print('    >')     # The nose
    print('  ooooo')   # The mouth
    return  # Return means we're done with this function.

# This function prints a monkey head using text characters.
def print_monkey_head():
    print('   .--.   ')  # The top of the monkey's head
    print('  /.-.-.\\ ')  # The monkey's ears and face
    print(' ( ( o o ) )')  # The monkey's eyes
    print('  |/  "  \\| ')  # The monkey's mouth
    print('   \\ .-. /')  # The monkey's chin
    print('   /\'"""\'\\')  # The bottom of the monkey's face
    return  # Return means we're done with this function.

# This function prints the entire figure using the head from one of the above functions.
# It takes another function (either print_human_head or print_monkey_head) as an input.
def print_figure(face):
    face()  # This calls the function to print the head (either human or monkey)
    print('    |')  # The body
    print('  --|--')  # The arms
    print('   / \\')  # The legs
    print('  @   @')  # The feet
    return  # We're done with this function.

# Ask the user whether they want to draw a monkey or a human.
choice = int(input('Enter "1" to draw monkey, "2" for human: '))

# If the user chooses 1, we print the monkey figure.
if choice == 1:
    print_figure(print_monkey_head)

# If the user chooses 2, we print the human figure.
elif choice == 2:
    print_figure(print_human_head)
