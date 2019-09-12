import random
r = random.randint(1,100)
times = 1

while 1 :
    times = times + 1
    g = input('猜一个1到100的数字:')
    g = int(g)
    if r == g:
        print('哇哦!', times, '次就猜对了呢，快去领取奖励吧！')
        break
    elif r < g:
        print('比这个数小噢')
    else:
        print('比这个数大噢')




        

