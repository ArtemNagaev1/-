# Апгрейд калькулятора

def main():
    number = int(input('Введите число:'))
    action = input('Введите действие (sum), (max), (min):')
    if action == 'sum':
        summa_n(number)
    elif action == 'max':
        maximum(number)
    elif action == 'min':
        minimum(number)
    else:
        print('Введено неверное действие') 
    main()     

def summa_n(number):
    summ = 0
    while  number > 0:
        digit = number % 10
        summ += digit
        number //= 10
    print('Сумма цифр числа равна:', summ) 

def maximum(number):
    digit_max = 0
    while  number > 0:
        digit = number % 10
        digit_max = (digit_max + digit + abs(digit - digit_max)) / 2
        number //= 10
    print('Максимальная цифра числа равна: ', int(digit_max)) 

def minimum(number):
    digit_min = 9
    while  number > 0:
        digit = number % 10
        digit_min = (digit_min + digit) - ((digit_min + digit + abs(digit - digit_min)) / 2)
        number //= 10
    print('Минимальная цифра числа равна: ', int(digit_min)) 

main()