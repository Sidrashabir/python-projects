#Word Counter program
def count_words(text):
    #Split the text into words and count them
    words=text.split()
    return len(words)

#Main program
print('Welcome to the Word Counter!')
print('This program will count the number of words in your text.')

#Get input from user
user_input = input('Please enter a sentence or paragraph:')

# Check if the input is empty
if user_input.strip() == "":
    print('Oops! You did not enter any text. Please try again.')
else:
    word_count=count_words(user_input)

    #Display the result
    print(f'Your text contains {word_count}words.')
print('Thank you for using the Word Counter!')    
