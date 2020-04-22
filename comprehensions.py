
'''
    comprehensions: concise syntax for desc lists, sets and dict
                    Readable and expressive
                    Close to natural lang
    Syntax: [expr(item) for item in iterable]
'''
def comp_test():
    words = 'Este es un ejemplo de una lista a partir de un string'.split()
    print(words)
    print([len(word) for word in words]) #jala el length de cada elemento de la lista
    #el siguiente bloque hace lo mismo a patin
    lengths = []
    for word in words:
        lengths.append(len(word))
    print(lengths)

    from math import factorial
    f = [len(str(factorial(x))) for x in range(20)]
    #print(f) #imprime una lista con valores cuyo length del factorial esta entre 0 y 20
    #print(type(f)) #imprime la clase del objeto que es f (una lista)
    #print(type(f[3]))# imprime la clase del objeto que el indice 3 de f es (int)
    #la lista tiene duplicados, vamos a eliminarlos usando set
    s = {len(str(factorial(x))) for x in range(20)}
    #print(type(s))
    #print(s)
    #comprehension para dict, incluye key y value para cada item
    stat_to_cap = { 'Nuevo Leon' : 'Monterrey',
                    'Guanajuato' : 'Guanajuato',
                    'Jalisco' : 'Guadalajara',
                    'Yucatan' : 'Merida',
                    'Chihuahua' : 'chihuahua'}
    #vamos a invertir el orden del key y value e imprimirlo con el pretty print alv
    cap_to_stat = { cap : edo for edo, cap in stat_to_cap.items()}
    from pprint import pprint as pp
    #pp(cap_to_stat)
    w = ['hi' , 'hello', 'foxtrot', 'hotel'] #keys recientes sobreescriben keys anteriores
    #print({x[0] : x for x in w})#nomas el ultimo valor de la key es guardado 
    #la complejidad de lo que iteramos a un dict puede ser mas jarcor
    #pero no hay que pasarse de pistola con la raza
    #este ejemplo esta aceptable aun
    import os 
    import glob
    file_sz = {os.path.realpath(p): os.stat(p).st_size for p in glob.glob('*.py')}
    pp(file_sz)
    print(type(file_sz))
    
    from math import sqrt
    def is_prime(x): #checa si un numero es primo 
        if x < 2:
            return False #no siendo menor a dos
        for i in range(2, int(sqrt(x)) + 1):
            if x % i == 0:
                return False
        return True
    #pp([x for x in range(101) if is_prime(x)])
    prime_sq_div = {x*x:(1,x,x*x) for x in range(30) if is_prime(x)} #genera un dict con la raiz cuadrada del numero que es primo con su respectiva lista con 1, el numero primo y su razi cuadrada
    pp(prime_sq_div)
#comp_test()

def iteration_protocols_test():
    def first(iterable):
        iterator = iter(iterable)
        try:
            return next(iterator)
        except StopIteration:
            raise ValueError('iterable vacio')
    
    print(first(['1ro', '2do', '3ro']))#siempre jala el 1er valor por que list
    print(first({'1ro', '2do', '3ro'}))#cada corrida avanza una posicion por que dict
    #print(first(set())) # se turece por que no tiene nada el set
#iteration_protocols_test()

def gen123():
    yield 1
    yield 2
    yield 3
g = gen123()
#print(g)
#gen123()
#print(next(g))
#print(next(g))
#print(next(g))
#print(next(g)) # tira un StopIteration exception por que no hay un 4to valor
for v in gen123():
    print(v)
def gen246():
    print('yield 2')
    yield 2
    print('yield 4')
    yield 4
    print('yield 6')
    yield 6
g = gen246()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
    