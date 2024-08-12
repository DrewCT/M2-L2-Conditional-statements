#Task 1: Identify the Greatest Write a Python program that asks the user to enter three numbers. Your code should then identify and print out the largest number among the three

number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))
number_3 = int(input("Enter third number: "))

largest_number = max(number_1, number_2, number_3)
print(f"the largest number among the three is: {largest_number}")

#Task 2: Identify the Smallest Improve upon your code from Task 1 to also determine the smallest number among the three and print it out.

number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))
number_3 = int(input("Enter third number: "))

largest_number = max(number_1, number_2, number_3)
smallest_number = min(number_1, number_2, number_3)
print(f"the smallest number is {smallest_number} and the largest number is {largest_number}")

