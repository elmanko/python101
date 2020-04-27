import sys
#print(sys.getdefaultencoding()) # never assume the encoding, explicit is beter than implicit
"""
f = open('archivopegas.txt', mode='wt' , encoding='utf-8') #mode write text
print(type(f))
#print(help(f))

print(f.write('Pablito clavo un clavito, ')) #regresa 26 el numero de chars
f.write('en la cabeza\n')#New line needs to be provided manually 
f.write('de un calvito.')
f.close() # Files must be closed
# Now a new file is available in the FS with the name provided and the contet written into it

#Read
g = open('archivopegas.txt' , mode='rt' , encoding='utf-8') #mode read text
#print(g.read(26)) #prints the 26 first chars of the file, which we know is the first line
print(g.read()) #no args reads the whole file
print(g.seek(0)) # returns to the beginning of the file
print(g.readline())#returns first line
print(g.readline()) # returns next line, in this case the last line
print(g.readline()) # retuns an empty string as the file ended already
print(g.seek(0))# hopping to the beggining again
print(g.readlines()) # returns the lines as a list
print(type(g.readlines())) # is a list
g.close() #closing the file

#appending to an existing file
h = open('archivopegas.txt' , mode='at' , encoding='utf-8') #mode appending text
h.writelines(
    ['Tres tristes tigres, \n',
        'tragaban trigo, \n',
        'en tres tristes trastos, \n'])
h.close()
"""
f = open(sys.argv[1], mode='rt', encoding='utf-8')
for line in f:
    #print(line)# prints double new lines cuz of \n 
    sys.stdout.write(line) #prints only th \n in the file
f.close()
#this can be called by running: python3.6 ./files.py archivopegas.txt
