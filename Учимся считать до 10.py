a = 12345678910
b = True
x = 1
d = 2
while a:
    c = int (input('Добро пажаловать сейчас мы научимся считать до 10 - '))
    if c == a:
        c = False
        for e in range (1, 11):
            print (e)
        else:
            print('Поздравляю вы молодец')
    if c < a:
     p = int (input('Хотите сравнить ответ'))
    if p == x:
        for e in range (1, 11):
            print(e)
    if p < d:
        print('Хорошо пробуем еще раз')