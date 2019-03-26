def enforce(*type):
    def wrapper(fn):
        def inner(*args,**kwargs):
            print(*args)
            for i,k in kwargs.items():
                print(k)
            return "hello"
        return inner
    return wrapper

@enforce(str, int)
def war_chant(text: str,num: int):
    return print([text for x in range(num)])

war_chant(hell="lasflskj")