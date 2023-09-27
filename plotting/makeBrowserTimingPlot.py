import numpy
import matplotlib.pyplot as plt

offset = 0.2

x = numpy.arange(2)
y = [182.42, 189.14]
minVals = [174, 181]
maxVals = [216, 220]

max(maxVals)


def addlabels(x, y):
    for i in range(len(x)):
        plt.text(y[i] - 50, x[i], y[i], va="center")



def getDifference(a1, a2):
    result = []
    for i in range(len(a1)):
        result.append(abs(a1[i] - a2[i]))
    return result

errMin = getDifference(minVals, y)
print(errMin)
errMax = getDifference(maxVals, y)
print(errMax)
totalErr = [errMin, errMax]


bars = plt.barh(x, y, height=0.4)
plt.xlabel("time (ms)")
addlabels(x, y)
plt.yticks(x, ["original", "instrumented"], rotation=90, va="center")
plt.errorbar(y, x, xerr=totalErr, color="r", fmt="o")
bars[1].set_color("orange")

plt.show()
