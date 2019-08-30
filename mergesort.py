import time
def ms(arr,left,right):
    if(left>=right):
        return
    elif(right-left==1):
        if(arr[left]>arr[right]):
            k=arr[left]
            arr[left]=arr[right]
            arr[right]=k
    else:
        i = (left + right) // 2 + 1
        j = (left + right) // 2
        ms(arr,left,j)
        ms(arr, i, right)
        lf=left
        ri=right
        temp=[]

        while(True):
            if(i<=right ):
                if(lf == j+1):
                    temp.append(arr[i])
                    i = i + 1
                elif(arr[i]<arr[lf]):
                    temp.append(arr[i])
                    i=i+1
                else:
                    temp.append(arr[lf])
                    lf=lf+1
            else:
                temp.append(arr[lf])
                lf = lf + 1
            if(i==right+1 and lf==j+1):
                break

        for num in range(len(temp)):
            arr[left] = int(temp[num])
            left = left + 1


print("请输入数组，数组数据以“,”分割")
arr=input()
arr=arr.split(",")
arr=[int(arr[i]) for i in range(len(arr))]

begin=time.clock()
ms(arr,0,len(arr)-1)
end=time.clock()
print(arr)

print("归并排序时间是:%f s"%(end-begin))
