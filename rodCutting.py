
class RodCuttingProblem(object):
    
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
        
        A, R = self.getRevenueSubArray(pList)
        maxVal = R[-1]
        sizes = []
        rodSize = len(pList)
        while 
            sizes.append(A[i])
            
        
        