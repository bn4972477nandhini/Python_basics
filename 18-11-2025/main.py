# Find the smallest word in a sentence.
# Input: "Python is super powerful"
# Output: is  
def print_small_word(num):
    word = num.split()
    print(word)
    small = word[0]

    for i in word:
        if len(i)<len(small):
            small=i
    print(small)
print_small_word("python is super powerful")


# 2. A list is strictly increasing if every next element is greater than the previous one.
# Example:
# [1,3,5,9] → True
# [2,2,5] → False (because 2 is NOT less than 2)
# [10,5,6] → False (because 5 < 10)
def strictly_increasing(num):
    for i in range(len(num)-1):
        if num[i+1]<=num[i]:
            return False
    return True

print(strictly_increasing([1,3,5,9]))
print(strictly_increasing([2,2,5]))
print(strictly_increasing([10,5,6]))


# 3. Replace characters at odd indexes with 
# Example: "hello" → "h*l*o" (edited) 
def print_reverse(num):
    result=""
    for i in range(len(num)):
        if i%2!=0:
            result = result + "*"
        else:
            result = result + num[i]
    print(result)
print_reverse("hello")
