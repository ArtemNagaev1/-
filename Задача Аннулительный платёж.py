print('Аннуитетный платёж')
summ_credit = float(input('Введите сумму кредита: '))
years = int(input('На сколько лет выдан: '))
procent = float(input('Сколько процентов годовых? '))
procent /= 100
year_procent = procent
body_credit = 0
years2 = years


for data in range(1, years+1):
  if data<4:
    k = procent*(1 + procent) ** years2/((1 + procent) ** years2 - 1)
    years2 -= 1
    A = summ_credit*k
    round(A,2)
    year_procent *=  summ_credit
    body_credit =  A -  year_procent
    print('\nОстаток долга на начало периода: ', summ_credit)
    summ_credit += year_procent - A
    print('Выплачено процентов: ', year_procent)
    print('Выплачено тело кредита: ', body_credit)
  year_procent =  procent
  body_credit = 0


extension = int(input('\nНа сколько лет продляется договор?: '))
bet = int(input('Увеличение ставки до: '))
bet /= 100
year_procent = bet
years = years2 = (years - 3) + extension


for data in range(1, years+1):
  if data<years+1:
    k = bet*(1 + bet) ** years2/((1 + bet) ** years2 - 1)
    years2 -= 1
    A = summ_credit*k
    round(A,2)
    year_procent *=  summ_credit
    body_credit =  A -  year_procent
    print('\nОстаток долга на начало периода: ', summ_credit)
    summ_credit += year_procent - A
    print('Выплачено процентов: ', year_procent)
    print('Выплачено тело кредита: ', body_credit)
    year_procent =  bet
    body_credit = 0
  else:
    k = bet*(1 + bet) ** years2/((1 + bet) ** years2 - 1)
    years2 -= 1
    A = summ_credit*k
    round(A,2)
    year_procent *=  summ_credit
    body_credit =  A -  year_procent
    print('\nОстаток долга на начало периода: ', summ_credit)
    summ_credit -= body_credit
    print('Выплачено процентов: ', year_procent)
    print('Выплачено тело кредита: ', body_credit)
print('Остаток долга: ', summ_credit)