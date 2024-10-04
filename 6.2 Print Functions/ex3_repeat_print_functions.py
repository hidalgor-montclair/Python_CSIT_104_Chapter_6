# Program B (Using a function to avoid repeating code)

print("Program B (Using a function to avoid repeating code)")

# This is the function that prints the same message,
# but it allows us to pass a different word each time.
def print_greatest(word):
    # Start of the sentence
    print('--The Greatest *', end='')  
    # Print the word that we give the function (like "Show" or "Song")
    print(word, end='')
    # End of the sentence
    print('* on Earth!--')

# Now we can call the function and give it the word "Show"
print_greatest('Show')

# Call the function again with the word "Song"
print_greatest('Song')
