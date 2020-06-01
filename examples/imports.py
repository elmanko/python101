import sys #system
sys.path.append('/home/mnk/Projects/python101') #manually adding a path to sys.path, also not best practice
import my_modules as mm
from my_modules import find_index, test
import my_modules
from my_modules import * # not a good practice, not useful tracking definitions 

import random #standard library module
import math #standard library module
import datetime,calendar #standard library module
import os # access to the os
import antigravity #xkcd webcomic :)

courses = ['History', 'Math', 'Physics','Coding']

index = my_modules.find_index(courses, 'Coding') # imported only my_modules
index1 = find_index(courses, 'Math') # imported specifically 
index2 = mm.find_index(courses, 'History') #imported find_index with my_modules as mm

# print(index)
# print(index1)
# print(index2)
# print(test) # test from my_modules.py is available thru the import
# print(sys.path) # list all directories sys has access to


random_course = random.choice(courses)
print(random_course)

rads = math.radians(90)

print(math.sin(rads))

today = datetime.date.today()
print(today)

print(calendar.isleap(2020))

print(os.getcwd())

print(os.__file__)

