# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
if (a > b and b > c) or (a < b and b < c):
  mean = b
elif (a > b and a < c ) or ( a < b and a > c):
  mean = a
else:
  mean = c
print(f'среднее {mean}')
