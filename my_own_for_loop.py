def my_for_loop(iterable, func):
    iterator = iter(iterable)
    while True:
        try:
            item = next(iterator)
            func(item)
        except StopIteration:
            print("End of Loop")
            break 
# my_for_loop("If I ruled the world, I'd free all my children.  Cause I love em, love em babyyyyy", print)