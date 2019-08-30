import time
print("请输入背包大小")
pack_V=int(input())
print("请输入每个物品的重量,以空格分隔每个大小")
each_hight=input()
each_hight=each_hight.split(" ")
each_hight=[int(each_hight[i]) for i in range(len(each_hight))]

print("请输入每个物品的价值,以空格分隔每个大小")
each_val=input()
each_val=each_val.split(" ")
each_val=[int(each_val[i]) for i in range(len(each_val))]


begin=time.clock()
each_new=[]

pack_V=pack_V+1
for i in range(pack_V):
    each_new+="0"

each_new=[int(each_new[i]) for i in range(len(each_new))]

for i in range(len(each_hight)):
    newv=pack_V-1
    while(newv>=each_hight[i]):
        each_new[newv]=max(each_new[newv],each_new[newv-each_hight[i]]+each_val[i])
        newv=newv-1


end=time.clock()
alltime=end-begin
print("最大价值为：",each_new[pack_V-1])
print("算法所需时间为 %f s"%alltime)

