#Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
a = int(input('введите номер букв: '))
a = a+96
if a >= 96 & a <= 122:
  aChar = chr(a);
  print(f'буква {aChar}')
else:
  print(f'буква с таким номер не найдена')
