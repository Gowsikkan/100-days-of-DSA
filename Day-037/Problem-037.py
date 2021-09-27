def twosum(num,target):
    x=[]
    for i in range(len(num)):
        for j in range(len(num)):
            if i!=j:
                if num[i]+num[j]==target:
                    x.append([i,j])
        break
    return x

a=int(input("enter the size of st2ring"))
num=[]
for i in range(a):
    b=int(input("enter the value"))
    num.append(b)
target=int(input("enter the target num"))
x=twosum(num,target)
print(x)
