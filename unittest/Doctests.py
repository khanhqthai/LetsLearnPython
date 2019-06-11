#Using doctest to test functions
#Very cool feature, but syntax must be precise and there are quirks
#Not recommened to use for testing

def add(x,y):
    """
    >>> add(1,4)
    5
    >>> add(10,100)
    110
    """
    return x + y
    
def double(values):
    """ doubles the values in a list
    
    >>> double([1,2,3])
    [2, 4, 6]
    
    >>> double([])
    []
 
    >>> double(['a','b','c'])
    ['aa', 'bb', 'cc']
    
    """
    return [i+i for i in values]

def say_hi():
    #Note: doctest compares strings with single quotes: 'hi' will pass test
    """ return  "Hi"
    >>> say_hi()
    "hi"       
    """
    return "hi"
    
    
def true_that():
    #note: if there is a white space after True test will fail, doctest is finicky
    """ returns True, 
    >>> true_that()
    True
    """
    return True
    
def make_dict(keys):
    #note order of dictionary items matter
    """
    >>> make_dict(['a','b'])
    {'b': True, 'a': True}
    """
    return {key:True for key in keys}