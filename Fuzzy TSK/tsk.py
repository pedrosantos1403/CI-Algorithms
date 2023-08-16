import math

# define x universe
begin = -20
end = 20
step = 1
xs = [x for x in range(begin,end,step)]

# define average_x
average_x = 0
for x in xs:
    average_x += x
average_x /= len(xs)

# define standart_deviation
standart_deviation = 0
for x in xs:
    standart_deviation += (x - average_x)**2
standart_deviation /= len(xs)
standart_deviation = math.sqrt(standart_deviation)

# gaussiana?
w = []
for x in xs:
    w.append(math.exp((-1/2)*((x-average_x)/standart_deviation)**2))

# parameter p1?

# parameter p2?