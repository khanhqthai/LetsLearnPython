from functools import wraps


#example 1:
#we can use decorator to ensur that kwargs will not be passed in
def ensure_no_kwargs(fn):

    #standard wrapper boiler plate
    @wraps(fn)
    def wrapper(*args,**kwargs):
        #check if there is key word arguments
        if kwargs:
            raise ValueError("No kwargs allowed")
        return fn(*args,**kwargs)
    return wrapper
@ensure_no_kwargs
def greet(name):
    print(f"Hi there {name}")

#no should not work, should get error raise "no kwargs allowed"
#no key word arguments allowed!
#we can use this same idea to ensure only certain types can be use
#greet(a="Joe")


#example 2
'''
@double_return 
def add(x, y):
    return x + y

add(1, 2) # [3, 3]

@double_return
def greet(name):
    return "Hi, I'm " + name

greet("Colt") # ["Hi, I'm Colt", "Hi, I'm Colt"]
'''

# return functions two times
def double_return(fn):
    @wraps(fn)
    def wrapper(*args,**kwargs):
        val = fn(*args,**kwargs)
        return [val,val]
    return wrapper

@double_return
def add(x,y):
    return x + y

@double_return
def greet(name):
    return "Hi, I'm" + name
