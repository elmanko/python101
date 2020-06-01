
# LEGB = Local, Enclosing, Global, Built-in

x = 'global x'
# import builtins

# print(dir(builtins))
# m = min([5,3,23,5,76,4,0])
# print(m)

# def test(z):
#     # global x
#     x = 'local x'
#     # print(y)
#     print(z)

# test('local z')
# print(z)
# print(y) # NameError: name 'y' is not defined


def outer():
    # x = 'outer x' # x is local to outer()

    def inner():
        # nonlocal x # not same as global, only inside enclosure( funcions in function)
        # x = 'inner x' # x is local to inner()
        print(x) # LEGB -> inner x
    
    inner() #LEGB -> outer x
    print(x)

outer() # LEGB, checks for inner() x, then outer() x, the ENCLOSER



