def findFactors(point = 8, numBF = 0, stage = 1):
    test = point / numBF
    count = 0
    for i in range(0, numBF):
        print count
        count = test + count

def numButterFlies(point = 8, stage = 0):
    N = point / 2
    numBF = pow(2, stage)
    print "At stage " + str(stage) + " number of butterflies are " + str(numBF)
    findFactors(point = point, numBF = numBF)

def fft(point = 8):
    numButterFlies(point = point, stage = 0)
    numButterFlies(point = point, stage = 1)
    numButterFlies(point = point, stage = 2)
    numButterFlies(point = point, stage = 3)

def demo():
    fft(point = 16)
    #findFactors()

if __name__ == '__main__':
    demo()
