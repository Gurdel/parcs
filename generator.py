from random import randint as r

with open('input1800k.txt', 'w') as sw:
    for _ in range(1800000):
        #print(',', end='')
        n = r(3, 10)#вимірність
        #генерю площину та заповнюю тестові точки
        B = r(1, 100)
        A = []
        x = []
        y = []
        for _ in range(n):
            A.append(r(1, 100))
            x.append(r(1, 100))
            y.append(r(1, 100))
        #із певною ймовірністю змінюю точки так, щоб вони належали площині
        if(r(0, 10) == 0):#якщо точка х належить площині
            ind = r(0, n-1)#індекс змінної, яка виправить решту виразу
            buf = B - sum([x[i] * A[i] for i in range(n)])#теперішнє відхилення від площини
            buf += x[ind] * A[ind]#вилучаю теперішній вплив точки, значення якої будемо виправляти
            x[ind] = buf / A[ind]#нове значення цієї точки
        if(r(0, 10) == 0):#якщо точка у належить площині
            ind = r(0, n-1)#індекс змінної, яка виправить решту виразу
            buf = B - sum([y[i] * A[i] for i in range(n)])#теперішнє відхилення від площини
            buf += y[ind] * A[ind]#вилучаю теперішній вплив точки, значення якої будемо виправляти
            y[ind] = buf / A[ind]#нове значення цієї точки
        #записую результат у файл
        sw.write(str(n))
        [sw.write(' '+str(i)) for i in A]
        sw.write(' '+str(B))
        [sw.write(' '+str(i)) for i in x]
        [sw.write(' '+str(i)) for i in y]
        sw.write('\n')
