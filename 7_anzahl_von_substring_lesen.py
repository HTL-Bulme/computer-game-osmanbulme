# Exercise 7: Return the count of a given substring from a string
# Write a program to find how many times substring “Emma” appears in the given string.

def Convert(string): 
    li = list(string.split(" ")) 
    return li 

str_x = "Emma is good developer. Emma is a writer"

list_x = Convert(str_x)

count_list_x=list_x.count("Emma")

print("Emma appeared", count_list_x, "times")