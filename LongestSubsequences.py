class LongSubsequences:
    def findLMSequence(self, array):        
        size = len(array)
        aux = [None]*size
        length = [None]*size        
        aux [0]=0
        length[0]=0
        for i in range(1, size):     
            lst = [(0, 0)]*i
            lst[0] = (0, 0)
            for j in range (0, i):                           
                if array[j] <= array[i]:
                    lst.append((j, 1+length[j]))
            # lis,key=itemgetter(1)
            from operator import itemgetter
            index, cnt = max(lst, key=itemgetter(1))
            # index, cnt = max(lst, key=lambda item:item[1])
            length[i] = cnt
            aux[i] = index
        return aux, length
        
    def findAMSequence(self, array):        
        size = len(array)
        aux = [None]*size
        length = [None]*size        
        aux [0]=0
        length[0]=0
        for i in range(1, size):     
            lst = [(0, 0)]*i
            lst[0] = (0, 0)
            prev = array[i]
            for j in range (i-1, -1, -1):                                         
                if array[j] <= array[i]:
                    a = prev%2
                    b = array[j]%2
                    if (prev%2 != array[j]%2):                        
                        prev = array[j]
                        lst.append((j, 1+length[j]))
            # index, cnt = max(lst, key=lambda item:item[1])
            from operator import itemgetter
            index, cnt = max(lst, key=itemgetter(1))
            length[i] = cnt
            aux[i] = index
        return aux, length
    
    def findLMSequence1(self, array):
        aux, length = [0]*len(array), [0]*len(array) 
        for i in range(1, len(array) ):  
            for j in range (0, i):                           
                if (array[j] <= array[i]) & (length[i] < 1+length[j]):
                    length[i] = 1 +length[j]
                    aux[i] = j           
        return aux, length

    def findAMSequence1(self, array):        
        size = len(array)
        aux, length = [0]*size, [0]*size 
        for i in range(1, size): 
            prev = array[i]
            for j in range (i-1, -1, -1):                                         
                if array[j] <= array[i]:
                    if (prev%2 != array[j]%2) & (length[i] < 1 + length[j]):
                        length[i] = 1 + length[j]
                        aux[i] = j
                        prev = array[j]                       
        return aux, length
    def findLMSSolution(self, array):           
        aux, length = algos.findLMSequence1(array)    
        # aux, length = algos.findAMSequence1(array)   
        size = len(array)-1
        index, cnt = 0, 0
        while size > 0:
            if cnt < length[size]:
                cnt = length[size]                
                index = size      
            size -= 1
        subArray = []
        while index > 0:
            subArray.append(array[index])
            index = aux[index] 
        subArray.reverse()
        return subArray, len(subArray)


# sequence = [0, 7, 9, 12, 3, 5, 6, 8, 4, 15, 9]
# testSequence = [0, 3, 5, 6, 8, 9, 10, 12, 13, 15, 16]
# t2Seq = [0, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# print algos.findLMSSolution(sequence)