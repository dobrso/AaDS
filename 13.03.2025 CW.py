import numpy as np

class Solution:
    @staticmethod
    def task1():
        return np.array([range(16)]).reshape(4, 4)

    @staticmethod
    def task2():
        return np.zeros(25).reshape(5, 5)

    @staticmethod
    def task3():
        return np.ones(18).reshape(3, 6)

    @staticmethod
    def task4():
        return np.eye(4)

    @staticmethod
    def task5():
        return np.random.rand(6).reshape(2, 3)

    @staticmethod
    def task6():
        arr = np.array([range(12)]).reshape(3, 4)
        return np.ndim(arr)

    @staticmethod
    def task7():
        arr = np.array([range(10)]).reshape(2, 5)
        return np.shape(arr)

    @staticmethod
    def task8():
        arr = np.array([range(12)]).reshape(3, 4)
        return np.size(arr)

    @staticmethod
    def task9():
        arr = np.array(range(9)).reshape(3, 3)
        return arr.dtype

    @staticmethod
    def task10():
        arr = np.array([range(9)]).reshape(3, 3)
        return arr[1, 2]

    @staticmethod
    def task11():
        arr = np.array([range(16)]).reshape(4, 4)
        return arr[1, :]

    @staticmethod
    def task12():
        arr = np.array([range(25)]).reshape(5, 5)
        return arr[:, 2]

    @staticmethod
    def task13():
        arr = np.array([range(36)]).reshape(6, 6)
        return arr[:3, :3]

    @staticmethod
    def task14():
        arr = np.array([range(9)]).reshape(3, 3)
        return arr.flatten()

    @staticmethod
    def task15():
        arr = np.array([range(12)]).reshape(2, 6)
        return arr.reshape(3, 4)

    @staticmethod
    def task16():
        arr1 = np.array([range(4)]).reshape(2, 2)
        arr2 = np.array([range(4)]).reshape(2, 2)
        return arr1 + arr2

    @staticmethod
    def task17():
        arr = np.array([range(9)]).reshape(3, 3)
        return arr * 5

    @staticmethod
    def task18():
        arr1 = np.array([range(4)]).reshape(2, 2)
        arr2 = np.array([range(4)]).reshape(2, 2)
        return arr1 * arr2

    @staticmethod
    def task19():
        arr = np.array([range(16)]).reshape(4, 4)
        return np.mean(arr)

    @staticmethod
    def task20():
        arr = np.array([range(9)]).reshape(3, 3)
        return np.mean(arr, 1)

    @staticmethod
    def task21():
        arr = np.array([range(25)]).reshape(5, 5)
        return np.mean(arr, 0)

    @staticmethod
    def task22():
        arr = np.array([range(16)]).reshape(4, 4)
        return np.max(arr), np.min(arr)

    @staticmethod
    def task23():
        arr = np.array([range(9)]).reshape(3, 3)
        return np.sum(arr)

    @staticmethod
    def task24():
        arr = np.array([range(6)]).reshape(2, 3)
        return arr.T

    @staticmethod
    def task25and26():
        arr = np.array([range(9)]).reshape(3, 3)
        np.save("arr.npy", arr)
        loadedArr = np.load("arr.npy")
        return loadedArr

    @staticmethod
    def task27and28():
        arr = np.array([range(4)]).reshape(2, 2)
        np.savetxt("arr.txt", arr)
        loadedArr = np.loadtxt("arr.txt")
        return loadedArr

    @staticmethod
    def task29():
        arr = np.array([range(9)]).reshape(3, 3)
        for row in arr:
            print(row)

    @staticmethod
    def task30():
        arr = np.array([range(8)]).reshape(2, 4)
        for row in arr:
            for el in row:
                print(el)