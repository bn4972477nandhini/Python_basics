def sum_of_number(num):
    sum=0
    for i in num:
        if i%2==0:
            sum+=i
    print(sum)


sum_of_number([1,2,3,4,5,6])
