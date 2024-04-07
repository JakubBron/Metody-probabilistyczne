import matplotlib.pyplot as plt

def __main__():
    M = 2**31 - 1
    # other primes: 1000000009
    N = 1000000
    a = 742938285
    seed = 2137
    numberOfRanges = 10

    # task 1
    randomSequenceLinear = linearGenerator(a, 0, M, seed, N)
    splitAndCount(randomSequenceLinear, numberOfRanges, M//numberOfRanges)
    drawPlot(randomSequenceLinear, 1000)
    # task 2
    randomSequenceRegister = shiftRegisterGenerator(seed, N)
    splitAndCount(randomSequenceRegister, 2, 1)
    drawPlot(randomSequenceRegister, 2)
    return 0

def avg(data: list) -> float:
    avg_ = 0
    for value in data:
        avg_ += value
    avg_ /= len(data)
    return avg_

def drawPlot(data: list, bins: int):
    plt.hist(data, bins=bins, edgecolor='black')
    plt.title("Linear Generator")
    plt.show()

def shiftRegisterGenerator(seed: int, length: int) -> list:
    # for p = 2 and q = 1
    if length <= 0:
        return None
    
    p = 3
    q = 1
    seed = list(map(int, bin(seed)[2:]))    # skip '0b' prefix
    randomSequence = []
    
    for i in range(length):
        if(i<p):
            randomSequence.append(seed[i])
        else: 
            randomSequence.append(randomSequence[-1] ^ randomSequence[-3])
           # print(randomSequence[-1])

    return randomSequence

def linearGenerator(a: int, c: int, M: int, seed: int, length: int) -> list:
    # if c = 0, generator is multiplicative
    if length <= 0:
        return None
    
    seed = seed % M
    randomSequence = []
    for i in range(length):
        if i == 0:
            randomSequence.append(seed)
        else:
            randomSequence.append((a * randomSequence[i-1] + c) % M)    
    
    return randomSequence

def splitAndCount(sequence: list, numberOfRanges: int, rangeWidth: int):
    ranges = [0 for i in range(0, numberOfRanges)]

    for value in sequence:
        ranges[value//rangeWidth] += 1
    
    avg_ = avg(ranges)
    for i in range(0, numberOfRanges):
        print(str(i*rangeWidth) + " -> " + str((i+1)*rangeWidth-1) + ": " + str(ranges[i]) + " (" + str((ranges[i]-avg_) / avg_ * 100) + "%)")
    print("Average in range: ", avg_)

__main__()