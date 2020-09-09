from colorama import init
from colorama import Fore, Back, Style
init()

print(Back.BLACK)
print(Fore.GREEN)
what = input('Что будете делать?: +, -, *, /: ')

print(Back.RED)
print(Fore.YELLOW)
num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))

if what == '+':
    result = num1 + num2

elif what == '-':
    result = num1 - num2

elif what == '*':
    result = num1 * num2

elif what == '/':
    result = num1 / num2


print(Back.GREEN)
print(Fore.RED)
print('Результат: ' + str(result))
