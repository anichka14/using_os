import numpy as np


def orthonormal_v1(a):
    for i in range(a.shape[0]):  # матриця квадратна
        for j in range(a.shape[0]):  # i - один рядок, j - другий рядок
            prod = np.dot(a[i], a[j])
            if i == j:
                if not np.isclose(prod, 1):
                    return False
            else:
                if not np.isclose(prod, 0):
                    return False
    return True


# матриця транспонована, якщо її добуток на неї транспоновану є одиничною матрицею
def orthonormal_v2(a):
    y = np.dot(a, a.T)
    eye = np.eye(a.shape[0])
    return np.all(np.isclose(y, eye))  # чи всі елементи матриць True, тоді повертає True


if __name__ == "__main__":
    array = np.random.rand(3, 3)
    print(array)
    print(orthonormal_v1(array))
    print(orthonormal_v2(array))

    array = np.eye(3)  # одинична матриця
    print(array)
    print(orthonormal_v1(array))
    print(orthonormal_v2(array))

    array = np.array(
        [
            [np.sqrt(2) / 2, np.sqrt(2) / 2, 0],
            [np.sqrt(2) / 2, -np.sqrt(2) / 2, 0],
            [0, 0, 1]
        ]
    )
    print(array)
    print(orthonormal_v1(array))
    print(orthonormal_v2(array))
