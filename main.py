#!/usr/bin/python3.5
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


disp = display_nth_root(666,6)
#los dunder o double underscore __name__ name son features, o funciones especiales... creo
'''
num=nth_root(200,2)
print(num)
'''