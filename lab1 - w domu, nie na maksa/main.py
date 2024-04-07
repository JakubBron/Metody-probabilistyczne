from math import sin, cos, acos, radians

def generatePermutations(data, current=None, result=None):
    # Heap algorithm to generate permutations
    if result is None:
        result = []
    if current is None:
        current = []
    
    if len(data) == 0:
        result.append(tuple(current))
        return result
    
    for element in data:
        newPerm = current[:]    # all array
        newPerm.append(element)

        newData = data[:]
        newData.remove(element)

        result = generatePermutations(newData, newPerm, result)
    return result
    

def generateCombinations(data, k, current=None):
    if current is None:
        current = []

    if len(current) == k:
        return [current]
    combs = []
    for i, val in enumerate(data):
        newCurrent = current.copy()
        newCurrent.append(val)
        newData = data[i+1:]
        combs += generateCombinations(newData, k, newCurrent)
    return combs

def loadData():
    cities = []
    with open('miastaSmall.in', 'r') as file:
        for row in file.readlines()[1: ]:   # skip first row (header)
            data = row.strip().split(' ')   # remove whitespaces&newlines and split by space
            city = []
            city.append(data[0])    # id
            city.append(data[1])    # name
            city.append(data[2])    # population
            city.append(data[3])    # latitude
            city.append(data[4])    # longitude
            cities.append(city)
    return cities

def calculateDistance(c1, c2):
    # Haversine formula
    R = 6371   # Earth radius in km
    lat1 = radians(float(c1[3]))
    lon1 = radians(float(c1[4]))
    lat2 = radians(float(c2[3]))
    lon2 = radians(float(c2[4]))
    return acos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(lon2 - lon1))*R

def findShortestRoute(permutations):
    print(len(permutations), "permutations")

    shortestRoute = 213721372137
    shortestRouteCities = []
    for p in permutations:
        distance = 0
        prevCity = p[0]
        for city in p[1:]:
            distance += calculateDistance(prevCity, city)
            prevCity = city
        
        print("Route: ", [str(city[1]) for city in p], " distance: ", distance)
        if distance < shortestRoute:
            shortestRoute = distance
            shortestRouteCities = p
    print("Shortest route: ", [str(city[1]) for city in shortestRouteCities], " distance: ", shortestRoute)

def findCityWithPopulationAroundHalfOfAllCities(combinations, sum):
    sum = sum/2
    minDifference = 213721372137
    result = []

    print(len(combinations), "combinations; half of sum of all: ", sum)
    for c in combinations:
        currentSum = 0
        for city in c:
            currentSum += int(city[2])
        
        difference = abs(currentSum - sum)
        if difference < minDifference:
            minDifference = difference
            result = c
        
        print("Combination: ", [str(city[1]) for city in c], " with sum: ", currentSum, " (", abs(currentSum-sum), ")")

    print("Best sum for permutation: ", [str(city[1]) for city in result])

# /////////////////////////////////////////////////////////////////////// #

cities = loadData()
n = len(cities)

k = n//2
print("1. ")
permutations = generatePermutations(cities)
findShortestRoute(permutations)

print("2. ")
combinations = generateCombinations(cities, k)
sumAllPopulations = sum([int(city[2]) for city in cities])
findCityWithPopulationAroundHalfOfAllCities(combinations, sumAllPopulations)