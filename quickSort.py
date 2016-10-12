    
"""
Procedure for quicksort using randomized partition
randomizedPartition: generalized algorithm, assumes the elements are distinct
randomizePartAdvanced: which considers equal elements and give a partioned array with
                       equal elements from <x, q...=x..t, >x
"""
import random    
class quickSort:
    def quickSortAlgorithm(self, randList, p, r):
        if p >= r: return randList
        q, t, randList = self.randomizedPartAdvanced(randList, p, r)
        self.quickSort(randList, p, q-1)
        self.quickSort(randList, t+1, r)
        return randList

    def randomizedPartition(self, array, p, r):
        q = random.randint(p,r)
        x = array[q]#pivot element
        array[q], array[r] =  array[r], array[q]
        i = p-1
        for j in range(p, r):
            if array[j]  < x:
                i = i + 1
                array[j], array[i] = array[i], array[j]
        array[i+1], array[r] = array[r], array[i+1]
        return i+1 #, array # should we return            


    #This method outputs two indices: q, t. 
    #the elements from q to t are equal and right of t are larger and left of q are smaller
    def randomizedPartAdvanced(self, array, p, r):
        rand = random.randint(p,r)
        x = array[rand]#pivot element
        array[q], array[p] =  array[p], array[q]
        q, t = p, p
        for j in range(p+1, r+1):
            if array[j] < x:
                tmp = array[q]
                array[q] = array[j]
                array[j]= array[t+1]
                array[t+1] = tmp
                q, t += 1, 1
            elif array[j] == x:
                array[t+1], array[j] = array[j], array[t+1]
                t += 1
        return q, t


qs = quickSort()
crudeList = [2, 3, 4, 6,3, 6,4, 3, 7, 8,2,1 ,7, 9, 3, 4, 6,6, 7, 8, 9, 10,3,5,11,4,5] # for QuickSort

print qs.quickSortAlgorithm(crudeList)