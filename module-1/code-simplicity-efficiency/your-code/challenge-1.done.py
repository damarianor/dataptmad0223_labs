print('Welcome to this calculator where we can add and subtract whole numbers from zero to five')
a = int(input('Please choose your first number (1 to 5): '))
b = input('What do you want to do? plus or minus: ')
c = int(input('Please choose your second number (1 to 5): '))

numbers = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5}

operation = {'plus': 1, 'minus':-1}

if a in numbers.keys():
    num1 = numbers[a]
else: 
    print("I am not able to answer this question. Check your input.")

if b in operation.keys()
    factor = operation[b]
else:
    print("I am not able to answer this question. Check your input.")

if c in numbers.keys()  
    num2 = numbers[c] * factor
else:
    print("I am not able to answer this question. Check your input.")

result = sum([num1, num2])
result

dict_result = {0:'zero', 1:'one', 2:'two'}

if factor < 0:
    num_sign = 'negative '
else:
    num_sign = ''

num_sing = 'negative'
num_result = 'two'

f' {a} {b} {c} equals {num_sing}{num_result}'