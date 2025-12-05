#Average sum
#1.Sum of all number average print 
def step_average(numbers):
    total = 0
    averages = []
    for i in range(len(numbers)):
        total += numbers[i]
        avg = total / (i+1)
        averages.append(avg)
    print(averages)
# call
step_average([10, 20, 30, 40, 50])




