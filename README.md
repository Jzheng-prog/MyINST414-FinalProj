# INST414 FINAL
The purpose of this project is to Analyze the spendings of Prince Georges County. There are hundred thousands of money going in and out of the counties each year in Maryland. But, where exactly are the moneys going to? To whom, for what reason, and how much? These are the questions we would like to answer in this project though data visualization.
- Using Panda module to manipulate csv file
- Using Matplotlib create graph visualization. 
# Data
- Variables
    - payee_name
    - agency
    - zip-code
    - amount
    - description

# Methods
    - defplotName()
        - This method will graph the number of times the county pays a payee.
    - def plotAmount()
        - This method will plot the total amount from each payee.
    - def getMeanSpendingByPayee(payeeName)
        - This method gets the mean spending of the specific payee. Takes in a string of the name of the payee_name.
    - def getOverallSpendingMean()
        - This is another mean method but this one gets the overall mean of the dataset.
    - def sortAcend()
        - 
    - def percentileRank(payee_name)
        - This method will compute the fraction of the spending less than or equal to the parameter.

# Analysis/Conclusion
Base on the output of the methods, we can conclude that there are many payee's that Prince Georges paid and gain from. Through, the method sort we can see that the lowest payment was to "Ping P Krell" which the spending is zero. By looking at the dataset we can see that Ping P Krell broke even with the payments. Using dataframe created by the modules pandas and using head and tail we can see the top 5 lowest and 5 highest transactions. There were couple of spendings on apparel, howver, it was evened out. The highest payment PG county has transfer is to 'PRINCE GEORGES COUNTY BOARD" with almost 1 billion dollars in accumulated transaction. The top 5 were spending on maryland transit system, construction, education, and community. We can conslude that most of the money PG county goes towards education purposes and the well being of the community.
