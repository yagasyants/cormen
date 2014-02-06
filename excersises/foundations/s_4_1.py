
def findDeal(arr):
    bestMinInd = 0
    bestMaxInd = 0
    minInd = 0
    for i in range(1, len(arr)):
        currDeal = arr[bestMaxInd] - arr[bestMinInd]
        val = arr[i]
        if(val > arr[minInd]):
            newDeal = val - arr[minInd]
            if(newDeal > currDeal):
                bestMinInd = minInd
                bestMaxInd = i
        elif (val<arr[minInd]):
            minInd=i

    currDeal = arr[bestMaxInd] - arr[bestMinInd]
    return (currDeal, bestMinInd, bestMaxInd)

arr = [100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97]
#arr = [20,10,2,3,4,7,3,25,13]

print(findDeal(arr))