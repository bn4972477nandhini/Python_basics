#1sum 
#Even and odd number index  print 
def odd_and_even(s):
    odd = ""
    even = ""
    for i in range(0,len(s),+1):
        if i%2==0:
            even = even + s[i]
        else:
            odd = odd + s[i]
    print(even,odd)
odd_and_even("python")

#2sum
# input[1,2,3,4]-> output->[24,12,8,6]
def print_multiple_number(num):
    product = 1
    result = []
    for i in range(len(num)):
        product = product * num[i]
    for j in num:
        result.append(product //j)
    print(result)

print_multiple_number([1, 2, 3, 4])

#3ed sum
# - Count Occurrences of a Given Number Write a program to count how many times a specific number appears in a list.
# python
# Input: numbers = [3, 5, 3, 8, 3, 9], target = 3
# Output: 3

def count_numbers_print(number,target):
    count=0
    for j in number:
        if j == target:
            count+=1
    print(count)
count_numbers_print([3,5,6,3,5,5,3,0,9],3)
