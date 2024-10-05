num1 = [1, 3, 5, 4, 9]#выделить четные индекса и сделать сумму, потом умножить на последний индекс

counter1 = 0 #Счетчик для индексных чисел
for i in range(0, len(num1), 2): #Выделил четные идекса
    counter1 += num1[i] #Сумма индексов

result1 = counter1 * num1[-1] #Сумму умножил на последний индекс
print(result1) #Вывел результат

num2 = [6]

counter2 = 0
for i in range(0, len(num2), 2):
    counter2 += num2[i]

result2 = counter2 * num2[-1]
print(result2)

num3 = []

if len(num3) == 0: #Если размер переменной num3 = 0, то выводим число 0
    counter3 = 0
    print(counter3)
else:
    counter3 = 0
    for i in range(0, len(num3), 2):
        counter3 += num3[i]

    result3 = counter3 * num3[-1]
    print(result3)