#! python3

# Have the user enter in a sentence. 
# Check to see if the word "password" is located in the sentence

# Inputs:
# a sentence

# Outputs:
# "the sentence contains password"
# "the sentence does not contain password"

a=input("Enter a sentence:  ")
a=str(a)

if "password" in a:
    print("the sentence contains password")

else:
    print("the sentence does not contain password")
