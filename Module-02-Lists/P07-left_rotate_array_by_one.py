def rotate_list(ip):
    print("\nInput List !!")
    print(ip)
    print("\nUsing Comprehension: Rotating by one !!")
    print(ip[1:]+ip[0:1])

    print("\nUsing Pop: Rotating by one !!")
    ip.append(ip.pop(0))
    print(ip)

rotate_list([10,20,30,40])


def cutom_rotate_logic(ip):
    print("\n\nInside the custom logic !!")
    n = len(ip)
    temp = ip[0]
    for i in range(1,n):
        print(ip)
        print("Rotating :")
        ip[i-1] = ip[i]
        print(ip)
        print("\n")
    ip[n-1] = temp
    print(f"Final List: {ip}")

cutom_rotate_logic([10,20,30,40])