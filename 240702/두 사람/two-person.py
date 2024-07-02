p1 = input().split()
p2 = input().split()

a = int(p1[0])
b = str(p1[1])
c = int(p2[0])
d = str(p2[1])


if (a>=19 and b == "M") or (c>=19 and d == "M") :
    print(1)
else :
    print(0)