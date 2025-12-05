# 1.Write a Python program that splits a sentence into words and finds the longest word in it.
# Sample Input:

# Data science evolves every year
# Sample Output:
# Longest word: science

def longest_word(sen):
    word=sen.split()
    longest=""
    for i in word:
        if len(i)>len(longest):
            longest=i
    print(longest)
longest_word("Data science evolves every year")

# 2. Write a Python program to find the word that has maximum number of vowels from the given sentence
# Sample Input:
# Learning Python is interesting
# Sample Output:
# interesting

def maximum_letter(s):
    let=s.split()
    max_word=""
    for j in let:
        if len(j)>len(max_word):
            max_word=j
    print(max_word)
maximum_letter(" Learning Python is interesting")


# 3. Write a python program to find the words that has more than 4 characters
# Sample Input:
# This is a python program
# Sample Output:
# python
# program

def more_then_4letter_word(m):
    dom=m.split()
    words=""
    for x in dom:
        if len(x)<len(words):
            words=x
    print(words)
more_then_4letter_word("This is a python program")