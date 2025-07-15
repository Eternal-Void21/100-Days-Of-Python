letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#----------------- My Answer --------------------
#Easy level

import random
letter_seq = random.choices(letters, k=nr_letters)
print1 = "".join(map(str, letter_seq))

symbol_sequence = random.choices(symbols, k=nr_symbols)
print2 = "".join(map(str, symbol_sequence))

number_seq = random.choices(numbers, k= nr_numbers)
print3 = "".join(map(str, number_seq))

print(print1,print2,print3, sep="")

#Hard level
nr_total = nr_letters + nr_symbols + nr_numbers
final_list = letter_seq + symbol_sequence + number_seq
random.shuffle(final_list)
print4 = "".join(map(str, final_list))
print(print4, sep="")

#----------------- Official Answer --------------------
#Easy level

password = ""
for char in range (0, nr_letters):
    password += random.choice(letters)

for char in range(0, nr_symbols):
    password += random.choice(symbols)

for char in range(0, nr_numbers):
    password += random.choice(numbers)
print(password)

#Hard level

password_list = []
for char in range (0, nr_letters):
    password_list.append(random.choice(letters))

for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))
random.shuffle(password_list)
Final_pass = "".join(map(str, password_list))

print(Final_pass)
