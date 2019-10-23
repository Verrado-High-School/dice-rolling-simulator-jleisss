# Name:
# Period
# Dice Rolling Simulator
import random

rolls = int(input("how many rolls? "))
x = 1

num1 = 0
num2 = 0
num3 = 0
num4 = 0
num5 = 0
num6 = 0

while x <= rolls:
	randNum = random.randint(1, 6)
	
	if randNum == 1:
		num1 += 1
		print("roll number: " + str(x) + ":1") 
	elif randNum == 2:
		num2 += 1
		print("roll number: " + str(x) + ":2") 
	elif randNum == 3:
		num3 += 1
		print("roll number: " + str(x) + ":3") 
	elif randNum == 4:
		num4 += 1
		print("roll number: " + str(x) + ":4") 
	elif randNum == 5:
		num5 += 1
		print("roll number: " + str(x) + ":5") 
	else:
		num6 += 1
		print("roll number: " + str(x) + ":6") 
		x += 1


print("Out of the " + str(rolls) + " rolls;")
print("The number 1 was rolled " + str(num1) + " times,")
print("The number 2 was rolled " + str(num2) + " times,")
print("The number 3 was rolled " + str(num3) + " times,")
print("The number 4 was rolled " + str(num4) + " times,")
print("The number 5 was rolled " + str(num5) + " times,")
print("And the number 6 was rolled " + str(num6) + " times")
print("The number 1 was rolled " + str(num1 / rolls * 10))
print("The number 2 was rolled " + str(num2 / rolls * 10))
print("The number 3 was rolled " + str(num3 / rolls * 10))
print("The number 4 was rolled " + str(num4 / rolls * 10))
print("The number 5 was rolled " + str(num5 / rolls * 10))
print("The number 6 was rolled " + str(num6 / rolls * 10))
