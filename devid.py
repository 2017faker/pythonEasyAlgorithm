import time

def devide(ma,mi,xtuple,left,right):
    if(left>right):
        return
    elif(left==right):
        ma[0]=max(ma[0],xtuple[left])
        mi[0]=min(mi[0],xtuple[left])
        return
    elif(right-left==1):
        if(xtuple[left]>xtuple[right]):
            ma[0]=max(ma[0],xtuple[left])
            mi[0]=min(mi[0],xtuple[right])
            return
        else:
            ma[0]=max(ma[0],xtuple[right])
            mi[0]=min(mi[0],xtuple[left])
            return

    devide(ma,mi,xtuple,(left+right)//2+1,right)
    devide(ma,mi,xtuple,left,(left+right)//2)



print("请输入数组，以,分隔数组中元素")
xlist=input()
xlist=xlist.split(",")
xlist=[int(xlist[i]) for i in range(len(xlist))]
xtuple=tuple(xlist)

mi=[99999999]
ma=[-999999]

begin=time.clock()

devide(ma,mi,xtuple,0,len(xtuple)-1)

end=time.clock()

sumtime=end-begin

print("最大值为:%i"%ma[0])
print("最小值为:%i"%mi[0])
print("查找最大最小所用时间为:%f s"%sumtime)