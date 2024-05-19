
print('Welcome to the basic_math Python program.\n')

print('lets add and subtract two numbers!\n')

num1 = float(input('Enter the first number:\n'))
num2 = float(input('Enter the second number:\n'))

print(num1, '+', num2, '=', num1 + num2, '\n')
print(num1, '-', num2, '=', num1 - num2, '\n')

print('lets multiply and divide two numbers!\n')

num3 = float(input('Enter the first number:\n'))
num4 = float(input('Enter the second number:\n'))

print(num1, '*', num2, '=', num1 * num2, '\n')
if num4 != 0:
    print(num3, '/', num4, '=', num3 / num4, '\n')
else:
    print(num3, '/', num4, '= Error: cannot divid by zero\n')

print('Thank you for using the basic_math Python program')
