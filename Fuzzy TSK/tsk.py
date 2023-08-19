import math
import random
import numpy as np
import matplotlib.pyplot as plt

# define x universe
ITERATION_LIMIT = 1000
BEGIN = -2
END = 2
LEARNING_RATE = 0.01
STEP = 0.01

def gaussian_calculator(x, average_x, standart_deviation_x):
    return math.exp((-1/2) * ((x - average_x) / standart_deviation_x)**2)

def y_calculator(x,p,q):
    # y1 = p1 * x + q1
    # y2 = p2 * x + q2
    return p*x + q

def tsk_calculator(w1,y1,w2,y2):
    return (w1*y1 + w2*y2) / (w1 + w2)

def adjust_pq(error, w1, w2, x, group):
    if group == 1:
        return LEARNING_RATE * (error * (w1 / (w1 + w2)) * x)
    else:
        return LEARNING_RATE * (error * (w2 / (w1 + w2)) * x)

def adjust_average_x(error, w1, w2, y1, y2, average_x, standart_deviation_x, x, group):
    if group == 1:
        return LEARNING_RATE * (error * w2 * ((y1 - y2) / (w1 + w2)**2) * w1 * ((x - average_x) / standart_deviation_x**2))
    else:
        return LEARNING_RATE * (error * w1 * ((y2 - y1) / (w1 + w2)**2) * w2 * ((x - average_x) / standart_deviation_x**2))

def adjust_standart_deviation_x(error, w1, w2, y1, y2, average_x, standart_deviation_x, x, group):
    if group == 1:
        return LEARNING_RATE * (error * w2 * ((y1 - y2) / (w1 + w2)**2) * w1 * (x - average_x)**2 / standart_deviation_x**3)
    else:
        return LEARNING_RATE * (error * w1 * ((y2 - y1) / (w1 + w2)**2) * w2 * (x - average_x)**2 / standart_deviation_x**3)

def plot(xs, ys, i, average_error):
    # Criando um gráfico de dispersão
    plt.scatter(xs, np.power(xs, 2), label='f(x) = x²', color='blue')
    plt.scatter(xs, ys, label='Fuzzy TSK', color='red')

    # Adicionando rótulos aos eixos e título ao gráfico
    plt.xlabel('x')
    plt.ylabel('y')

    plt.title('adjust number: {}\n average error: {}'.format(i,average_error))
    plt.legend()
    plt.show()

def main():
    # define start average_x
    average_x1 = -2
    average_x2 = 2

    # define start standart_devitation_x
    standart_deviation_x1 = 1.5
    standart_deviation_x2 = 1.5

    # start p1, p2, q1, q2
    p1 = random.random()*abs(BEGIN)
    p2 = random.random()*abs(BEGIN)
    q1 = random.random()*abs(BEGIN)
    q2 = random.random()*abs(BEGIN)

    # start xs, ys and errors
    x = BEGIN
    xs = []
    ys = []
    errors = []
    while (x <= END):
        xs.append(x)
        x += STEP
        ys.append(0)
        errors.append(0)

    for i in range(ITERATION_LIMIT):
        # pass through xs in a random order
        indexes = [z for z in range(0,len(xs),1)]
        random.shuffle(indexes)

        while(indexes != []):
            # break when there's no more index
            random_index = indexes.pop()
            x = xs[random_index]

            # calculate gaussian w1
            w1 = gaussian_calculator(x, average_x1, standart_deviation_x1)

            # calculate gaussian w2
            w2 = gaussian_calculator(x, average_x2, standart_deviation_x2)

            # calculate y1
            y1 = y_calculator(x, p1, q1)

            # calculate y2
            y2 = y_calculator(x, p2, q2)

            # calculate ys[random_index]
            ys[random_index] = tsk_calculator(w1,y1,w2,y2)

            # calculate errors[random_index]
            errors[random_index] = ys[random_index] - x**2

            # update p1
            p1 -= adjust_pq(errors[random_index], w1, w2, x, 1)

            # update p2
            p2 -= adjust_pq(errors[random_index], w1, w2, x, 2)

            # update q1
            q1 -= adjust_pq(errors[random_index], w1, w2, x, 1)
            
            # update q2
            q2 -= adjust_pq(errors[random_index], w1, w2, x, 2)

            # hold the old average value for future
            leg_average_x1 = average_x1
            leg_average_x2 = average_x2

            # update average_x1
            average_x1 -= adjust_average_x(errors[random_index], w1, w2, y1, y2, average_x1, standart_deviation_x1, x, 1)

            # update average_x2
            average_x2 -= adjust_average_x(errors[random_index], w1, w2, y1, y2, average_x1, standart_deviation_x1, x, 2)
            
            # update standart_deviation_x1
            # remember: must use old average value
            standart_deviation_x1 -= adjust_standart_deviation_x(errors[random_index], w1, w2, y1, y2, leg_average_x1, standart_deviation_x1, x, 1)
        
            # update standart_deviation_x2
            # remember: must use old average value
            standart_deviation_x2 -= adjust_standart_deviation_x(errors[random_index], w1, w2, y1, y2, leg_average_x2, standart_deviation_x2, x, 2)

        # find current average_error
        average_error = 0
        for e in errors:
            average_error += e
        average_error /= len(errors)
        
        # plot progress
        if i % 200 == 0:
            plot(xs, ys, i, average_error)

    # plot final answer
    plot(xs, ys, ITERATION_LIMIT, average_error)