import random

#决定随机数大小范围
start = input('请输入随机数范围上界:')
end = input('请输入随机数范围下界:')
start = int(start)
end = int(end)
r = random.randint(start, end)

times = 1

#猜数环节！
while 1 :
    times = times + 1
    g = input('猜一个数字:')
    g = int(g)
    if r == g:
        if times <= 10:
            print('哇哦!', times, '次就猜对了呢，快去领取奖励吧！')
        else:
            print('猜了', times, '次猜对了呢，下次再接再励噢！')
        break
    elif r < g:
        print('比这个数小噢')
    else:
        print('比这个数大噢')




        

