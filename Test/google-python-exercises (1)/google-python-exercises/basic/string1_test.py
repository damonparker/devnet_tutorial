#google python exerise string 1.py # 1

# def donuts():
#     count = input('How many donuts did you get? ')
#     count = int(count)
#     if count < 10:
#         print('Number of donuts: ' + str(count))
#     else:
#         print('Number of donuts: So Many')
#     return

# donuts()


# B. both_ends
# Given a string s, return a string made of the first 2
# and the last 2 chars of the original string,
# so 'spring' yields 'spng'. However, if the string length
# is less than 2, return instead the empty string.
# def both_ends():

#     s = input('Please provide a word to manipulate\n')
#     first_two = s[0:2]
#     last_two = s[-2:]

#     if len(s) < 2:
#         print('The word is not long enough')

#     else:
#         print(first_two + last_two)

# both_ends()

# C. fix_start
# Given a string s, return a string
# where all occurences of its first char have
# been changed to '*', except do not change
# the first char itself.
# e.g. 'babble' yields 'ba**le'
# Assume that the string is length 1 or more.
# Hint: s.replace(stra, strb) returns a version of string s
# where all instances of stra have been replaced by strb.
# def fix_start():
#     s = input('Please provide a sentence to manipulate\n')
#     new_string = s[0] + s[1:].replace(s[0],"*")
#     print(new_string)

# fix_start()

# D. MixUp
# Given strings a and b, return a single string with a and b separated
# by a space '<a> <b>', except swap the first 2 chars of each string.
# e.g.
#   'mix', pod' -> 'pox mid'
#   'dog', 'dinner' -> 'dig donner'
# Assume a and b are length 2 or more.
def mix_up():
    word_1 = input("Enter 1 word\n")
    word_2 = input("Enter another word\n")
    new_string = word_1.replace(word_1[:2], word_2[:2]) + word_2.replace(word_2[:2], word_1[:2])
    print(new_string)



mix_up()