nums=[]
num=0
while not num==3:
    num+=1
    nums.append(str(input("Вводите числа: ")))
for i in nums:
    print(i)
answer=str(input("Вы хотите оставить последний элэмент в списке?: "))
if answer=="no":
    nums.remove(nums[2])
    print(nums)
