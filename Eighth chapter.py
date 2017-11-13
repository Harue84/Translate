for looper in [1,2,3,4,5]:
    print "hello"

for looper in [1,2,3,4,5]:
    print looper

for looper in [1,2,3,4,5]:
    print looper, "times 8 =", looper*8

print "1 times 8 =", 1 * 8
print "2 times 8 =", 2 * 8
print "3 times 8 =", 3 * 8
print "4 times 8 =", 4 * 8
print "5 times 8 =", 5 * 8

for looper in range (1, 5):
    print looper, "times 8 =", looper * 8

print range (1, 5)
[1,2,3,4]

for looper in range (1, 11):
    print looper, "times 8 =", looper * 8

for i in range (1, 5):
    print i, "times 8 =", i * 8

for i in range (1,10,2):
    print i

for i in range (5,26,5):
    print i

for i in range (10, 1, -1):
    print i

import time
for i in range (10, 0, -1):
    print i
    time.sleep(1)
    print "BLAST OFF!"

for cool_guy in ["Spongebob", "Spiderman", "Justin Timberlake", "My Dad"]:
    print cool_guy, "is the coolest guy ever!"

print "Type 3 to continue, anything else to quit."
someInput = raw_input()
while someInput == '3':
    print "Thank you for the 3. Very kind of you."
    print "Type 3 to continue, anything else to quit."
    someInput = raw_input()
print "That's not 3, so I'm quitting now."

for i in range (1, 6):
    print
    print 'i =', i,
    print 'Hello, how',
    if i == 3:
        continue
    print 'are you today?'

for i in range (1, 6):
    print
    print 'i =', i,
    print 'Hello, how',
    if i == 3:
        break
    print 'are you today?'

print "How many times would the following loop run?"
for i in range (1, 6):
    print 'Hi, Warren'

long_string = """How many times would the following loop run?
And what would the values of i be for each loop?"""
for i in range (1, 6, 2):
    print 'Hi, Warren'

    
print "What list of numbers would range (1,8) give you?"
for i in range (1, 8):
    print i

print "What list of numbers would range (8) give you?"
for i in range (8):
    print i

print "What list of numbers would range (2,9,2) give you?"
for i in range (2, 9, 2):
    print i

print "What list of numbers would range (10,0,-2) give you?"
for i in range (10, 0, -2):
    print i

