
def hello_func(name, message='pinshi'):
    return '{} {} func.'.format(message, name)

# print(hello_func) # <function hello_func at 0x7f6a7d6d9dc0>
# print(hello_func().upper())


# print(hello_func('mario','joto'))

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ['Math', 'Art']
info = {'name': 'Juan', 'age': 14 }

student_info(*courses, **info)