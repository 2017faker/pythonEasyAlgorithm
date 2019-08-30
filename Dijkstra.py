import time

# def dijkstra(matric,fisrt,flag,n,end):
#     mi=999999
#     k=0
#     for i in range(n):
#         if(flag[i]!=1):
#             if(end[i]<mi):
#                 mi=end[i]
#                 k=i
#
#     flag[k]=1
#     for i in range(n):
#         if(flag[i]!=1):
#             end[i]=min(matric[k][i]+end[k],end[i])


n=int(input("请输入矩阵大小"))
matric=[[0]*n for i in range(n)]
flag=[0]*n
end=[999999]*n
# father=[0]*n
print("请输入矩阵，无相邻边则用-1表示")
for i in range(n):
    matric[i]=input().split(' ')
    matric[i]=[int(matric[i][j]) for j in range(n)]

first=int(input("请输入首结点"))
for i in range(n):
    if(matric[first-1][i]!=-1):
        end[i]=matric[first-1][i]
        # father[i]=first

begin=time.clock()
flag[first-1]=1

# dijkstra(matric,first,flag,n,end)

count=0
while(count!=n):
    mi=999999
    k=0
    for i in range(n):
        if(flag[i]!=1):
            if(end[i]<mi):
                mi=end[i]
                k=i

    flag[k]=1
    for i in range(n):
        if(flag[i]!=1 and matric[k][i]!=-1):
            # end[i]=min(matric[k][i]+end[k],end[i])
            if(matric[k][i]+end[k]<end[i]):
                end[i]=matric[k][i]
                # father[i]=k
    count=count+1

endti=time.clock()
for i in range(n):
    if(i+1==first):
        continue
    if(end[i]!=999999):
        print(first,"到第",(i+1),"点最近距离为",end[i])
        # fak=i
        # print("路径为:",i,"<- ",end='')
        # while(True):
        #     if(father[fak]==first-1):
        #         print(first)
        #         break
        #     else:
        #         print(father[fak]+1,"<- ",end='')
        #         fak=father[fak]

    else:
        print(first,"到第",(i+1),"点最近距离为无穷")
print('the time is %f s' %(endti-begin))
