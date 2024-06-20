lst = [10,20,30,40,51]
print(lst[0])
print(lst[1])
print(lst[-1])
print(lst[-2])


print(f"Mean is: {sum(lst)/len(lst)}")
print(f"Even Pos List: {[lst[x] for x in range(0,len(lst),2)]}")
print(f"Odd  Pos List: {[lst[x] for x in range(1,len(lst),2)]}")
print(f"Even Ele List: {[x for x in lst if x%2==0]}")
print(f"Odd  Ele List: {[x for x in lst if x%2!=0]}")

def find_smaller(ip_lst:list, small_ele:int):
    return [element for element in ip_lst if element < small_ele]

print(find_smaller(lst,43))

lst = [10,20,30,40,51]
print(lst[:2:-1])