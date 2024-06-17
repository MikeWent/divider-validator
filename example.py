import numpy as np

import validator


def f(x, n) -> list[int]:
    # this function creates an array of normally distributed random numbers.
    # this function does NOT solve the task. it's used purely as an example.
    return np.clip(np.random.normal(x / 2, 15, x), 0, x).astype(int)


data = [f(100, 10) for _ in range(10_000)]
validator.plot_distribution(data)
