import matplotlib.pyplot as plt
import random
from solutionUtils import measureTimeMeanOneArg

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

def fisrtAlg():
    ...

def secondAlg():
    ...

funcRepeatTimes = 100

timesFirstAlg = []
timesSecondAlg = []
timesThirdAlg = []

for i in range(funcRepeatTimes):
    randomNumber = random.randint(10, 1_000_000)

    timeFirstAlg = measureTimeMeanOneArg()
    timesFirstAlg.append(timeFirstAlg)

    timeSecondAlg = measureTimeMeanOneArg()
    timesSecondAlg.append(timeSecondAlg)

    timeThirdAlg = measureTimeMeanOneArg()
    timesThirdAlg.append(timeThirdAlg)