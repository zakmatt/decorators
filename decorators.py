import functools

def my_decorator(func):
    @functools.wraps(func)
    def function_which_runs_func():
        print("Before func.")
        func()
        print("After func")
    return function_which_runs_func

@my_decorator
def super_function():
    print("I like pancakes")
    

def decorator_with_args(number):
    def my_decorator(func):
        @functools.wraps(func)
        def function_which_runs_func(*args, **kwargs):
            print("Before func.")
            a = func(*args, **kwargs) + 5
            print("After func.")
            return a
        return function_which_runs_func
    return my_decorator
    
@decorator_with_args(123)
def super_second_function(x, y):
    print("I like pancakes too!" )
    print(x+y)
    return 5
    
    
    
if __name__=='__main__':
    super_function()
    print(super_second_function(3, 23))