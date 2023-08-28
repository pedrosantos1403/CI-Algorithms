# Regressão Linear com uma variável

import math
import random
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Cálculo da função custo (J(O1, O2))
def cost_equation(m:int, h:list, y:list):

    # m -> Quantidade de entradas
    # h -> Valor previsto
    # y -> Valor real
    
    error_list = []
    for i in range (m):
        e = h[i] - y[i]
        error_list.append(e**2)

    # Retorna o valor da função custo
    return (1/2*m) * sum(error_list)

    

