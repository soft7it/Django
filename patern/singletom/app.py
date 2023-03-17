from db import *

# HW3: try/except -> catch exception -> message
count1 = loadCount()  # operatot 1
q1 = int(input('How many 1? '))


count1 -= q1
saveCount(count1)

count2 = loadCount()  # operatot 2
q2 = int(input('How many 2? '))
count2 -= q2
saveCount(count2)