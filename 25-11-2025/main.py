
# - Given a list of words, print only the ones that start with an uppercase letter.
#   Use a single loop to check their first character.

# ```python
# test case 1
# Input: ["Apple", "ball", "Cat", "dog"]
# Output: Apple Cat
#Explanation: They start with capital letters.

def students_score(maths,science):
    res=[]
    for i in range(0,len(maths)):
        if maths[i]>80 and science[i]>80:
            res.append(i)
    print(res)
students_score([92, 45, 81],[88, 90, 70])


# - Given two equal-length arrays maths and science,
#   return the indexes of students who scored > 80 in both subjects.

# ```python
# #test case 1
# Input:
# maths [92, 45, 81], science [88, 90, 70]

# Output: [0]

def uppercase(num):
    result=""
    for i in range(0,len(num)):
        if (num[i][0]) in "QWERTYUIOPASDFGHJKLZXCVBNM":
            result+=" "+num[i]
    print(result)
uppercase(["Apple", "ball", "Cat", "dog"])

# - Filter numbers satisfying 3 conditions
#   Problem:
#   Print numbers that:

# 1. are 4 digits
# 2. end with an even digit

# ```python
# #Test Case:
# Input: [2481, 3572, 602, 7890, 4214]
# Expected Output: [3572,7890 ,4214]

def fillter_the_number(n):
    temp=[]
    for i in range(0,len(n)):
        if n[i]>1000 and n[i]<9999:
            if n[i]%2==0:
                temp.append(n[i])
    print(temp)
fillter_the_number([2481, 3572, 602, 7890, 4214])

# - From a string, collect all the lowercase letters in the same order.
#   Use a single loop to scan the string.

# ```python
# # test case 1
# Input: "PyTHonProGRam"
# Output: "yonroam"

def lowercase(num):
    result=""
    for i in range(0,len(num)):
        if (num[i][0]) in "mnbvcxzlkjhgfdsapoiuytrewq":
            result+=""+num[i]
    print(result)
lowercase("PyTHonProGRam")


#- You are given a list containing integers, floats and strings
# Create a new list containing only the float values using one loop.
# ```python
# Example:
# Input: [10, 3.5, "hello", 8.2, 6]
# Output: [3.5, 8.2]

def print_float(num):
    res=[]
    for i in num:
        if type(i) == float:
            res.append(i)
    print(res)
print_float([10, 3.5, "hello", 8.2, 6])
    

