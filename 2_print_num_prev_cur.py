# Exercise 2: Print the sum of the current number and the previous number
#Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.

sum_of_all=0

for i in range(0,10):
    prev_num=i-1
    sum_of_all=i+prev_num
    print("Current Number ", max(0, i), " Previous Number ", max(0, prev_num), " Sum: ", max(0, sum_of_all)) #darf nicht negativ sein