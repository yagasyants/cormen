arr = [31, 41, 59, 26, 41,  58]

for j in reversed(range(len(arr)-1)):
    elem = arr[j]
    i = j + 1
    while i < len(arr) and arr[i] > elem:
        arr[i-1] = arr[i]
        i = i + 1
    arr[i-1] = elem
    print(arr)
        
print(arr)
