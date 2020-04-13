#!/usr/bin/python3.5
print("hello world")

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
'''
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
