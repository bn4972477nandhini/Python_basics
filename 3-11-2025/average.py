# # here last occurrence of quick is not considered
# ```

# ## Level 3

# Given an array count the number of elements higher than the average of the array?
# Assume all the elements inside the array are greater than zero. 
# Bonus: If validation for the input array is possible, you can include 

# ```python
# # test case 1
# Input: [10,20,30,40,50]
# Output: 2

# # here the average of all elements in 10+20+30+40+50 = 150 /5 = 30
# # you have 40 and 50 only which are greater than the average
# # so the count is 2

# # test case 2
# Input: [5,5,5,5]
# Output: 0

# # here the average of all elements is 5+5+5+5 = 20/4 = 5
# # you don’t have any element greater than 5 
# # so the count is 0


def average(array):
    count = 0
    total = 0
    avg = 0
    if len(array)==0:
        print("Invalid Input")
    else:
        count=0
        total=0
        for i in array:
            total+=i
            ave=total/len(array)
        for j in array:
            if j>ave:
                count+=1
        print(count)
       
average([10,20,30,40,50])
average([5,5,5,5])


