import matplotlib.pyplot as plt
import random
from solutionUtils import measureTimeMean, primeDivisors

"""
Запустить 100 раз и измерить среднее время работы алгоритма для разных чисел от 10 до 1_000_000.
Сравнить время работы алгоритмов. 

1.	Реализовать алгоритм Евклида поиска наибольшего общего делителя (НОД) целых чисел a и b, используя следующие свойства НОД:
1)	НОД(a, b) = a, если b = 0;
2)	НОД(a, b) = b, если a = 0;
3)	НОД(a, b) = НОД(b, a), если a < b;
4)	НОД(a, b) = НОД(a - b, b), если b  0.

2.	Другой вариант реализации алгоритма Евклида основан на соотношениях:
1)	НОД(a, b) = a, если b = 0;
2)	НОД(a, b) = b, если a = 0;
3)	НОД(a, b) = НОД(b, a), если a < b;
4)	НОД(a, b) = НОД(b, a mod b), если b  0.

3.	Реализовать алгоритм поиска НОД с помощью разложения на множители.
Одним из способов нахождения НОД является разложение чисел на простые множители. Алгоритм нахождения наибольшего общего делителя (НОД) двух чисел с помощью разложения на простые множители состоит из следующих шагов:
1.	Разложить каждое число на простые множители.
2.	Определить общие простые множители.
3.	Записать каждый общий множитель столько раз, сколько он встречается в разложении обоих чисел наименьшее количество раз.
4.	Перемножить выбранные множители.
"""

def firstAlg(a, b):
    while b != 0:
        if a < b:
            a, b = b, a
        a -= b
    return a

def secondAlg(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def thirdAlg(a, b):
    aDivs = primeDivisors(a)
    bDivs = primeDivisors(b)

    commonDivs = set(aDivs).intersection(set(bDivs))

    gcd = 1
    for div in commonDivs:
        aPower = 0
        while a % div == 0:
            a = a // div
            aPower += 1
        bPower = 0
        while b % div == 0:
            b = b // div
            bPower += 1
        minPower = min(aPower, bPower)
        gcd *= div ** minPower

    return gcd

repeatTimes = 100
funcRepeatTimes = 1

timesFirstAlg = []
timesSecondAlg = []
timesThirdAlg = []
randomNumbers = []

for i in range(repeatTimes):
    randomNumberFirst = random.randint(10, 1_000_000)
    randomNumberSecond = random.randint(10, 1_000_000)

    randomNumbers.append(randomNumberFirst)

    timeFirst = measureTimeMean(firstAlg, randomNumberFirst, randomNumberSecond)
    timesFirstAlg.append(timeFirst)

    timeSecond = measureTimeMean(secondAlg, randomNumberFirst, randomNumberSecond)
    timesSecondAlg.append(timeSecond)

    timeThird = measureTimeMean(thirdAlg, randomNumberFirst, randomNumberSecond)
    timesThirdAlg.append(timeThird)

sortedData = sorted(zip(randomNumbers, timesFirstAlg, timesSecondAlg, timesThirdAlg), key=lambda x: x[0])
randomNumbers = [x[0] for x in sortedData]
timesFirstAlg = [x[1] for x in sortedData]
timesSecondAlg = [x[2] for x in sortedData]
timesThirdAlg = [x[3] for x in sortedData]

plt.figure(figsize=(12, 6))

plt.plot(randomNumbers, timesFirstAlg, label="Первый алгоритм Евклида", marker="o")
plt.plot(randomNumbers, timesSecondAlg, label="Второй алгоритм Евклида", marker="o")
plt.plot(randomNumbers, timesThirdAlg, label="Третий алгоритм Евклида", marker="o")

plt.xlabel("Случайные числа")
plt.ylabel("Время выполнения (в секундах)")

plt.title("Сравнение времени выполнения алгоритмов Евклида")
plt.legend()
plt.grid(True)

plt.xscale("linear")
plt.yscale("linear")

plt.show()