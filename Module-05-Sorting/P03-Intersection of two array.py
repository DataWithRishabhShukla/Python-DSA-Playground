
def inetersection_of_array(a,b):
    i, j = 0, 0
    res = []

    while i < len(a) and j < len(b):
        print(f"i: {i}")
        print(f"j: {j}")
        print(f"a[i]: {a[i]}")
        print(f"b[j]: {b[j]}")
        if i > 0 and a[i] == a[i-1]:
            i = i + 1
        elif j > 0 and b[j] == b[j-1]:
            j = j+1
        elif a[i] == b[j]:
            res.append(a[i])
            i +=1
            j +=1
        elif a[i] > b[j]:
            j +=1
        else:
            i += 1
    return res


a = [3,5,10,10,10,15,15,20]
b = [5,10,10,15,30]

print(inetersection_of_array(a,b))

a = [1,1,3,3,3]
b = [1,1,1,1,3,5,6]
print(inetersection_of_array(a,b))