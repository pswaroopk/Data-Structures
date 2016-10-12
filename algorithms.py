
import random
import math
def getRandInt(i, j):
    return random.randint(i, j)

class Algorithms(object):
    
    #incorrect appproach
     def activityScheduleSpl(self, start, finish, profit, special):
        if len(start) != len(finish) != len(profit):
            print "Check the schedule arrays"   
            return [], [], []
        n  = len(start) # total no of events
        activities, used, trace = [None]*(n),  [None]*(n),  [None]*(n)      
        activities[0] = 0      
        # used = [None]*n #activity used for the problem
        # traceBack = [None]*n #js are stored here
        for i in range(1, n):
            isSpl = special[i]
            activities[i] = activities[i-1]
            used[i] = False
            j = i - 1    

            ''''Linear Search for j'''
            while finish[j] > start[i]:
                j = j-1     

            trace[i] = k = j
            while used[k]:
                k = trace[k]
            if special[k] & special[i]:     
                k = k-1
            if special[j]:
                k-=1    
        return activities, used, traceBack
    

algos = Algorithms()


# print algos.findSolution(a, use, j, special, len(start)-1)
# print algos.findSolution(a, use, j, len(start)-1)