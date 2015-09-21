import math

def printSingleButterfly(start = 0, end = 2):
    k = 0
    for i in range(start, end):
        print "x" + str(i) + " + " + "x" + str(end + k)
        print "x" + str(i) + " - " + "x" + str(end + k)
        k = k + 1

def printButterflies(point = 0, count = [], stage = 1):
    N = point
    k = 0
    half = point / 2
    if len(count) == 1:
        printSingleButterfly(start = 0, end = half)
    elif len(count) != 1:
        for i in range(0, len(count)):
           if i == len(count) - 1:
               printSingleButterfly(start = count[i], end = count[i] + half)
           else:
               printSingleButterfly(start = count[i], end = count[i] + half)


def findFactors(point = 8, numBF = 0, stage = 1):
    test = point
    count = []
    for i in range(0, numBF):
        if i == 0:
            count.append(0)
        else:
            count.append(count[i - 1] + test)
            
    #print count

    printButterflies(point = point, count = count, stage = stage)

def numButterFlies(point = 8, stage = 0):

    numBF = pow(2, stage)
    print "At stage " + str(stage) + " number of butterflies are " + str(numBF)
    findFactors(point = point, numBF = numBF, stage = stage + 1)

def fft(point = 8, stage = 0, stages = 3):
    if stages > 0:
        numButterFlies(point = point, stage = stage)
        fft(point = point / 2, stage = stage + 1, stages = stages - 1)

    #numButterFlies(point = point, stage = 1)
    #numButterFlies(point = point, stage = 2)
    #numButterFlies(point = point, stage = 3)

def demo():
    point = 8
    stages = int(math.log(8)/math.log(2))
    fft(point = point, stages = stages)
    #findFactors()

if __name__ == '__main__':
    demo()
