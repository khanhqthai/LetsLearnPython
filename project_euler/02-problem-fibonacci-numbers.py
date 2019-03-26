num1=0
num2=1
sum = 0
for i in range(0,400000):
    current = num1 + num2
    num1 = num2
    num2 = current
    #print(current)
    if current%2 ==0:
        sum+=current
    if current > 4000000:
        break
    print(sum)