'''
@show_args
def do_nothing(*args, **kwargs):
    pass

do_nothing(1, 2, 3,a="hi",b="bye")

# Should print (on two lines):
# Here are the args: (1, 2, 3)
# Here are the kwargs: {"a": "hi", "b": "bye"}
'''

from functools import wraps


def show_args(fn):
    #wraps keep meta data
    @wraps(fn)
    def wrapper(*args,**kwargs):
        '''Wrapper function for show_args'''
        return fn(*args,**kwargs)

    return wrapper

@show_args
def do_nothing(*args,**kwargs):
    print((*args))
    print(dict(**kwargs))
do_nothing(1,2,3, a="hi",b="bye")