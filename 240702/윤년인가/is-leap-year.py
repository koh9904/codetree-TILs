y = int(input())

if y%4 == 0 :
    if y%100 == 0 or y%400 == 1 :
        print("false")
    else :
        print("true")
else :
    print("false")