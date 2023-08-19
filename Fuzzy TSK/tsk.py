import math

# define x universe
ITERATION_LIMIT = 1000
BEGIN = -200
END = 200
LEARNING_RATE = 0.01
STEP = 1

# define start average_x
average_x1 = 0
average_x2 = 0

# define start standart_devitation_x
standart_deviation_x1 = 0
standart_deviation_x2 = 0

# start xs and ys
xs = [x for x in range(BEGIN, END, STEP)]
ys = [0 for y in range(BEGIN, END, STEP)]

# start average_error
average_error = 0

for i in range(ITERATION_LIMIT):
    while(True):
        # pass through xs in a random order
        # break when there's no more index
        random_index = 0
        x = xs[random_index]

        # calculate gaussian_w1 
        # calculate gaussian_w2

        # calculate y1 = p1 * x + q1
        # calculate y2 = p2 * x + q2

        # calculate ys[random_index] = (w1*y1 + w2*y2) / (w1 + w2)

        # calculate errors[random_index] = ?

        # update p1 ?
        # update p2 ?
        # update q1 ?
        # update q2 ?

        # update average_x1
        # update average_x2
        # update standart_deviation_x1
        # update standart_deviation_x2

        # update average_error
    
    # plot progress

# plot final answer