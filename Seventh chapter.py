num1 = float(raw_input("Enter the first number: "))
num2 = float(raw_input("Enter the second number: "))
if num1 < num2:
    print num1, "is less than", num2
if num1 > num2:
    print num1, "is greater than", num2
if num1 == num2:
    print num1, "is equal to", num2
if num1 != num2:
    print num1, "is not equal to", num2

answer = float(raw_input("Enter a number from 1 to 15"))
if answer >= 10:
    print "You got at least 10!"
elif answer >= 5:
    print "You got at least 5!"
elif answer >= 3:
    print "You got at least 3!"
else:
    print "You got less than 3."

age = float(raw_input("Enter your age: "))
grade = int(raw_input("Enter your grade: "))
if age >= 8:
        if grade >= 3:
            print "You can play this game."
else:
    print "Sorry, you can't play the game."

age = float(raw_input("Enter your age: "))
grade = int(raw_input("Enter your grade: "))
if age >= 8 and grade >= 3:
    print "You can play this game."
else:
    print "Sorry, you can play this game."

age = float(raw_input("Enter your age: "))
grade = int(raw_input("Enter your grade: "))
color = raw_input("Enter your favorite color: ")
if age >= 8 and grade >= 3 and color == "green":
    print "You are allowed to play this game."
else:
    print "Sorry, you can't play the game."

color = raw_input("Enter your favorite color: ")
if color == "red" or color == "blue" or color == "green":
    print "You are allowed to play the game."
else:
    print "Sorry, you can't play the game."

age = float(raw_input("Enter your age: "))
if not (age < 8):
    print "You are not allowed to play this game."
else:
    print "Sorry, you can't play the game."

my_number = 7
if my_number < 20:
    print 'Under 20'
else:
    print '20 or over'

my_number = 25
if my_number < 20:
    print 'Under 20'
else:
    print '20 or over'

num1 = float(raw_input("Enter the first number: "))
num2 = float(raw_input("Enter the second number: "))
if num1 > num2:
    print num1, "is greater than", num2
if num1 < num2:
    print num1, "is less than", num2
if num1 == num2:
    print num1, "is equal to", num2



