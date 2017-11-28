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
    
if __name__=='__main__':
    super_function()