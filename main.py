# -------------------- Caeser Cipher Program -------------------- #
# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

# def greet():
#   print("Hello, world!")
#   print("This is the Caeser Cipher Program.")
#   print("How are you?")
#greet()

# def greet_person(name):
#    print(f"Hey, {name}. ")
#    print(f"How are you, {name}? ")

# greet_person("Bond")

# Functions with more than 1 input
# Changing order of arguments-
# def greet_with(name, location):
#   print(f"Hello, {name}.")
#   print(f"What is it like in {location}?")
# greet_with(location = "Manaus", name = "Alan")

# import math
# def paint_calc(height, width, cover):
#     #math.ceil to round the result up
#     cans = math.ceil((height * width) / coverage)
#     print(f"You'll need {cans} cans of paint.")
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)

def prime_checker(number):
    prime = True
    for i in range(2, number):
        if number % i == 0:
            prime = False
    if prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")
n = int(input("Check this number: "))
prime_checker(number=n)