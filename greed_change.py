
'''
Gives the smallest number of coins to make a given amount of change. 

Asks the user to input the change as an int without a decimal.
So $269.63 would be 26963. 
(Don't use floats - unreliable comparisons)
'''

# object to keep currencies in
class Currency:
    def __init__(self, val, name):
        self.value = val
        self.name = name
    def __repr__(self):
        return repr(self.name)
    
# greedy algorithm for finding the lowest number of coins
def findBiggestChange(currencyList):
    # get input
    amount = int(input("enter amount (example: 145 for 1 dollar 45 cents)"))
    
    # set current amount and an empty list
    curAmt = amount
    totalCurrencies = []
    
    while curAmt > 0:
        curCur = None
        # find biggest valid currency
        for i in currencyList:
            if i.value <= curAmt:
                curCur = i
                break
        # sub currency value from current amount
        curAmt -= curCur.value
        # add this currency to the list
        totalCurrencies.append(curCur)
        
    print(totalCurrencies)
    
    return

# make a list of currencies
D100 = Currency(10000, "one hundred dollar bill")
D50 = Currency(5000, "fifty dollar bill")
D20 = Currency(2000, "twenty dollar bill")
D10 = Currency(1000, "ten dollar bill")
D5 = Currency(500, "five dollar bill")
D1 = Currency(100, "one dollar bill")
C50 = Currency(50, "fifty cent piece")
C25 = Currency(25, "quarter")
C10 = Currency(10, "dime")
C5 = Currency(5, "nickel")
C1 = Currency(1, "penny")

# add all to a list
allCurrencies = []
allCurrencies.append(D100)
allCurrencies.append(D50)
allCurrencies.append(D20)
allCurrencies.append(D10)
allCurrencies.append(D5)
allCurrencies.append(D1)
allCurrencies.append(C50)
allCurrencies.append(C25)
allCurrencies.append(C10)
allCurrencies.append(C5)
allCurrencies.append(C1)

# run greedy alg
findBiggestChange(allCurrencies)
