def __main__():
    M = 2**31
    # other primes: 1000000009
    N = 1000000
    a = 69069
    c = 1
    seed = 15
    numberOfRanges = 10
    p = 7
    q = 3
    seedShift = [1,1,0,1,0,0,1]     # 105dec = 1101101bin

    print("task 1")
    sequence1 = linearGenerator(a,c,N, M,seed)
    splitForRanges(sequence1, numberOfRanges, M//numberOfRanges)

    print("task 2")
    sequence2 = shiftRegister(p, q, seedShift, N)
    splitForRanges(sequence2, numberOfRanges, M//numberOfRanges)
    return


def shiftRegister(p, q, seed, N):
    # make M numbers, each number created using 31 bits
    ans = []
    binary = seed
    #print(len(binary)-p)
    for i in range(N):
        while len(binary) < 31:
            binary.append( binary[len(binary)-p] ^ binary[len(binary)-q] )
        
        createdNumber = 0
        for i in range(len(binary)):
            createdNumber *= 2
            createdNumber += binary[i]
        #print(createdNumber)
        ans.append(createdNumber)
        binary = binary[-p:]

    return ans

def linearGenerator(a, c, N, mod, seed):
    sequence = []
    seed %= mod
    sequence.append(seed)
    for i in range(N-1):
        sequence.append((a * sequence[i-1] + c)%mod)
    
    return sequence

def calcAvg(tab):
    avg = 0
    for value in tab:
        avg += value
    
    return avg/len(tab)

def splitForRanges(data, ranges, rangeLen: int):
    result = []
    for i in range(ranges):
        result.append(0)

    for value in data:
        #print(value, " " , value // rangeLen)
        result[value // rangeLen ] += 1
    
    avg = calcAvg(result)
    for i in range(ranges):
        print(str((i)*rangeLen) + " -> " + str((i+1)*rangeLen-1)+ ": " + str(result[i]) + " " + str( round((result[i] - avg) / avg * 100, 2) ) + " % of avg in range")


__main__()