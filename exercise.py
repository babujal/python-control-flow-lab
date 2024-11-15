# Exercise 0: Example
#
# This is a practice exercise to help you understand how to write code "inside" a provided Python function.
#
# We'll create a function that checks a condition and prints a specific greeting message based on that condition.
#
# Requirements:
# - The function is named `print_greeting`.
# - Inside the function, declare a variable `python_is_fun` and set it to `True`.
# - Use a conditional statement to check if `python_is_fun` is `True`.
# - If `python_is_fun` is `True`, print the message "Python is fun!"

def print_greeting():
    # Your code goes here. Remember to indent!
    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")

# Call the function
print_greeting()

# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.

def check_letter():
    # Your control flow logic goes here
    while True:
        letter = input('Enter a letter from a to z or type "quit" to quit:').lower()
        # print(f'The letter {letter} is a vowel.')

        if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
            print(f'The letter {letter} is a vowel.')
        elif letter == 'quit':
            print('Time to quit!')
            break
        else:
            print(f'The letter {letter} is not a vowel.')

# Call the function
# check_letter()

#//////////////////////////////////////////////////////////////////////////////////////////////

# Exercise 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting age.
# - Print a message indicating whether the user is eligible to vote based on the entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# - Use a conditional statement to check if the age meets the minimum voting age requirement.

def check_voting_eligibility():
    # Your control flow logic goes here
    try:
        user_age = input('Please enter your age:')
        age_to_int = int(user_age)
        if age_to_int < 18:
            print('You are not eligible to vote')
        else:
            print('You are eligible to vote')
    except ValueError as e:
        print(f"The following error occurred: {e}")
# Call the function
# check_voting_eligibility()
# Source for try except block: https://www.serveracademy.com/blog/python-try-except/

#///////////////////////////////////////////////////////////////////////////

# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.

def calculate_dog_years():
    # Your control flow logic goes here
    try:
        dog_age = input('Input a dogs age:')
        age_to_int = int(dog_age)
        age = 0
        if age_to_int < 3:
            age = age_to_int * 10
            print(f"The dog's age in dog years is: {age}")
        else:
            age = age_to_int * 7
            print(f"The dog's age in dog years is: {age}")
    except ValueError as e:
        print(f"The following error occurred: {e}")

# Call the function
calculate_dog_years()

