Group members:
Adam Yabai
Shamry Igat
Clinton Patma



num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
operator = input("Enter any operator [+ - * /]: ")

result = 0
if operator == '+':
	result = num1 + num2
elif operator == '-':
	result = num1 - num2
elif operator == '*':
	result = num1 * num2
elif operator == '/':
	result = num1 / num2

else:
	print("Error!")
	
print(num1, operator, num2, ":", result)
