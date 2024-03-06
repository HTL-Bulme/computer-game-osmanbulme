#Exercise 1: Calculate the multiplication and sum of two numbers
#Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.
def multiplication_or_sum(num1, num2):
    multiplication = num1 * num2
    if multiplication<=1000:
        return multiplication
    else:
        return num1+num2

#einlesen vom user
in_number1 = int(input("First Number: ")) 
in_number2 = int(input("Second Number: "))

result = multiplication_or_sum(in_number1, in_number2) #geht hier auch mit int func
print("The result is ", result)
