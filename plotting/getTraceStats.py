import sys
import numpy
import matplotlib.pyplot as plt

if len(sys.argv) <= 1:
    print("no target specified")
    exit(1)
traceFile = open(sys.argv[1])

reads = 0
writes = 0
forks = 0
joins = 0
acquires = 0
releases = 0

for line in traceFile:
    trace = line.split("|")
    # trace[0]: EventAction/Thread as Tn
    # trace[1]: operation(target)
    # trace[2]: code location
    eventAction = int(trace[0][1:])
    partitionedOperation = trace[1].partition("(")
    operation = partitionedOperation[0]
    target = partitionedOperation[2].strip("()")
    match operation:
        case "r":
            reads += 1
        case "w":
            writes += 1
        case "fork":
            forks += 1
        case "join":
            joins += 1
        case "acq":
            acquires += 1
        case "rel":
            releases += 1

total = reads + writes + forks + joins + acquires + releases
print(f"reads: {reads}, writes: {writes}, forks: {forks}, joins: {joins}, acquires: {acquires}, releases: {releases}")


def getPercent(total, val):
    return f"{round(((val / total) * 100), 2)}%"


def addPercentageLabels(x, y):
    for i in range(len(x)):
        plt.text(i, y[i], y[i], ha="center")
        plt.text(i, y[i] + total * .02, getPercent(total, y[i]), ha="center", size="small")


x = numpy.arange(4)
y = [reads, writes, forks, acquires]
plt.bar(x, y)
plt.xticks(x, ["reads", "writes", "forks", "acquires"])
plt.ylabel("Events counted")
addPercentageLabels(x, y)
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.show()
