import math
import random
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# h(x) = b0 + b1 * x
def prediction(b0, b1, x_i):
    return b1 * x_i + b0

#h(x_i) - y_i
def error(b0, b1, x_i, y_i):
    return prediction(b0, b1, x_i) - y_i

# J(b0,b1) = 1/2m * SUM(h(x_i) - y_i) ^ 2
def cost(b0, b1, x, y):
    error_list = []
    for x_i, y_i in zip(x, y):
        error_list.append(error(b0, b1, x_i, y_i)**2)

    # Returns J(b0,b1) value
    return (1 / (2 * len(x))) * sum(error_list)

# d/db0 J(b0,b1) = 1/m * SUM(h(x_i) - y_i)
def adjust_b0(b0, b1, x, y):
    error_list = []
    for x_i, y_i in zip(x, y):
        error_list.append(error(b0, b1, x_i, y_i))

    return (1 / len(x)) * sum(error_list)

# d/db1 J(b0,b1) = 1/m * SUM(h(x_i) - y_i) * x_i
def adjust_b1(b0, b1, x, y):
    error_list = []
    for x_i, y_i in zip(x, y):
        error_list.append(error(b0, b1, x_i, y_i) * x_i)

    return (1 / len(x)) * sum(error_list)
