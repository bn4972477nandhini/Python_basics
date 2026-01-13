# #1 method 
def reverse_even_odd_index(num):
    temp=""
    for i in range(len(num)-1,-1,-1):
        if i%2!=0:
            temp+=num[i]
    print(temp)

reverse_even_odd_index("python")


#2 method
def reverse_even_odd_index(n):

    res=""
    temp=""
    for i in range(len(n)):
        if(i+1)%2==0:
            res=res+n[i]
        # print(temp)
    for i in res:
        temp=i+temp
    print(temp)

reverse_even_odd_index("python")