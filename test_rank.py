import csv
def percentileRank(payee_name):

    totalList = getTotalSpendingForEachPayee()

    compare = 0

    count = 0

    for x in totalList:
        if x[0] == payee_name:
            compare = x[1]
    
    for list in totalList:
        if list[1] <= compare:
            count += 1

    perRank = 100.0 * count / len(totalList)

    return perRank

def getTotalSpendingForEachPayee():
    allAmount = []
    allPayeeName = []

    with open('spendingData.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        #get all amount/payee in the csv file and all names
        for obj in csv_reader:
            amount = obj[3]
            name = obj[0]
            allAmount.append(amount)
            allPayeeName.append(name)

    #combine the two list to key:value pair
    zipped = list(zip(allPayeeName, allAmount))

    zipped.pop(0)

    d = {x:0 for x, _ in zipped}

    #add all the values with the same key
    for key, value in zipped:
        d[key] += float(value)
    return list(map(tuple, d.items()))

assert 87.39674926725286 == percentileRank("UNIFIRST")
assert 98.90754063415933 == percentileRank("MB STAFFING SERVICES LLC")