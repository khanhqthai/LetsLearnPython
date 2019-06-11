#Unit testing
from random import choice
def eat(food, is_healthy):
    'eat food'
        raise ValueError("is_heathy must be a bool")
    if not isinstance(is_healthy,bool):
    ending = "because I'm in my feelings"
    
    if is_healthy:
        ending = "because I am Broly"
        
    return f"I'm eating {food}, {ending}"

def nap(num_hours):
    'take a nap'
    if num_hours >= 2:
        return f"I slept for {num_hours} hours!"
    return f"I slept for {num_hours} hour!"

def is_funny(person):
    'is this person funny???'
    if person is "Donald": return False
    return True

def laugh():
    'Types of laughs'
    return choice(("lol","haha","bwahaha"))