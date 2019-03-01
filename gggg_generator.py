# hasta la vista baby
# The generator

'''
days = week()
next(days) # 'Monday'
next(days) # 'Tuesday'
next(days) # 'Wednesday'
next(days) # 'Thursday'
next(days) # 'Friday'
next(days) # 'Saturday'
next(days) # 'Sunday'
next(days) # StopIteration
'''
# day generator
def week():
    days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]
    
    for day in days:
        yield day


#days = week()
#print(next(days))
#print(next(days))


'''
gen = yes_or_no()
next(gen) # 'yes'
next(gen) # 'no'
next(gen) # 'yes'
next(gen) # 'no'
'''

# yes or not generator
def yes_or_no():
    answer = "yes"
    while True:
        yield answer
        if answer == "yes":
            answer = "no"
        else:
            answer = "yes"

gen = yes_or_no()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    