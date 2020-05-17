
'''
This is the program for giving the optimal amount of change
Fixes the previous greedy problem

QUARTERS are worth 12 cents again

But entering 16 (as in 16 cents) will give you
dime, nickel, penny

'''

import math

# object to keep currencies in
class Currency:
    def __init__(self, val, name):
        self.value = val
        self.name = name
    def __repr__(self):
        return repr(self.name)
        
class RecDepthAndList:
    def __init__(self):
        self.depth = 0
        self.allChange = []
    
# greedy algorithm for finding the lowest number of coins
def startChange(currencyList, targetAmount):
    
    curRecList = RecDepthAndList()
    curRecList.depth = math.inf
    for i in currencyList:
        newDepList = RecDepthAndList()
        RecList = findWaysToChange(currencyList, targetAmount, i, newDepList)
        #if RecList != None:
            #print("bubbled up:")
            #print (RecList.allChange)
        if RecList != None and RecList.depth < curRecList.depth:
            curRecList = RecList
    
    return curRecList

def findWaysToChange(currencyList, targetAmount, changeType, depthList):
    
    curDepList = RecDepthAndList()
    curDepList.depth = depthList.depth
    curDepList.allChange = depthList.allChange.copy()
    
    curAmt = targetAmount
    curAmt -= changeType.value
    
    if curAmt == 0:
        curDepList.depth += 1
        curDepList.allChange.append(changeType)
        return curDepList
        
    if curAmt < 0:
        return None

    curDepList.depth += 1
    curDepList.allChange.append(changeType)
    
    deeperDepList = RecDepthAndList()
    deeperDepList.depth = math.inf
    for i in currencyList:
        nxtDepList = findWaysToChange(currencyList, curAmt, i, curDepList)
        #if nxtDepList != None:
            #print (nxtDepList.allChange)
        if nxtDepList != None and nxtDepList.depth < deeperDepList.depth:
            deeperDepList = nxtDepList
            #print (nxtDepList.allChange)
            break;

    #print ("selected: " + str(nxtDepList.depth))
    #print (nxtDepList.allChange)
    return nxtDepList

# make a list of currencies
D100 = Currency(10000, "one hundred dollar bill")
D50 = Currency(5000, "fifty dollar bill")
D20 = Currency(2000, "twenty dollar bill")
D10 = Currency(1000, "ten dollar bill")
D5 = Currency(500, "five dollar bill")
D1 = Currency(100, "one dollar bill")
C50 = Currency(50, "fifty cent piece")
C25 = Currency(12, "quarter")
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

# run alg
amount = int(input("enter amount (example: 145 for 1 dollar 45 cents)"))
num = startChange(allCurrencies, amount)
print(str(num.depth) + " " + str(num.allChange))
