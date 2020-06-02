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