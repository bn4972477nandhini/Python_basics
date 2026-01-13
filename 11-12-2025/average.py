def highest_average(first,second):
    first_sum=0
    second_sum=0
    for i in first:
        first_sum+=i
    for i in second:
        second_sum=0
    first_avg=first_sum/len(first)
    second_avg=second_sum/len(second)

    if first_avg>second_avg:
        print(first)
    elif first_svg<second_avg:
        print(second)
    else:
        print("Both are equal")


highest_average([4, 1, 2, 3, 5], [1, 0, 0, 1, 2, 1, 0, 2])
