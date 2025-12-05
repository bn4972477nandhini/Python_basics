#1st sum
# Given a list of integers, check if a number is present in the list or not. Print “found” else, print “not found”
def check_number(a,b):
    if b in a:
        print("found")
    else:
        print("not found")
check_number([8,1,0,19,11,28,5,3],5)

#2nd sum
# Check if the sum of all numbers in a list is even or not

def check_sum_even(num):
    total = sum(num)
    print(total)
    if total % 2 == 0:
        print("Sum is even")
    else:
        print("Sum is odd")
check_sum_even([8, 1, 0, 19, 11, 28, 3, 5])

#3ed sum
# Given two numbers a and b and a list of numbers num_list. Print all the elements in num_list between a and b.
# For eg, num_list = [8, 1, 0, 19, 11, 28, 3, 5],  a = 10 and b = 20

def print_between(num, a, b):
    for i in num:
        if a <= i <= b:
            print(i)
print_between(num = [8, 1, 0, 19, 11, 28, 3, 5],a = 10,b = 20 )


