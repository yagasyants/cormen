
def add(a, b):
    m = 0
    c = []
    for i in reversed(range(len(a))) :
        aEl = a[i]
        bEl = b[i]
        sumEl = aEl + bEl + m
        if sumEl <= 1 :
            c.insert(0, sumEl)
            m = 0
        elif sumEl == 2 :
            c.insert(0, 0)
            m = 1
        else :
            c.insert(0, 1)
            m = 1
    c.insert(0, m)       
    return c
    
a1 = [1, 1, 1, 1]
b1 = [1, 0, 0, 1]

c1 = add(a1, b1)

print(c1)