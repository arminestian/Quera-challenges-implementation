n = int(input())
nums = list()

for i in range(n):
    num = input()
    if (len(num) == 12 and num.startswith("98") and num.isdigit()):
        nums.append("+" + num)

    elif (num.startswith("+98") and len(num) == 13):
        num = list(num)
        num.remove("+")
        try:
            num.remove("+")
            nums.append("invalid")
        except:
            num = "".join(num)
            nums.append("+" + num)

    elif (len(num) == 11 and num.startswith("09") and num.isdigit()):
        num = list(num)
        num.remove("0")
        num = "".join(num)
        num = "+98" + num
        nums.append(num)

    else:
        nums.append("invalid")  
           
for i in range(n):
    print(nums[i])   