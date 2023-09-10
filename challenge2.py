#def BMICalculator(weight, height):
#    return (weight/height**2)
#
#def divide(x, y):
#    try:
#        z = x/y
#    except ZeroDivisionError:
#        z = 'Cannot divide by zero'
#    finally:
#        return z
#
#
#print('*****BMICalculator*****\n')
#while True:
#    try:
#        weight = float(input('Please enter your weight: '))
#        height = float(input('Please enter you height: '))
#        break
#    except ValueError:
#        print('Invalid input')
#BMI = BMICalculator(weight, height)
#print(f'Your BMI is: {BMI}\n\n')
#
#
#print('*****Division Function*****\n')
#print('dividing by zero test: 10/0')
#print('Output: {0}'.format(divide(10, 0)))
#print('testing normally: 10/4')
#print('Output: {0}\n\n'.format(divide(10, 4)))
#
#
#print('*****Using files: opening, writing, reading, and appending*****\n')
#inputToWrite = input('Please enter a string to write to file: ')
#demoFile = open('demo.txt', 'w')
#demoFile.write(inputToWrite)
#demoFile.close()
#
#demoFile = open('demo.txt', 'r')
#print('This is what you wrote coming from file demo.txt')
#print(demoFile.read())
#demoFile.close()
#
#inputToWrite = input('\n Why don\'t you add another line in? Type here:')
#demoFile = open('demo.txt', 'a')
#demoFile.write('\n' + inputToWrite)
#demoFile.close()
#
#demoFile = open('demo.txt', 'r')
#print('This is what is in demo.txt now')
#print(demoFile.read())
#demoFile.close()
#
#
#print('*****Using Dictionaries*****\n')
#products = {
#    "Keyboard": 39.99,
#    "Headphones": 149.99,
#    "Monitor": 175.99,
#    "USB drive": 23.99,
#    "Mouse": 47.99
#}
#print('Here is a list of products, please type a name to see it\'s price:')
#for keys, value in products.items():
#    print(keys)
#productName = input('Enter product name from list above: ')
#print(f'Price: ${products[productName]}\n\n')


print('*****Using Lists: all odd numbers from 1 to 100*****')
print('Using a list:')
oddNumbers = [x for x in range(100) if x % 2 == 1]
print(oddNumbers)

print('using for loop with Range and a conditional (two birds with one stone) ')
for x in range(100):
    if (x%2 == 1):
        print(x)
