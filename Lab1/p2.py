print("Prime checker")
x = int(input())

if x <= 1:
    print("no")
else:
    q = x
    q %= 2
    if q == 0:
        if x == 2:
            print("yes")
        else:
            print("no")
    else:
        d = 3
        f = False
        dd = d
        dd *= d
        while dd <= x and not f:
            q = x
            q %= d
            if q == 0:
                print("no")
                f = True
            d += 2
            dd = d
            dd *= d
        if not f:
            print("yes")

