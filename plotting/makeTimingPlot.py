import numpy
import matplotlib.pyplot as plt

width = 0.4
offset = 0.2


def addlabels(x, y, offset):
    for i in range(len(x)):
        plt.text(i + offset, y[i] + 0.005, y[i], ha="center")


x = numpy.arange(3)
# yeah i know this is scuffed, but this is where the data goes!
y1 = [0.06, 0.01, 0.062]
y2 = [3.19, 0.33, 2.681]

plt.bar(x - offset, y1, width)
plt.bar(x + offset, y2, width)
plt.ylabel("time (s)")
addlabels(x, y1, -offset)
addlabels(x, y2, offset)
plt.xticks(x, ["user", "system", "real"])
plt.legend(["original", "instrumented"])

plt.show()
