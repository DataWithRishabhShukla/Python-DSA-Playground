
def naive_solution(lst, n):
    temp = []
    temp.append(lst[0])
    res = 1
    for x in lst[1:]:
        if x != temp[res - 1] :
            temp.append(x)
            res = res + 1
    print(temp)
    
    
ip = [10,20,20,30,40,45,45]
naive_solution(ip,7)