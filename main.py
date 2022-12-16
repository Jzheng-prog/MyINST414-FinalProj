import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import csv




# this method will graph the number of times the county pays a payee.
def plotName():
    uniquePayeeName = []
    allPayeeName = []
    count = []

    with open('spendingData.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)


        #get all unique names in the csv file and all names
        for obj in csv_reader:
            name = obj[0]
            #get all payee_name in the file
            allPayeeName.append(name)
            if name not in uniquePayeeName:
                uniquePayeeName.append(name)

        #count all the names into an array list
        for name in uniquePayeeName:
            count.append(allPayeeName.count(name))
            #print(count)

    # the first element is payee_name
    plt.plot(uniquePayeeName[1:100], count[1:100])
    plt.ylabel("Total Amount")
    plt.xlabel("Payee Name")
    plt.show()

# this method will plot the total amount from each payee_name
def plotAmount():

    output = getTotalSpendingForEachPayee()

    xName = list(zip(*output))[0]
    yAmount = list(zip(*output))[1]

    plt.plot(xName[0:50],yAmount[0:50])
    plt.ylabel("Total Spending $")
    plt.xlabel("Payee Name")

    plt.show()

#get the mean spending of the specific payee. Take in a string of the name of the payee_name
def getMeanSpendingByPayee(payeeName):

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

    #first element is a label
    zipped.pop(0)

    #sum is the total, counter is the divisor
    sum = 0
    counter = 0

    for name, amount in zipped:
        if name == payeeName:
            sum += float(amount)
            counter += 1

    return "Mean: " + str(sum / counter)

# this is another mean method but will the overall mean
def getOverallSpendingMean():

    allAmount = []

    total = 0

    with open('spendingData.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        #get all amount/payee in the csv file and all names
        for obj in csv_reader:
            amount = obj[3]
            allAmount.append(amount)

    allAmount.pop(0)
    
    for amount in allAmount:
        total += float(amount)

    return "Mean: " + str(total/len(allAmount))

#will sort all the data in acending by amount
def sortAcend():

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

    newList = list(map(tuple, d.items()))

    return sorted(newList, key = lambda a: float(a[1]))

# this method will compute the fraction of spending lees than or equal to the parameter
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

    print("Percentile Rank of " + payee_name + ": " + str(perRank))


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

#instead of a line graph this method is plotting a scatter plot
def plotScatter():

    data = getTotalSpendingForEachPayee()

    plt.scatter(*zip(*data[0:100]))
    plt.ylabel("Total Spending $")
    plt.xlabel("Payee Name")
    plt.show()



def main():

    sortList = sortAcend()

    df = pd.DataFrame(sortList)

    print(df.head())
    print(df.tail())
    


if __name__ == "__main__":
        main()