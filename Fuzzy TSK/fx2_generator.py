begin = -20
end = 20
step = 1

xs = [x for x in range(begin,end,step)]

file = open("fx2.csv", "w")
file.write("x,fx2\n")
for x in xs:
    file.write("{},{}\n".format(x,x**2))
file.close()