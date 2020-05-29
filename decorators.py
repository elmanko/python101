#Decorators

# # will use a 1st class function to print a message
# # the inner_function() with the message will be returned
# # to the outter_function, to be called

# # def outer_function(msg):
# #     def inner_function():
# #         print(msg)
# #     return inner_function

# # my_func = outer_function()
# # my_func() # a closure, remembers 'message' even though inner_function has finished

# # hi_func = outer_function('Hi')
# # bye_func = outer_function('Bye')

# # hi_func()
# # bye_func()


# def decorator_function(original_function):
#     def wrapper_function(*args, **kwargs):
#         print('wrapper_function executed this before: {}'.format(original_function.__name__))
#         return original_function(*args, **kwargs)
#     return wrapper_function

# class decorator_class(object):
#     def __init__(self, original_function):
#         self.original_function = original_function

#     def __call__(self, *args, **kwargs):
#         print('__call__ method executed this before: {}'.format(self.original_function.__name__))
#         return self.original_function(*args, **kwargs)
from functools import wraps

def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info('Ran with args: {}, and kwargs: {}'.format(args,kwargs))
        return orig_func(*args, **kwargs)

    return wrapper

def my_timer(orig_func):
    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 =  time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__,t2))
        return result
    
    return wrapper


# @decorator_function
# def display():
#     print('Display function ran')
import time


@my_logger
@my_timer
def display_info(name, age):
    time.sleep(1)
    print("display_info ran with arguments: ({}, {})".format(name, age))

display_info('Oscar', 66)

# decorated_display = decorator_function(display)
# decorated_display()

#display() # executes display() but with the decorator_function first, which
          # receives as original_function(display), defines wrapper_function
          # and returns wrapper_function which is ready to be executed , and
          # since original_function was display(), when decorator_function(display)
          # returns wrapper_function, prints the .format statement and then the
          # print from display()
