# 1st sum
# - Identify the First Negative NumberProblem Statement: Traverse a list of integers.
#  Stop iterating and print the first negative number encountered.
#   If no negative numbers are found after checking the entire list, print "All are Positive".

# python
# Input: [5, 12, 3, -8, 15, -2]
# Output: -8    
# explain question and answer

def negative_number(num):
    for i in num:
        if i<0:
            print(i)
        else:
            print("All are positive")
negative_number([5, 12, 3, -8, 15, -2])   #sir


# 2en sum
# - Given a list of any data type (e.g., numbers or strings),
#   determine and print the total number of elements in the list.
#   (Hint: use a loop with a temporary variable `count`)

# ```python
# Input = ['apple', 'banana', 'cherry', 'date']
# Output = 4

def words_count(words):
    count=0
    for i in words:
        count+=1
    print(count)
words_count(['apple','orange','banana','cherry'])

# 3ed sum
# - Remove Specific Value Occurrences (Without remove() or pop())
#   Problem Statement: Given a list and a target value, create a new list that contains all
#  elements from the original list except for any occurrence of the target value.

# ```python
# Sample Input: data = [1, 5, 2, 5, 3, 5], target = 5
# Expected Output: [1, 2, 3]

def remove_target(num, target):
    new_list = []
    for i in num:
        if i != target:
            new_list.append(i)
    print(new_list)

remove_target([1, 5, 2, 5, 3, 5], 5)    #sir

#4th sum

# - Given a list of four or more elements, determine if every element in the list is exactly the same value.
#   Print "Uniform" or "Mixed".

# ```python
# # test case 1
# Input = ['A','A','A','A','B']
# Output = "Mixed"

# # test case 2
# Input = [1,1,1,1]
def check_uniform(lst):
    first = lst[0]
    for i in lst:       
        if i != first:   
            print("Mixed")
        else:
            print("Uniform")
        
    
check_uniform(['A','A','A','A','B'])
check_uniform([1,1,1,1])


#5th sum
# - Given a list of positive integers,
#   create a new list containing only those numbers that are two digits long
#   (i.e., numbers between `10` and `99`, inclusive).

# ```python
# Input = [5, 12, 100, 45, 9, 201]
# Output = [12,45]
# ```

def two_digit_numbers(numbers):
    new_list = []
    for n in numbers:
        if n >= 10 and n <= 99:
            new_list.append(n)
    print (new_list)
two_digit_numbers([5, 12, 100, 45, 9, 201])


#6th sum
# - Total Number of Students Passed
#   Given marks of students in a list, count how many students scored greater than or equal to 40.

# python
# Input: marks = [25, 65, 78, 39, 56, 41]
# Output: 4
def students_marks(mark):
    count=0
    for i in mark:
        if i >= 40:
            count+=1
    print(count)
       
students_marks( [25, 65, 78, 39, 56, 41])

# 7th sum
# - Replace Negative Numbers

# Given a list of integers, replace all negative numbers with 0.

# ```python
# Input: [-2, 5, -9, 8, 0, -4]
# Output: [0, 5, 0, 8, 0, 0]
# ```

def replace_number(nums):
    empty_list = []
    for n in nums:
        if n < 0:
            empty_list.append(0)
        else:
            empty_list.append(n)
    print(empty_list)

replace_number([-2, 5, -9, 8, 0, -4])


# 8th sum
# - Product of All Numbers
#   Find the product of all elements in a list without using built-in functions.

# ```python
# Input: [1, 2, 3, 4]
# Output: 24
# ```

def product_of_list(nums):
    product = 1
    for n in nums:
        product = product * n
    print(product)

product_of_list([1, 2, 3, 4])


# 9th sum
# - Increase Every Element by 10
# Write a program to increase every element in the list by 10 and print the new list.

# ```python
# Input: [2, 4, 6, 8]  
# Output: [12, 14, 16, 18]
# ```

def increase_by_ten(nums):
    result = []
    for n in nums:
        result.append(n + 10)
    print( result)
increase_by_ten([2, 4, 6, 8])



# 10th sum- Check if Two Words Have the Same Length
#   Write a program to check if two words have the same number of characters without using `len()`.
#   Print `Yes`, if both lengths matches
#   Print `No`, if not matching

# ```python
# Input: word1 = "tree", word2 = "bush"
# Output: Yes

def same_number_count(word1, word2):
    count1 = 0
    count2 = 0

    for J in word1:
        count1 += 1

    for J in word2:
        count2 += 1

    if count1 == count2:
        print( "Yes")
    else:
        print ("No")


same_number_count("tree", "bush")
same_number_count("cat", "lion")

# 11th sum
# - Vowel Extractor  
#   Write a program to extract only the vowels from a given word and store them in a list.  
#   Print the list at the end.

# ```python
# Input: word = "education"
# Output: ['e', 'u', 'a', 'i', 'o'] 

def print_vowel_only(word):
    empty_list=[]
    vowel="a,i,o,u,e"
    for i in word:
        if i in vowel:
            empty_list.append(i)
    print(empty_list)
print_vowel_only("education")



