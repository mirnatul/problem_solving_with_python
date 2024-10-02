x = 10
xStr = list(str(x))
newxStr = xStr.copy()
newxStr.reverse()

if xStr == newxStr:
    print("true")
else:
    print("false")