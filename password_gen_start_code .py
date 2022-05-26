"""
    Password Generator Project
    input:  password length
            Number of Digits
            Number of Symbols
    
    output: password (as string)
"""
####################################################################################################
######################## DO NOT CHANGE THIS SECTION OF THE CODE ####################################
# importing the relevant modules
import string
import random

# List of all lowercase and uppercase characters in Python
all_alphabets = list(string.ascii_letters)
# print(f"These Are the Alphabets: {all_alphabets}" )


all_digits = list(string.digits)
# print(f"See all these Digits: {all_digits}")

all_symbols = list(string.punctuation)
# print(f"Check out these symbols: {all_symbols}")


# Ask user for how many letters they would like in their password and cast to integer and store as no_of_letters
no_of_letters = int(input("Hey How Many Letters Would You Like In Your Password?  "))
# print(f"What Data Type Is This?  {type(no_of_letters)} letters")



# Ask user for how many symbols they would like in their password and cast to integer and store as no_of_symbols
no_of_symbols = int(input("Hey How Many Symbols Would You Like To Have In Your Password?  "))

# Ask user for how many digits they would like in their password and cast to integer and store as no_of_digits
no_of_digits = int(input("Hey How Many digits Would You Like To Have In Your Password?  "))

# Set Accumulator for Password Characters List
pass_char_list = []


# Get the random letter for the password
# Randomly Select the characters
for number in range(no_of_letters):
#       select a random characer from list of alphabets and append to the password characters list 
    # print(number)  
    random_letter = random.choice(all_alphabets)
    # print(random_letter)
    pass_char_list.append(random_letter)

print(pass_char_list)    
  



# Get the Random Symbols for the password symbols

# Set Accumulator for the Number of Symbols List

pass_symbol_list = []
# Randomly Select the characters
for number in range(no_of_symbols):
#       select a random symbol from list of symbols and append to the password symbols list 
    random_symbol = random.choice(all_symbols)
    pass_symbol_list.append(random_symbol)

print(pass_symbol_list)   




# Get the Random Digits for the password

# Set Accumulator for the Number of Digits List
pass_digits_list = []
# Randomly Select the characters
for number in range(no_of_digits):
#       select a random digit from list of digits and append to the password digits list 
    random_digit = random.choice(all_digits)
    pass_digits_list.append(random_digit)

print(pass_digits_list)   


# Add the lists to get the final_password_list and shuffle the fin_pass_list

fin_pass_list = pass_char_list + pass_symbol_list + pass_digits_list

#shuffle the fin_pass_list
random.shuffle(fin_pass_list)
print(fin_pass_list)

# Now that we have our password in a list lets change that to a string then print it

# accumulator for string_password


# for character in final_password_list:
#       append the character to the string_password

# Print the string password
