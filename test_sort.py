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

