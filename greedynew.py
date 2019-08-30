import time
def swap(a1,a2,i,j):
    k = a1[i]
    a1[i] = a2[j]
    a2[j] = k

print("请输入背包大小")
pack=int(input())
print("请输入物品的大小，以空格分离")
each_hi=input()
each_hi=each_hi.split(" ")
each_hi=[int(each_hi[i]) for i in range(len(each_hi))]

print("请输入物品的价值，以空格分离")
each_va=input()
each_va=each_va.split(" ")
each_va=[int(each_va[i]) for i in range(len(each_va))]

begin=time.clock()
unitva=[float(each_va[i]/each_hi[i]) for i in range(len(each_hi))]

for i in range(len(unitva)):
    for j in range(i+1,len(unitva)):
        if(unitva[i]<unitva[j]):
            swap(each_va,each_va,i,j)
            swap(each_hi,each_hi,i,j)
            swap(unitva,unitva,i,j)

sum=0
for i in range(len(each_hi)):
    if(each_hi[i]<=pack):
        pack=pack-each_hi[i]
        sum=sum+each_va[i]
    else:
        k=pack*unitva[i]
        sum=sum+k
        break
end=time.clock()
alltime=end-begin

print("最高总价值为：",sum)
print("时间为:%f s"%alltime)