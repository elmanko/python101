#!/usr/bin/env python3.6
'''print("hello world")

var1 = 1 
var2 = "1" + "lol".strip() #replace. or lstrip. or rstrip

var4 = [1,"mames" , "mames2"]

var5 = ()
var6 = {}
var7 = True
var8 = 0.5

var9 = list()
var10 = None
var9.append(var1)

comentario de bloque alv
no 

print(var1)
print(var2)
print(var8)
print(var4)
print(var5)
print(var6)
#print(var1+var7+var6+var7)
print('no mames {},{},{}'.format(1,2,var6))
print(var9)
'''

#while True:
#    print('while ')
#   break

#while True:
#    response = input()
#   if int(response) % 7 == 0:
#       break
"""
i = 0
while i <= 10:
    print(i)
    i+=1

from urllib.request import urlopen
story = urlopen('https://raw.githubusercontent.com/elmanko/python101/master/README.md')
story_words = []
for line in story:
    #decode('utf8') jala strings en lugar de bytes a line_words
    line_words = line.decode('utf8').split()
    for word in line_words:
        story_words.append(word)
story.close()
print(story_words)
"""

def square(x):
    return x * x


#print(square(3))

def even_or_odd(n):
    if n % 2 == 0:
        print('even')
        return
    print('odd')

w = even_or_odd(31)

print(w is None)

def nth_root(radicand,n):
    return radicand ** (1/n)

def ordinal_suffix(value):
    s = str(value)
    if s.endswith('11'):
        return 'th'
    elif s.endswith('12'):
        return 'th'
    elif s.endswith('13'):
        return 'th'
    elif s.endswith('1'):
        return 'st'
    elif s.endswith('2'):
        return 'nd'
    elif s.endswith('3'):
        return 'rd'
    return 'th'

def ordinal(value):
    return str(value) + ordinal_suffix(value)

def display_nth_root(radicand, n):
    root = nth_root(radicand , n)
    message = 'The ' + ordinal(n) + ' root of ' + str(radicand) + ' is ' + str(root)
    print(message)


#disp = display_nth_root(666,6)
#los dunder o double underscore __name__ name son features, o funciones especiales... creo
'''
num=nth_root(200,2)
print(num)
'''
def dictionaries_test():
        people = dict(Alex=31,Ana=23,Pau=27 )
        books = [('Book 1', '1a'),('Book2', '2a'),('Book3','3a')]
        names = [('pepe',20),('juan',33),('marcela',32),('octiavia',33)]
        peeps = people.copy()
        print(peeps)
        pee = dict(peeps)
        print(pee)
        print('peeps is pee')
        print(peeps is pee)
        print('peeps == pee')
        print(peeps == pee)
        print(id(peeps))
        print(id(pee))

        p = dict(MArtin=21, Jose=44 , joseluis = 90)
        pee.update(p)

        print(pee)
        #nm = dict(names)
        #print(names)
        #print(nm)
        #print(books,people)
        #print(people)
        print(books)
        boox = dict(books)
        boox.update({'Book3':'666','Book4':'5a'})
        print('after books.update')
        print(boox)

        #loops
        dik = dict( key1 = 'val1', key2 ='val2',
                     key3 = 'val3', key4 = 'val4',
                     key5 = 'val5', key6 = 'val6')
        #print(dik)
        for k in dik:
            print(f"key= {k}, value= {dik[k]}")
        
        for v in dik.values():
            print(v)
        
        for k in dik.keys():
            print(k)
        print('con items: ')
        for k,v in dik.items():
            print(f" k= {k} , v= {v}")
        #ejemplo con in y not in

        banda = dict( pepe='vato', maria='ruca', tracy='puto', gonzalo='vato', mafer='ruca')
        band = banda.copy()
        """print(banda)
        print('pepe'in banda)
        print( 'puto' in banda)
        print('jose' not in banda)
        print('mafer'not in banda)
        print(banda)
        print(band)
        del band['tracy']
        print(band)"""

        band.update(eusebio=['1','2','3'])
        #print(band)
        band['eusebio']+= [4,5,'6']
        band.update(pepe=['vato','machin'])
        band['pepe']+= ['jalisquillo','pendejo']
        #print(band)
        #print(band['pepe'])

        for v in band.values():
            print(v)
        band['alex'] = ['vato','gto']
        #print(band)
        print('pp')
        from pprint import pprint as pp

        pp(band)

dictionaries_test()