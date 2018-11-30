import random
guess=int(input('请输入你的数值'))
answer=random.randint(1,10)#单行注释 tab键是提示代码的键
while answer!=guess:
    if answer>guess:
        guess=int(input('小了点'))
    elif answer<guess:
        guess=int(input('大了点'))
print('对了，游戏结束！')
