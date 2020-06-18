S = 'Spam'
print(S)
# Длина
print(len(S))

# Первый элемент в S, который индексируется по позиции, начиная с нуля
print(S[0])
# Второй элемент слева
print(S[1])

# Последний элемент с конца в S
print(S[-1])
# Второй элемент с конца в S
print(S[-2])

# Последний элемент в S
print(S[-1])
# Отрицательная индексация
print(S[len(S)-1])

# Нарезание (Срез S смещения 1 до 2 (не 3)
print(S[1:3])

# Все после первого элемента (1:len(S))
print(S[1:])

# Все кроме последнего элемента (S[:3])
print(S[0:3])

# Вся строка
print(S[:])

# Конкатенация

print(S + 'xyz')

# Повторение
print(S * 8)

# Развернуть в список
S = 'shrubbery'
L = list(S)
print(L)

# Изменить на месте и объединить с пустым разделителем
L[1] = 'c'
print(''.join(L))

# Гибрид байтов/списка
B = bytearray(b'spam')
B.extend(b'eggs')

# Преобразовать в обычную строку
print(B.decode())

# Найти смещение подстроки в S (если не найдена, то -1)
S = 'Spam'
print(S.find('pa'))

# Заменить вхождение подстроки в S другой подстрокой
print(S.replace('pa', 'XYZ'))
print(S)

# Разбить по разделителю в список подстрок
line = 'aaa,bbb,ccccc,dd'
print(line.split(','))

# Преобразовать в верхний и нижний регистры
S = 'spam'
print(S.upper())
print(S.lower())

# Проверить содержимое: isalpha, isdigit и т.д.
print(S.isalpha())

# Удалить пробелы с правой стороны
line = 'aaa,bbb,ccccc,dd\n'
print(line.rstrip())

# Скомбинировать две операции
print(line.rstrip().split(','))

# Форматирование
print('%s, eggs, and %s' % ('spam', 'SPAM!'))
print('{}, eggs, and {}'.format('spam', 'SPAM!'))

print(dir(S))

# Конкатенация
print(S + 'NI!')
print(S.__add__('NI!'))