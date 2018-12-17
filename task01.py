a = int(input ('введите трехзначное число: ')) 
b = list(map(int, str (a))) 
summ = b[0] + b[1] + b[2]
multi = b[0] * b[1] * b[2]
print(f'сумма цифр: {summ}') 
print(f'сумма цифр: {multi}')
