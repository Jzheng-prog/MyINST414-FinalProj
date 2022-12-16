import csv

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

    return sum / counter

assert 135.46292003593888 == getMeanSpendingByPayee("UNIFIRST")
assert 2678.979870340344 == getMeanSpendingByPayee("MB STAFFING SERVICES LLC")