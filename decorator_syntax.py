from functools import wraps
#example 1
def be_polite(fn):
    def wrapper():
        print("What a pleasure to meet you!")
        fn()
        print("Have a great day!")
    return wrapper

@be_polite
def greet():
    print("My name is Matt")


#example 2, handling functions with multiple arguments
#**args, and kwargs**
def shout(fn):
    def wrapper(*args,**kwargs):
        return fn(*args,**kwargs).upper()
    return wrapper

@shout
def greet(name):
    return f"Hi, Iam {name}"
@shout
def order(main,side):
    return f"Hi, I'd like {main}, with a side of {side}, please"

#print(greet("khanh"))
#print(order("burgers", "fries))


#example 3
def log_function_data(fn):
   #wraps from functools, prints the corrects documents, function names meta dataf
    @wraps(fn)
    def wrapper(*args,**kwargs):
        """I AM A WRAPPER FUNCTIONS"""
        print(f"you are about to call {fn.__name__}")
        print(f"Here's the documentation: {fn.__doc__}"
        return fn(*args,**kwargs)
    return wrapper
@log_function_data
def add(x,y):
    """add two number together"""
    return x+y;
#print(add(2,9))
print(add.__doc__)
