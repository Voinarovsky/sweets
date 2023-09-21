import datetime
x, y = 10, 13
h, m, c = 1, 37, 58
#1
total_parts = int( ((h*60*60)+(m*60)+c)/10 +((h*60*60)+(m*60)+c)/13 )
print(total_parts)

#2
estimate_f = float( ((h*60*60)+(m*60)+c)/x )
estimate_f = x - (estimate_f%1)*x #(estimate_f%1)*x сколько детали сделано в данный момент в пересчете на сек

estimate_s = float( ((h*60*60)+(m*60)+c)/y )
estimate_s = x - (estimate_s%1)*y

print(estimate_f)
print(estimate_s)

#3
if x<y: #1 изгат детали быстрее второго
    numdetal_x = float(((h * 60 * 60) + (m * 60) + c) / x) #сколько сделал деталей x
    numdetal_y = float(((h * 60 * 60) + (m * 60) + c) / y)
    how_many = numdetal_x - numdetal_y #количество деталей которое нужно сделать что бы догнать
    time = how_many*y #время котрое будет потрачено
    time = str(datetime.timedelta(seconds=time)) #переводим сек в часы и минуты
    print(time)
elif x>y :
    numdetal_x = float(((h * 60 * 60) + (m * 60) + c) / x)
    numdetal_y = float(((h * 60 * 60) + (m * 60) + c) / y)
    how_many = numdetal_y - numdetal_x
    time = how_many * x
    time = str(datetime.timedelta(seconds=time))
    print(time)

#4+5
x = float(input())
y= float(input())
i = int(not '-' in str(x-y)) #добавляю каунтер определяет 0 если x-y отрец число и 1 если - нет
while i==0 : #пока 0 т.е. пока x<y
    numdetal_x = float(((h * 60 * 60) + (m * 60) + c) / x)  # сколько сделал деталей x
    numdetal_y = float(((h * 60 * 60) + (m * 60) + c) / y)
    how_many = numdetal_x - numdetal_y  # количество деталей которое нужно сделать что бы догнать
    time = how_many * y  # время котрое будет потрачено
    time = str(datetime.timedelta(seconds=time))  # переводим сек в часы и минуты
    print(time)
    i+=2
while i==1 :
    numdetal_x = float(((h * 60 * 60) + (m * 60) + c) / x)
    numdetal_y = float(((h * 60 * 60) + (m * 60) + c) / y)
    how_many = numdetal_y - numdetal_x
    time = how_many * x
    time = str(datetime.timedelta(seconds=time))
    print(time)
    i +=2
#6
n = 924499
counter = 0 #пока 0  число непростое
for i in range(2,(n//2)+1 ): #нужно проверить числа только от 2 до половины числа
    if n % i == 0:
        counter += 1  #число делится без остатка на какое то значит меняем каунтер
if counter == 1:
    print(f'{n} число простое')
else:
    print(f'{n} число непростое')
#7
n = 1000000007
b = int(n ** (0.5))
counter = 0 #пока 0  число непростое
for i in range(2, b+1 ): #нужно проверить числа только от 2 до половины числа
    if n % i == 0:
        counter += 1  #число делится без остатка на какое то значит меняем каунтер
if counter == 1:
    print(f'{n} число простое')
else:
    print(f'{n} число непростое')
#8
n = 123456789
count = 0 #каунт считает сколько шагов
while n != 1: #пока не равно 1 продолжаем шаги
    if n % 2 == 0: #если число четное то делим на 2
        n = n / 2
        count += 1
    else:
        n = n*3 + 1
        count += 1
print(count)

#9
N = int(input())
primes = [i for i in range(N + 1)]  # Создается список из значений от 0 до N включительно
primes[1] = 0   # Вторым элементом списка является единица, которую # не считают простым числом. Забиваем ее нулем
i = 2   # Начинаем с 3-го элемента
while i <= N:
    if primes[i] != 0:  # Если значение текущей ячейки до этого не было обнулено, # значит в этой ячейке содержится простое число
        j = i + i   # Первое кратное ему будет в два раза больше
        while j <= N:
            primes[j] = 0   # и это число составное, # поэтому заменяем его нулем
            j = j + i   # переходим к следующему числу, # которое кратно i (оно на i больше)
    i += 1
primes = [i for i in primes if i != 0]  # Избавляемся от всех нулей в списке
print(primes)

#10
