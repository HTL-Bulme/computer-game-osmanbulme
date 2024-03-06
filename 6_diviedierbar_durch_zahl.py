# Exercise 6: Display numbers divisible by 5 from a list
# Iterate the given list of numbers and print only those numbers which are divisible by 5

values=[10, 20, 33, 46, 55]

print("Given list is  [10, 20, 33, 46, 55]")
print("Divisible by 5")

for i in values:
    if i % 5 == 0:
        print(i)