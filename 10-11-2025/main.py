#1st sum
#  Create and Print a List
# Write a Python program to create a list of 5 fruits and print them one by one using a loop.

# ```python
# Input: ["apple", "banana", "cherry", "grapes", "mango"]  
# Output:  
# apple  
# banana  
# cherry  
# grapes  
# mango

def print_fruits(num):
    for i in num:
        print(i)
print_fruits(["apple","banana","cherry","grapes","mango"])

#2nd Sum
# * Sum of Numbers in a List
# Write a program to find the sum of all numbers in a list entered by the user.

# ```python
# Input: [10, 20, 30, 40, 50]  
# Output: 150 # 10+20+30+40+50

def sum_of_number(num):
    sum = 0
    for i in num:
        sum = sum + i
    print(sum)
sum_of_number([10,20,30,40,50])


#3ed sum
# *  Reverse a List (Without using reverse() method)
# Write a program to reverse a given list using loops 
# (Hint: Create a New List called `final` and print the `final` list at the last)

# python
# Input: [10, 20, 30, 40]  
# Output: [40, 30, 20, 10]

def print_reverse(num):
    for i in range(len(num)-1,-1,-1):
        print(num[i])
print_reverse([10,20,30,40])


#4th sum
# * Even Numbers from a List
# Write a program that prints only the even numbers from a given list.
# (Hint: Create a condition inside the loop to check through each number in the list 
# if number is even, print the number one by one)

# ```python
# Input: [3, 6, 9, 12, 15, 18]  
# Output: [6, 12, 18]

def print_even_number(n):
    for i in n:
        if i%2==0:
            print(i)
print_even_number([3,6,9,12,15,18])



#5th sum
# * Add All Positive Numbers Only
# Write a program to calculate the sum of all positive numbers in a list.
# (Create a variable called `total`
# Check each number in the list, if number above zero means, add to `total`)

# ```python
# Input: [12, -7, 5, -3, 9, 0]  
# Output: 26
# ```

def sum_positive_numbers(numbers):
    total = 0
    for i in numbers:
        if i > 0:
            total = total + i
    print(total)

sum_positive_numbers([12,-7,5,-3,9,0])

#6th sum
# - Square Each Number in a List
#   Write a Python program to create a new list that contains the squares of all numbers from a given list.

# ```python
# Input: [2, 3, 4, 5]
# Output: [4, 9, 16, 25]

def square_print(num):
    for i in num:
        print(i**2)
square_print([2,3,4,5])


#7th sum
# - Count Elements Greater Than 50
#   Given a list of numbers, count how many numbers are greater than 50.

# ```python
# Input: [20, 60, 75, 45, 90, 35]
# Output: 3
# # 60, 75, 90

def print_count_number(num):
    count = 0
    for i in num:
        if i > 50:
            count = count+1
    print(count)
print_count_number([20,60,75,45,90,35])


#8.first and last value only add 

def add_value(n):
    count=0
    for i in range(0,len(n),len(n)-1):
        count+=n[i]
    print(count)
add_value([2,4,6,8,7,6])


