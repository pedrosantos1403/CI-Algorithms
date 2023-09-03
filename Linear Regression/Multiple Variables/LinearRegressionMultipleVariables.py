import math
import random
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Alterar a função h(x) = b0 + b1 * x1 + b2 * x2

# h(x) = b0 + b1 * x1 + b2 * x2
def prediction(b0, b1, b2, x1_i, x2_i):
    return b0 + b1 * x1_i + b2 * x2_i

#h(x_i) - y_i
def error(b0, b1, b2, x1_i, x2_i, y_i):
    return prediction(b0, b1, b2, x1_i, x2_i) - y_i

# J(b0,b1,b2) = 1/2m * SUM(h(x_i) - y_i) ^ 2
def cost(b0, b1, b2, x1, x2, y):
    error_list = []
    for x1_i, x2_i, y_i in zip(x1, x2, y):
        error_list.append(error(b0, b1, b2, x1_i, x2_i, y_i)**2)

    return (1 / (2 * len(x1))) * sum(error_list)

# d/db0 J(b0,b1) = 1/m * SUM(h(x_i) - y_i)
def adjust_b0(b0, b1, b2, x1, x2, y):
    error_list = []
    for x1_i, x2_i, y_i in zip(x1, x2, y):
        error_list.append(error(b0, b1, b2, x1_i, x2_i, y_i))

    return (1 / len(x1)) * sum(error_list)

# d/db1 J(b0,b1) = 1/m * SUM(h(x_i) - y_i) * x_i
def adjust_b1(b0, b1, b2, x1, x2, y):
    error_list = []
    for x1_i, x2_i, y_i in zip(x1, x2, y):
        error_list.append(error(b0, b1, b2, x1_i, x2_i, y_i) * x1_i)

    return (1 / len(x1)) * sum(error_list)

# d/db12 J(b0,b1,b2) = 1/m * SUM(h(x_i) - y_i) * x_i
def adjust_b2(b0, b1, b2, x1, x2, y):
    error_list = []
    for x1_i, x2_i, y_i in zip(x1, x2, y):
        error_list.append(error(b0, b1, b2, x1_i, x2_i, y_i) * x2_i)

    return (1 / len(x1)) * sum(error_list)
