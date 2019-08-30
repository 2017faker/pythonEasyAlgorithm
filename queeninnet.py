import time

def conflict(state, col):
    # 冲突函数，row为行，col为列
    row = len(state)
    for i in range(row):
        if abs(state[i] - col) in (0, row - i):
            return True
    return False

def queens(num=8, state=()):
    # 生成器函数
    for pos in range(1,num+1):
        if not conflict(state, pos):
            if len(state) == num - 1:
                yield (pos,)
            else:
                for result in queens(num, state + (pos,)):
                    yield (pos,) + result

begin=time.clock()
for solution in list(queens(8)):
    print(solution)
end=time.clock()
print('  total number is ' + str(len(list(queens()))))
print('the time is %f s' %(end-begin))