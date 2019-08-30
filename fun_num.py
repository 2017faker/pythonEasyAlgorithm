from ctypes import *
import time

mod=1000000007
n=int(input())
status=[([0]*(6)) for i in range(n+1)]

status[1][0]=1

for i in range(2,n+1):
    status[i][0]=1
    status[i][1]=(status[i-1][1]*2+status[i-1][0])% mod
    status[i][2]=(status[i - 1][2] + status[i - 1][0]) % mod
    status[i][3] = (status[i - 1][3] * 2 + status[i - 1][1]) % mod
    status[i][4] = (status[i - 1][4] * 2 + status[i - 1][1] + status[i - 1][2]) % mod
    status[i][5] = (status[i - 1][5] * 2 + status[i - 1][3] + status[i - 1][4]) % mod

print(status[n][5])