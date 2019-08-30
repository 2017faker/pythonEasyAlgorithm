import time
n=int(input())
count=input().split(' ')
count=[int(count[i]) for i in range(n)]

zw=[([0]*5) for i in range(20)]

for k in range(n):
    flag=0
    for i in range(20):
        flag=0
        num=-1
        for j in range(5):
            if(zw[i][j]==0):
                flag=flag+1
            elif(zw[i][j]==1 and flag!=0):
                break
            if(flag==count[k]):
                num=flag
                break
        if(num!=-1):
            for j in range(5):
                if(zw[i][j]==0):
                    zw[i][j]=1
                    num=num-1
                    print((i+1)*10+j+1,end=' ')
                if(num==0):
                    print()
                    break
            break


    if(flag==0):
        num=count[k]
        for i in range(20):
            for j in range(5):
                if(zw[i][j]==0):
                    zw[i][j]=1
                    print((i+1)*10+j+1,end=' ')
                    num=num-1
                if(num==0):
                    print()
                    break
            if(num==0):
                break