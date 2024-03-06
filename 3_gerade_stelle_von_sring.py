#Exercise 3: Print characters from a string that are present at an even index number
#Write a program to accept a string from the user and display characters that are present at an even index number.
#For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.

user_input=input("please give a word ")
user_input_length=len(user_input)

print("Orginal String is ",user_input)
print("Printing only even index chars")


for i in range(0, user_input_length ,2):#start, where to stop, steps taken
    print(i ,user_input[i])
