class RodCutProblems:
    
    def getRevenueArray(self, profit):         
       
        trace, revenue = [None]*len(profit), [None]*len(profit)
        revenue[0] = 0
        trace[0] = 0
        for j in range(1, len(profit)):
            # revenue[j] = -float("inf")
            revenue[j] = revenue[j-1]
            for i in range(1, j+1):# when using range, it doesnot include the last index (start, last)
                if revenue[j] < profit[i] + revenue[j-i]:
                    revenue[j] = profit[i] + revenue[j-i]
                    trace[j] = i                    
        return trace, revenue

    def getCostRevArray(self, profit, cost):            
       
        trace, revenue = [None]*len(profit), [None]*len(profit)
        revenue[0], trace[0] = 0, 0
        #j = 0
        for j in range(1, len(profit)):# when using range, it doesnot include the last index (start, last)
            revenue[j] = -float("inf")
            cutCost = 0
            for i in range(1, j+1):
                if i != j: 
                    cutCost = cost[j]
                if revenue[j] < profit[i] + revenue[j-i] - cutCost:
                    revenue[j] = profit[i] + revenue[j-i] - cutCost
                    trace[j] = i   
        return trace, revenue

    def getLimitRevArray(self, profit, limit):            
       
        trace, revenue = [None]*len(profit), [None]*len(profit)
        revenue[0], trace[0] = 0, 0
        #j = 0

        for j in range(1, len(profit)):# when using range, it doesnot include the last index (start, last)
            # revenue[j] = revenue[j-1]
            iLimit = limit[:j+1]
            revenue[j] = -float("inf")
            for i in range(1, j+1):
                left = iLimit[i]
                if revenue[j] < profit[i] + revenue[j-i]:
                    if left > 0: 
                        revenue[j] = profit[i] + revenue[j-i]
                        trace[j] = i   
                        iLimit[i] -= 1
        return trace, revenue

    def getModRevArray(self, rodSize, profit, sizes):            
       
        trace, revenue = [None]*(rodSize+1), [None]*(rodSize+1)
        revenue[0], trace[0] = 0, 0
        for j in range(1, rodSize+1):            
            revenue[j] = -float("inf")
            for i in range(1, j+1):
                if i in sizes:     
                    index = sizes.index(i)         
                    if revenue[j] < profit[index] + revenue[j-i]:
                        revenue[j] = profit[index] + revenue[j-i]
                        trace[j] = i   
        return trace, revenue

    def getModRevArray1(self, rodSize, profit, sizes):            
       
        trace, revenue = [None]*(rodSize+1), [None]*(rodSize+1)
        revenue[0], trace[0] = 0, 0
        for j in range(1, rodSize+1):            
            revenue[j] = -float("inf")
            for i, size in enumerate(sizes):       
                if j < size: 
                    revenue[j] = max(0, revenue[j] + profit[i])
                elif revenue[j] < profit[i] + revenue[j-size]:
                    revenue[j] = profit[i] + revenue[j-size]
                    trace[j] = size   
        return trace, revenue
    
    

    def getRCPSolution(self, profit, cost, limit, sizes, rodSize):        
        # trace, revenues = self.getRevenueArray(profit)
        # trace, revenues = self.getCostRevArray(profit, cost)
        # trace, revenues = self.getLimitRevArray(profit, limit)
        trace, revenues = self.getModRevArray1(rodSize, profit, sizes)
        size = rodSize
        netProfit = 0
        pieces = []

        while size > 0:
            cut = trace[size]
            pieces.append(cut)
            netProfit += profit[sizes.index(cut)]
            size -= cut
        # netProfit -= 1 # cost[trace[j]]
        # while size > 0:
        #     cut = trace[size]
        #     pieces.append(cut)
        #     netProfit += profit[cut]
        #     size -= cut
        #     # netProfit -= 1 # cost[trace[j]]
        return pieces, netProfit

""" rod cutting problem"""
profit = [0, 1, 6, 9, 10, 13, 17, 17, 20, 24, 28]
cost   = [0, 0, 1, 1, 2,  2,  2,  3,  3,  3,  4]
limit =  [0, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1]
testProfit = [0, 1, 5, 8, 10, 14, 17, 17, 20, 24, 26]#[(2, 2, 6) - 27]


sizes = [0, 2, 3, 5, 7, 10]
modProfit = [0, 5, 8, 10, 17, 23]#[(3, 7) 10]


# print algos.getRCPSolution(modProfit, cost, limit, sizes, 10)
            
    
