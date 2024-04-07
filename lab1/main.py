def generateVariations(data, k, current=None, r=None):
    if current == None:
        current = []

    if r == None:
        r = []

    if k == 0:
        r.append(current)
        #print(current)
        return r

    for i, element in enumerate(data):
        currentCp = current[:]
        currentCp.append(element)
        dataCp = data[:]
        dataCp.remove(element)
        
        r = generateVariations(dataCp, k-1, currentCp, r)
    
    return r

def generateCombinationsWithDuplicates(data, m, current=None, r=None):
    if current == None:
        current = []

    if r == None:
        r = []

    if m == 0:
        r.append(current)
        return r

    dataCp = data[:]
    for i, element in enumerate(data):
        currentCp = current[:]
        currentCp.append(element)
        
        r = generateCombinationsWithDuplicates(dataCp, m-1, currentCp, r)
        dataCp.remove(element)
    return r
    
def calcDist(a, b):
    return ( (float(a[3])-float(b[3]))**2 + (float(a[4])-float(b[4]))**2 )**0.5

# #########################################################################
data = []
n = 5
k = 3
m = 3
for i in range(1, n+1):
    data.append(i)

cities = []
Iter = 0
with open('data.txt', 'r') as file:
    for row in file.readlines()[1:]:
        if Iter >= n:
            break
        data1 = row.strip().split(' ')
        city = []
        for iii in range(0, 5):
            city.append(data1[iii])

        cities.append(city)
        Iter += 1




#result = generateVariations(data, k)
result = generateVariations(cities, k)
i = 1
minDist = 213721372137
minDistPerm = []
for v in result:
    

    distance = 0
    city1 = v[0]
    for city in v[1:]:
        distance += calcDist(city1, city)
        city1 = city
    distance += calcDist(v[0], v[-1])

    if distance < minDist:
        minDist = distance
        minDistPerm = v

    print(i, " ", v)
    i += 1

print()
print("###########")

#result2 = generateCombinationsWithDuplicates(data, m)
result2 = generateCombinationsWithDuplicates(cities, m)
bestAvgCitizens = -1
bestAvgCitizensSet = []
i = 1
for v2 in result2:
    usedCities = []
    avgCitizens = 0
    for city in v2:
        if city in usedCities:
            continue
        usedCities.append(city)
        avgCitizens += int(city[2])

    print(i, " ", v2)
    i += 1
    
    if len(usedCities) != k:
        continue

    avgCitizens = avgCitizens/float(len(usedCities))
    if bestAvgCitizens < avgCitizens:
        bestAvgCitizens = avgCitizens
        bestAvgCitizensSet = v2
    
    
print()
print("##################")

print("Min distance = ", minDist, " through ", [x[1] for x in minDistPerm])
print("Best avg citizens = ", bestAvgCitizens, " in ", [x[1] for x in bestAvgCitizensSet])
