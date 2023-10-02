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

# def prime_checker(number):
#     prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             prime = False
#     if prime:
#         print("It's a prime number.")
#     else:
#         print("It's not a prime number.")
# n = int(input("Check this number: "))
# prime_checker(number=n)

alphabet = [' ','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caeser(start_text, shift_amount, cipher_direction):
  final_text = ""
  if cipher_direction == "decode":
      shift_amount *= -1
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      final_text += alphabet[new_position]
    else:
      final_text += char
  
  print(f"The {cipher_direction}d text is: {final_text}")

from art import logo
print(logo)

want_to_continue = True
while want_to_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  shift = shift % 26
  caeser(start_text = text, shift_amount = shift, cipher_direction = direction)

  result = input("'Yes' if you want to continue, 'No' if you want to stop: ").lower()
  if result == "no":
    want_to_continue = False
    print("Goodbye, hope you enjoyed.")

# def encrypt(plain_text, shift_amount):
#   cipher_text = ''
#   for letter in plain_text:
#     position = alphabet.index(letter)
#     new_position = position + shift_amount
#     new_letter = alphabet[new_position]
#     cipher_text += new_letter
#   print(f"The encoded text is: {cipher_text}")

# def decrypt(cipher_text, shift_amount):
#   plain_text = ''
#   for letter in cipher_text:
#     position = alphabet.index(letter)
#     new_position = position - shift_amount
#     plain_text += alphabet[new_position]
#   print(f"The decoded text is {plain_text}")


# if direction == "encode":
#   encrypt(plain_text = text, shift_amount = shift)

# elif direction == "decode":
#   decrypt(cipher_text=text, shift_amount=shift)

