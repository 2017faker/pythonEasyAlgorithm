import time
import queue
def swap(queue,point,i,j):
    k = queue[i]
    queue[i] = queue[j]
    queue[j] = k

    k = point[i]
    point[i] = point[j]
    point[j] = k

def my_sort(queue,point):
    for i in range(len(queue)):
        for j in range(i+1,len(queue)):
            if(queue[i]>queue[j]):
                swap(queue,point,i,j)


n=int(input("请输入矩阵大小"))
matric=[[0]*n for i in range(n)]
the_point=[]
the_queue=[]
the_end=[]
thr_endpoint=[]
print("请输入矩阵，无相邻边则用-1表示")
for i in range(n):
    matric[i]=input().split(' ')
    matric[i]=[int(matric[i][j]) for j in range(n)]

first=int(input("请输入起始点"))

for i in range(n):
    if(matric[first-1][i]>0):
        the_queue.append(matric[first-1][i])
        the_point.append(i)
my_sort(the_queue,the_point)


while(len(the_queue)!=0):
    the_end.append(the_queue[0])
    thr_endpoint.append(the_point[0]+1)
    if(len(the_queue)==1):
        break

    for i in range(n):
        if(matric[the_point[0]][i]>0):
            flag=-1
            for j in range(1,len(the_point)):
                if(the_point[j]==i):
                    if(the_queue[j]<=the_queue[0]+matric[the_point[0]][i]):
                        flag=0
                        break
                    else:
                        flag=j
                        break
            if(flag==0):
                break
            elif(flag==j):
                the_point[j]=i
                the_queue[j]=the_queue[0]+matric[the_point[0]][i]
            else:
                the_point.append(i)
                the_queue.append(matric[the_point[0]][i])

    the_point.remove(the_point[0])
    the_queue.remove(the_queue[0])
    my_sort(the_queue,the_point)

print(thr_endpoint)
print(the_end)
print(matric)

# 0 4 2 5 -1 -1 -1 -1 -1 -1
# -1 0 -1 -1 7 5 -1 -1 -1 -1
# -1 -1 0 -1 -1 9 -1 -1 -1 -1

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