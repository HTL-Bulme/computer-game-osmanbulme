# Exercise 5: Check if the first and last number of a list is the same
# Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.

def comparator(numbers):
    first=numbers[0]
    last=numbers[-1]

    if first==last:
        solution=True
    else:
        solution=False
    return solution

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

print("Given list: ", numbers_x)
print("result is:  ", comparator(numbers_x))

print("Given list: ", numbers_y)
print("result is:  ", comparator(numbers_y))