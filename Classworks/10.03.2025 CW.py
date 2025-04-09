import numpy as np

class Solution:
    @staticmethod
    def task1():
        return np.array(range(1, 11))

    @staticmethod
    def task2():
        return np.zeros(7)

    @staticmethod
    def task3():
        return np.ones(5)

    @staticmethod
    def task4():
        return np.arange(10, 50, 5)

    @staticmethod
    def task5():
        return np.linspace(0, 100, 6)

    @staticmethod
    def task6():
        arr = np.array([i for i in range(10)])
        return f"{arr[1]}, {arr[-1]}, {arr[3]}, {arr[6]}"

    @staticmethod
    def task7():
        arr = np.array([range(10)])
        for i in arr:
            print(i)

    @staticmethod
    def task8():
        arr1 = np.arange(10, 50, 5)
        arr2 = np.arange(50, 90, 5)
        return arr1 + arr2

    @staticmethod
    def task9():
        arr = np.array([range(10)])
        return arr * 2

    @staticmethod
    def task10():
        arr = np.array([range(10)])
        return arr **2

    @staticmethod
    def task11():
        arr = np.array([range(10)])
        return f"{np.min(arr)}, {np.max(arr)}"

    @staticmethod
    def task12():
        arr = np.array([range(10)])
        return f"{np.mean(arr)}, {np.std(arr)}"

    @staticmethod
    def task13():
        arr = np.array([range(10)])
        return f"{np.log(arr)}, {np.exp(arr)}, {np.sin(arr)}"

    @staticmethod
    def task14():
        return np.random.rand(10)

    @staticmethod
    def task15():
        return np.random.randint(1, 101, 6)

    @staticmethod
    def task16():
        arr = np.array([range(10)])
        return arr.reshape(2, 5)

    @staticmethod
    def task17():
        arr = np.array([range(9)])
        return arr.reshape(3, 3)

    @staticmethod
    def task18():
        arr = np.array([range(10)])
        return arr[arr > 5]

    @staticmethod
    def task19():
        arr = np.array([range(10)])
        vecFunc = np.vectorize(lambda x: x **3)
        return vecFunc(arr)

    @staticmethod
    def task20():
        arr = np.array([range(10)])
        np.save("arr.npy", arr)
        return np.load("arr.npy")