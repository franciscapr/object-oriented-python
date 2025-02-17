
def calculateAverage(numberList):
    total = 0.0
    
    for number in numberList:
        total = total + number
    nElements = len(numberList)
    average = total/nElements
    return average