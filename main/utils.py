from datetime import datetime

def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        print(start)
        result = func(*args, **kwargs)
        print(datetime.now() - start)
        return result
    return wrapper