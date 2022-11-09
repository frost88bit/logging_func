from functools import wraps

log = []

def main_log(func):
    '''Loggimg func'''
    @wraps(func)
    def with_loging(*arg, **kwargs):
        log.append(func.__name__+ ' func was called')
        with open('log.txt', 'w') as file:
            file.write(str(log))
        print(func.__name__+ ' func was called')
        return func(*arg, **kwargs)
    return with_loging

@main_log
def addition_func(a, b):
    """Sume of values"""
    return a + b

@main_log
def addition_func2(a, b):
    """Multiply of values"""
    return a * b


if __name__ == '__main__':
    result = addition_func(2, 3)
    result2 = addition_func2(2, 3)
    print(result, result2)
    print(log)
