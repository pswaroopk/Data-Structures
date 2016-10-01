
import random
import math
def getRandInt(i, j):
    return random.randint(i, j)

class Algorithms(object):
    def __init(self, unSortedlist):
        self.list = unSortedlist


    def activitySchedule(self, start, finish, profit):
        if len(start) != len(finish) != len(profit):
            print "Check the schedule arrays"   
            return [], [], []
        n  = len(start) # total no of events
        activities = [None]*(n)
        activities[0] = 0        
        used = [None]*n #activity used for the problem
        traceBack = [None]*n #js are stored here
        cnt = 1
        for i in range(1, n):
            activities[i] = activities[i-1]
            used[i] = False
            j = i - 1    
            lower = 0
            upper = j             
            while  lower <= upper:  
                j = int(math.floor((upper + lower)/2))
                if finish[j] < start[i]:
                    lower = j + 1
                elif finish[j] > start[i]:
                    upper = j - 1
                else:
                    break
            if finish[j] > start[i]:
                j = lower - 1
            traceBack[i] = j   #store the comaptible activity wrto i in traceback  [J]                          
            if profit[i] + activities[j] > activities[i]:
                activities[i] = profit[i] + activities[j]
                used[i] = True   
        return activities, used, traceBack

    def activityScheduleSpl(self, start, finish, profit, special):
        if len(start) != len(finish) != len(profit):
            print "Check the schedule arrays"   
            return [], [], []
        n  = len(start) # total no of events
        activities = [None]*(n)
        activities[0] = 0        
        used = [None]*n #activity used for the problem
        traceBack = [None]*n #js are stored here
        cnt = 1
        for i in range(1, n):
            isSpl = special[i]
            activities[i] = activities[i-1]
            used[i] = False
            j = i - 1    

            ''' linear search for j'''
            while finish[j] > start[i]:
                j -= 1
            if special[i] & 
                    
                
            ''''Binary Search for j'''  
            # lower = 0
            # upper = j            
            # while  lower <= upper:  
            #     j = int(math.floor((upper + lower)/2))
            #     if finish[j] < start[i]:
            #         lower = j + 1
            #     elif finish[j] > start[i]:
            #         upper = j - 1
            #     else:
            #         break
            # if finish[j] > start[i]:
            #     j = lower - 1
            traceBack[i] = j   #store the comaptible activity wrto i in traceback  [J]                          
            if profit[i] + activities[j] > activities[i]:
                activities[i] = profit[i] + activities[j]
                used[i] = True   
        return activities, used, traceBack

    def findSolution(self, activities, used, trace, size):
        solution = []      
        while size > 0:
            if used[size] == True:
                solution.append(size)
                size = trace[size]
            else: 
                size -= 1
        profit = activities[solution[0]]
        solution.reverse()
        return solution, profit

    def getRevenueSubArray(self, pList):
            
        A, R = []
        for i in range(i, len(pList)):
            A[i] = -1
        R[0] = 0
        #j = 0
        for j in range(1, len(pList)):
            R[j] = -9999999
            for i in range(1, j):
                if R[j] < pList[i] + R[j-i]:
                    R[j] = pList[i] + R[j-i]
                    A[j] = i
                    
        return A, R
    

    def getOptimalSolution(self, pList):
        return None
        # A, R = self.getRevenueSubArray(pList)
        # maxVal = R[-1]
        # sizes = []
        # rodSize = len(pList)
        # while 
        #     sizes.append(A[i])
            
    def quickSort(self, randList, p, r):
        if p >= r: return randList
        q, t, randList = self.randomizedPartition(randList, p, r)
        self.quickSort(randList, p, q-1)
        self.quickSort(randList, t+1, r)
        return randList

    def randomizedPartition(self, randList, p, r):
        i = getRandInt(p, r)
        x = randList[i]
        randList[i], randList[r] =  randList[r], randList[i]
        i = p-1
        t = r
        j = p
        while j < t:
            if randList[j] < x:
                i+=1
                randList[i], randList[j] = randList[j], randList[i]
            elif randList[j] == x:
                t -= 1
                randList[j], randList[t]  = randList[t], randList[j]
                j -= 1
            j += 1
        z = i+1
        k = 0
        while k < r-t+1:
            randList[z+k], randList[t+k] = randList[t+k], randList[z+k]
            k += 1

        #randList[i+1], randList[r] =  randList[r], randList[i+1]
        return [i+1, i+1 + r-t, randList]

#crudeList = [2, 3, 36, 4, 12, 5, 44, 7, 66, 8, 10, 9, 1, 30]
crudeList = [2, 3, 4, 6,3, 6,4, 3]
#crudeList = [2, 3, 4, 6,3, 6,4, 3, 7, 8,2,1 ,7, 9, 3, 4, 6,6, 7, 8, 9, 10,3,5,11,4,5]

start = [0, 1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
finish = [0, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
profit = [0, 3, 2, 6, 2, 5, 4, 4, 3, 4, 11, 2]
special = p[]
algos = Algorithms()
#a, use, j = algos.activitySchedule(start, finish, profit)
a, use, j = algos.activityScheduleSpl(start, finish, profit, special)

print algos.findSolution(a, use, j, len(start)-1)
#print algos.findSolution(a, use, j, len(start)-1)