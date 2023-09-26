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
# Changing order of arguments
def greet_with(name, location):
  print(f"Hello, {name}.")
  print(f"What is it like in {location}?")
greet_with(location = "Manaus", name = "Alan")