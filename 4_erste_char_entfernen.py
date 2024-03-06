# Exercise 4: Remove first n characters from a string
# Write a program to remove characters from a string starting from zero up to n and return a new string.

user_input_word=input("please give a word: ")
user_input_word_length=len(user_input_word)

user_input_cut=input("please give how many to cut: ")
user_input_cut_length=len(user_input_cut)

print("Orginal String is: ", user_input_word)

if int(user_input_cut_length)<int(user_input_word_length):
    print("Result:        ", user_input_word[int(user_input_cut):user_input_word_length])
else:
    print("ERROR 404: you stupid")

### Alternative ###
""""
def remove_chars(word, n):
    print('Original string:', word)
    x = word[n:]
    return x

print("Removing characters from a string")
print(remove_chars("pynative", 4))
print(remove_chars("pynative", 2))
"""