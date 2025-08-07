def log_yield(func):
    def wrapper(*args, **kwargs):
        for value in func(*args, **kwargs):
            print(f"Yielded: {value}")
            yield value
    return wrapper

@log_yield
def count_up_to(n):
    for i in range(n):
        yield i

for num in count_up_to(3):
    pass

# Key Differences
"""
Feature     Decorators                                  Generators
Purpose	    Modify behavior of a function/class         Yield values one-by-one lazily
Keyword	    @decorator_name	                            yield
Used for	  Code reuse, logging, validation, etc.	      Memory-efficient iteration
Returns	    Modified function                           Generator object (iterator)
"""