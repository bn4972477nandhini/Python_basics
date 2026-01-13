# Write a Python program to find and print the longest word in a given sentence.

# ```python
# Sample Input: "Python makes programming enjoyable"
# Sample Output: "programming"
def longest_word(sentence):
    word = sentence.split()      
    longest = ""               

    for j in word:
        if len(j) > len(longest): 
            longest = j

    print(longest)


longest_word("Python makes programming enjoyable")




