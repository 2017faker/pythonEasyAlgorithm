import time
import queue
import operator
class my_queue:
    def __init__(self,value,point):
        self.value=value
        self.point=point
        return
    def __lt__(self, other):
        return self.value<other.value
    def __cmp__(self, other):
        return operator.lt(self.value,other.value)


n=int(input("请输入矩阵大小"))
matric=[[0]*n for i in range(n)]
the_end=[]
thr_endpoint=[]
maked=[0]*n
print("请输入矩阵，无相邻边则用-1表示")
for i in range(n):
    matric[i]=input().split(' ')
    matric[i]=[int(matric[i][j]) for j in range(n)]

first=int(input("请输入起始点"))
begin=time.clock()
q=queue.PriorityQueue()
for i in range(n):
    if(matric[first-1][i]>0):
        f=matric[first-1][i]
        q.put(my_queue(f,i))
maked[first-1]=1
while(not q.empty()):
    my_new=q.get()
    if(maked[my_new.point]==0):
        the_end.append(my_new.value)
        thr_endpoint.append(my_new.point)
        maked[my_new.point]=1
    if(q.empty()):
        break
    x=len(the_end)
    for i in range(n):
        if(matric[thr_endpoint[x-1]][i]>0):
            if(maked[i]==1):
                continue
            q.put(my_queue(my_new.value+matric[thr_endpoint[x-1]][i],i))

end=time.clock()

for i in range(len(thr_endpoint)):
    print(first,"到",thr_endpoint[i]+1,"的最短路径为",the_end[i])

print("时间为:%f s"%(end-begin))


# 0 4 2 5 -1 -1 -1 -1 -1 -1
# -1 0 -1 -1 7 5 -1 -1 -1 -1
# -1 -1 0 -1 -1 9 -1 -1 -1 -1
# -1 -1 -1 0 2 -1 7 -1 -1 -1
# -1 -1 -1 -1 0 -1 -1 4 -1 -1
# -1 -1 -1 -1 -1 0 -1 -1 -1 6
# -1 -1 -1 -1 -1 -1 0 -1 3 -1
# -1 -1 -1 -1 -1 -1 -1 0 -1 7
# -1 -1 -1 -1 -1 -1 -1 -1 0 8
# -1 -1 -1 -1 -1 -1 -1 -1 -1 0