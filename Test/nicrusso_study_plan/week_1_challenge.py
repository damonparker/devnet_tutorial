#find what divisors of a given number
# user_number = int(input("Please enter a number: "))

# list_range = list(range(1,user_number+1))

# divisor_list = []

# for number in list_range:
#     if user_number % number == 0:
#         divisor_list.append(number)

# print(divisor_list)

#Find out if a string is a palidrome or not

# user_string = input("Please enter a word:").lower()

# reverse_user_string = user_string[::-1]

# if user_string == reverse_user_string:
#     print("This word is a palindrome")
# else:
#     print("This word is not a palindrome")

bday = {
    "Albert Einstein": 1888,
    "Ben Franklin": 1776,
    "Ada Lovelace": 1976,
    "Damon Parker": 1976
}

print("Want to know someones birthday? Here are the ones available to know: ")

for key in bday.keys():
    print(key)

lookup = input("Who's birthday would you like to know? ")

if lookup in bday:
    print(bday[lookup])


