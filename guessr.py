import random
r = random.randint(1,100)

while 1 :
    g = input('猜一个1到100的数字:')
    g = int(g)
    if r == g:
        print('猜对啦，快去领取奖励吧！')
        break
    elif r < g:
        print('比这个数小噢')
    else:
        print('比这个数大噢')




        

