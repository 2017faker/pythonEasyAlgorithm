import time
import random

def swap(num,i,j):
    k=num[i]
    num[i]=num[j]
    num[j]=k

def select(num):
    l=0
    r=len(num)-1
    if(len(num)%2==0):
        k=len(num)//2
    else:
        k=len(num)//2+1
    while(True):
        if(l>=r):
            return num[l]
        i=l
        j=l+random.randint(1, r-l)
        current = num[l]
        swap(num, i, j)
        j=r
        while(True):
            while(num[i]<current):
                i=i+1
            while(num[j]>current):
                j=j-1
            if(i>=j):
                break
            swap(num,i,j)

        if(j-l+1==k):
            return current

        if(j-l+1<k):
            k=k-j+l-1
            l=j+1
        else:
            r=j-1



print("请输入数组")
begin=time.clock()
num=input().split(' ')
n=len(num)
num=[int(num[i]) for i in range(n)]
a=select((num))
end=time.clock()
print("中值为",a)
print("时间为：%f s"%(end-begin))

# 7 28 9 0 32 45          9
# 33 5 0 1 32 77 43               32
# 46 19 59 0 43 -23 549 349 119 3 6                  43