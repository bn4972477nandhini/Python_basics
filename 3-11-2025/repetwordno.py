
# Write a Python program to find and print the longest word in a given sentence.

# ```python
# Sample Input: "Python makes programming enjoyable"
# Sample Output: "programming"

def remove_repet_word(s):
    result = ""
    for i in s:
        if i not in result:    
            result += i
    print(result)


remove_repet_word("programming")  