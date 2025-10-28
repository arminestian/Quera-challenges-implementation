CM, GM = map(int, input().split())
CS, GS = map(int, input().split())
rate = int(input())

if CS > CM:
    need = (CS - CM)
    if need % rate == 0:
        GM -= need // rate
        CM +=( need // rate) * rate
    else:
        GM -= (need // rate) + 1
        CM += ((need // rate) + 1) * rate
        
if GS > GM:
    need = GS - GM
    CM -= need * rate
    GM += need
        
if CM >= CS and GM >= GS:
    print("Yes")
else:
    print("No")