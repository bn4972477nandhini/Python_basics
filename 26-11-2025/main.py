#  1.Write a function that merges two lists by taking elements alternately.

# ```python
# Input: x= [1, 2, 3] y= ['a', 'b', 'c']
# Output: [1, 'a', 2, 'b', 3, 'c']
# ```

# merges two list 
def merges_two_list(x,y):
   result=[]
   for i in range(len(x)):
       result.append(x[i])
       result.append(y[i])
   print(result)
    
merges_two_list([1,2,3],['a','b','c'])

#2. print even number sum:
def even_count_number(num):
    sum=0
    for i in range(0,len(num),+1):
        if i%2==0:
            sum+=num[i]
    print(sum)
            
even_count_number([4,7,12,9,6])


# 3. Write a Program that Keep Words That Start and End With the Same Letter

# ```python
# Case-insensitive matching.
# Example:
#  Input: ["level", "Apple", "mana", "cool"]
#  Output: ["level"]

def same_start_end(words):
    result = []
    for w in range(len(words)):
        word = words[w]
        if word[0]==word[-1]:
            result.append(word)
    print(result)        
            
            
        
same_start_end(["level", "Apple", "mana", "cool"])


# - Given a list of names, print only the ones that contain “a” or “A”.

# ```python
# Input: ["Meera", "John", "Kavi", "Sona"]
# Output: Meera Kavi Sona
# Explanation: These names include the letter 'a'
# ```


def  print_word(n):
    result=[]
    for i in n:
        if "a" in i or "A" in i:
            result.append(i)
    print(result)
print_word(["Meera", "John", "Kavi", "Sona"])


# 1. Filter numbers whose reverse is greater than the number.
# Given a list of integers, print only those numbers whose reversed value is greater than the original number.
#  Input: [12, 41, 77, 30]
#  Output: 12 
#  (12→21>12, 30→03>30)

def reverse(a):
    for i in a:
        b = str(i)
        rev = ""
        for j in b:
            rev = j + rev
        math = int(rev)
        if math > i:
            print(i)
reverse([12,41,77,30])
            


# 2. Print words where the first and last letter are the same.
# Given a list of words, print only those whose first and last letters match.
#  Input: ["level", "apple", "noon", "code"]
#  Output: level noon

def first_and_last_word(num):
    result=[]
    for i in range(len(num)):
        word = num[i]
        if word[0]==word[-1]:
            result.append(word)
    print(result)
first_and_last_word(["level", "apple", "noon", "code"])


# 3. Filter strings that contain exactly 2 vowels.
# Given a list of strings, print only words having exactly 2 vowels.
#  Input: ["team", "sky", "apple", "road"]
#  Output: team road



def find_max(m):
    for i in x:
        if i in "QWERTYUIOPASDFGHJKLZXCVBNM":
            print(i)
find_max("HeLLoWoRlD")











