"""
1.DP for the Activity selection problem: Order: O(nlogn)
inputs:
output:
sorted by final
ASP[i] = 0 if i = 0
        max{ ASP[i-1],      if i is not selected 
             P[i]+ ASP[j]   if i is chosen
           j < i, suchthat f[j]<=s[j]  }  

2. DP for actitivity selection when special events are given and no two special events are chosen consecutively
    order: O(n**2)
inputs:
output:
ASP[i] = 0 if i = 0
        P[i] + ASP[j],      if i is forced for selction 
        j < i, suchthat f[j]<=s[j] & !(S[i] and S[j])}  

ASP = max(ASP[i])
     i:1 to n

Note: Do not ever attempt to write a dp unless you are able to recursively see the solution.
      Writing a dp is not hard. The hard part is coming up with a recursive algorithm/ dp that works
      As long you are able to find a recursive solution, the proof of correcness becomes obvious out of it 
"""


class ActivitySelectionDP:
    def activitySchedule(self, start, finish, profit):
        if len(start) != len(finish) != len(profit):
            print "Check the schedule arrays"   
            return [], [], []
        n  = len(start) # total no of events
        activities = [None]*(n)
        activities[0] = 0        
        used = [None]*n #activity used for the problem
        traceBack = [None]*n #js are stored here
        for i in range(1, n):
            activities[i] = activities[i-1]
            used[i] = False
            j = i - 1    
            lower = 0
            upper = j
            #binary search for j in 1 to i-1 events that is compatible with i             
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
        aux, length = [0]*len(start), [0]*len(start) 
        for i in range(1, len(start) ): 
            j = i-1
            while (finish[j] > start[i]) or (special[j] & special[i]) and j > 0: 
                j = j - 1         
            # for j in range (0, i):                           
            if length[i] < profit[i] + length[j]:
                length[i] = profit[i] +length[j]
                aux[i] = j  

        return aux, length

    def findSolution(self, activities, used, trace, special, size):
        
        solution = []      
        while size > 0:
            if used[size] == True:
                solution.append(size)
                size = trace[size]
            else: 
                size -= 1
        profit = activities[solution[0]]
        solution.reverse()

        splStatus = []
        for i, x in enumerate(solution):
            splStatus.append(special[x]) 

        return solution, profit, splStatus

start = [0, 1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
finish = [0, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
profit = [0, 3, 2, 6, 2, 5, 4, 4, 3, 4, 11, 2]
special = [False, True, False, False, True, False, True, True, False, False, True,  True]
# special = [False, False, False, False, False, False, False, False, False, False, False, False]
# special = [True, True, True, True, True, True, True, True, True, True, True, True]
# dummy  =  [ 0,     1,      2,     3,    4,    5,     6,    7,     8,     9,     10,   11]
# a, use, j = algos.activitySchedule(start, finish, profit)
a, use, j = algos.activityScheduleSpl(start, finish, profit, special)




