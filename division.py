def update(i,val,n,tree):
    while(i<=n):
        tree[i]=tree[i]+val
        i=i+(-i & i)


def getsum(i,tree):
    sum=0
    while(i>0):
        sum=sum+tree[i]
        i=i-(-i & i)
    return sum

n=int(input("请输入数的个数"))
m=int(input("请输入执行次数"))

tree=[0]*101024
a=[0]
b=input().split(' ')
for i in range(1,n+1):
    a.append(int(b[i-1]))
    update(i,a[i],n,tree)

for i in range(1,m+1):

    ord=input().split(' ')
    l=int(ord[1])
    r=int(ord[2])

    if(len(ord)==3):
        print(getsum(r,tree)-getsum(l-1,tree))
    else:
        w=int(ord[3])
        if(w==1):
            continue
        while(l<=r):
            if(a[l]>=w and a[l]%w==0):
                update(l,-(a[l]-a[l]//w),n,tree)
                a[l]=a[l]//w
            l=l+1

