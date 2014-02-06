#6,8,10|2,7,12
import sys

def merge(leftArr, rightArr):
    outArr = []
    i = 0
    j = 0
    numInv = 0
    while i<len(leftArr) or j < len(rightArr):
        lEl = getOrMax(leftArr, i)
        rEl = getOrMax(rightArr, j)
        if lEl > rEl:
            outArr.append(rEl)
            j = j + 1
        else:
            outArr.append(lEl)
            numInv=numInv + j
            i = i + 1
    return (numInv,outArr)

def getOrMax(arr, ind):
    if(ind < len(arr)):
        return arr[ind]
    else:
        return sys.maxsize

def sortAndCalc(arr):
    if(len(arr)==1):
        return (0, arr)
    m = len(arr) // 2
    lA = arr[0:m]
    numInvL, lA = sortAndCalc(lA)
    rA = arr[m:len(arr)]
    numInvR, rA = sortAndCalc(rA)
    numInvCross, arr = merge(lA, rA)
    return (numInvL + numInvR + numInvCross, arr)
    

lA = [6, 8, 10, 15, 18, 23]
rA = [2, 7, 12, 13, 14, 20, 21, 24]
oA = []

mArr = [8, 6, 12, 2, 7, 11]
numInv, mArr = sortAndCalc(mArr)
print(numInv)
print(mArr)            

    