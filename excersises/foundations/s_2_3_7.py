def biSechHelp(arr, x, s, e):
    if (e==s):
        if(x==arr[s]):
            return s
        else:
            return -1
    else:
        diff = e - s
        delim = s + diff // 2
        valDelim = arr[delim]
        if (x > valDelim):
            return biSechHelp(arr, x, delim + 1, e)
        elif (x==valDelim):
            return delim
        else:
            return biSechHelp(arr, x, s, delim - 1)
 
def biSech(arr, x):
    return biSechHelp(arr, x, 0, len(arr) - 1)
              
def findSum(arr, x):
    arr.sort()
    for el in arr :
        if (el > x) :
            return None
        rem = x - el
        ind = biSech(arr, rem)
        if(ind > 0):
            return [el, rem]
    return None

myArr = [1, 2, 3, 4, 5, 10]
val = biSech(myArr, 0)
print(val)        