#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
res = 0 #результат
d20 = random.randint(1, 20) #бросок кубика
d20d = 0 #сброс второго кубика
d20d20 = 0 #сброс третьего кубика

##lang = int(input('Language (RUS = 1, ENG = 2) ')) #язык программы
while True:
    
    a = int(input("Сколько действий за ход по одному объекту совершит игрок: "))
    err = 1 #проверка на ошибки
    if a < 1:
        print('Количество действий должно быть положительным числом!')
        err = 0
    if a > 3:
        print('Количество действий превышено!')
        err = 0

    if a == 1:
        num = int(input('Параметр характеристики: '))
        if num >= 1 and num <= 3:
            res = d20 + num - 4
        elif num >= 4 and num <= 6:
            res = d20 + num - 3
        else:
            print ('Параметр вышел за границы!')
            err = 0

    if a == 2: 
        d20d = random.randint(1,20)

        num1 = int(input('Первый параметр характеристики: '))
        if num1 < 1 or num1 > 6:
            print ('Параметр вышел за границы!')
            err = 0
        else:
            if num1 >= 1 and num1 <= 3:
                num1 = d20 + num1 - 4
            elif num1 >= 4 and num1 <= 6:
                num1 = d20 + num1 - 3

        num2 = int(input('Второй параметр характеристики: '))
        if num2 < 1 or num2 > 6:
            print ('Параметр вышел за границы!')
            err = 0
        else:
            if num2 >= 1 and num2 <= 3:
                num2 = d20d + num2 - 4
            elif num2 >= 4 and num2 <= 6:
                num2 = d20d + num2 - 3
        sum = num1 - num2
        res = (num1 + num2 + sum) // 2 

    if a == 3:
        d20d = random.randint(1,20)
        d20d20 = random.randint(1, 20)

        num1 = int(input('Первый параметр характеристики: '))
        if num1 < 1 or num1 > 6:
            print ('Параметр вышел за границы!')
            err = 0
        else:
            if num1 >= 1 and num1 <= 3:
                num1 = d20 + num1 - 4
            elif num1 >= 4 and num1 <= 6:
                num1 = d20 + num1 - 3

        num2 = int(input('Второй параметр характеристики: '))
        if num2 < 1 or num2 > 6:
            print ('Параметр вышел за границы!')
            err = 0
        else:
            if num2 >= 1 and num2 <= 3:
                num2 = d20d + num2 - 4
            elif num2 >= 4 and num2 <= 6:
                num2 = d20d + num2 - 3

        num3 = int(input('Третий параметр характеристики: '))
        if num3 < 1 or num3 > 6:
            print ('Параметр вышел за границы!')
            err = 0
        else:
            if num3 >= 1 and num3 <= 3:
                num3 = d20d20 + num3 - 4
            elif num2 >= 4 and num2 <= 6:
                num3 = d20d20 + num3 - 3

        sum = num1 - num2 - num3
        res = (num1 + num2 + num3 + sum) // 3

    if err != 0:
        print ('Бросок кубика:', d20)
        if d20d != 0:
            print ('Второй бросок кубика:', d20d)
        if d20d20 != 0:
            print ('Третий бросок кубика: ', d20d20)
        print ('Результат с учетом характеристик:', res)
    
    z = input("Продолжить? (Да, Нет) ")
    print("\n")
    if (z == 'Нет'):
        break
    else:
        continue

end = input("Конец программы. Нажми Enter.")


# In[ ]:





# In[ ]:





# In[ ]:




