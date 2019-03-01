
# generator, save a ton memory
# generator are not faster than traditional iterable aka for loops
# fibonanci num
def fib_gen(max):
    x = 0
    y = 1
    count = 0
    while count < max:
        x, y = y, x + y
        yield x
        count+=1

fib = fib_gen(1000000000)

#for n in fib:
#    print(n)
    
'''
evens = get_multiples(2, 3)
next(evens) # 2
next(evens) # 4
next(evens) # 6
next(evens) # StopIteration

default_multiples = get_multiples()
list(default_multiples) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''

def get_multiples(num=1,count=10):

    for i in range(count+1):
        if i != 0:
            yield i*num

#evens = get_multiples(2,3)
#print(next(evens))


'''
sevens = get_unlimited_multiples(7)
[next(sevens) for i in range(15)] 
# [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105]

ones = get_unlimited_multiples()
[next(ones) for i in range(20)]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
'''

def get_unlimited_multiples(number=1):
    next_num = 1
    while True:
        yield next_num*number
        next_num+=1

one = get_unlimited_multiples(5)

print(next(one))
print(next(one))
print(next(one))
print(next(one))
print(next(one))
