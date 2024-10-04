# Program A (Repeating code without a function)

print("Program A (Repeating code without a function)")
# We want to print a message like: --The Greatest Show on Earth!--
# But we're writing the same code twice for different words.

# First print statement for the word "Show"
# We print the start of the sentence
print('--The Greatest *', end='')  # The "end=''" keeps everything on one line
# Now we print the word, in this case, "Show"
print('Show', end='')  
# And finally we finish with the rest of the sentence
print('* on Earth!--')

# Second print statement for the word "Song"
# Again, we repeat all the lines, but now with the word "Song"
print('--The Greatest *', end='')  # The start of the sentence
print('Song', end='')  # Print the word "Song" here
print('* on Earth!--')  # The end of the sentence
