#encoding: utf-8

import random

secret = random.randint(1, 100)
guess = 0
tries = 0

print ("\033[34;1m唔哈！！ 我是可怕的海盗罗伯茨，我有一个秘密！\033[0m")
print ("\033[31;1m这是一个从1到99的数字，我只会给你6次机会。\033[0m")

while guess != secret and tries <6:
    guess = int(raw_input("\033[34;1m你猜这个数是多少?  \033[0m"))
    if guess < secret:
        print ("\033[32;1m太低了，你这只笨狗熊!  \033[0m")
    elif guess > secret:
        print ("\032[34;1m太高了, 你这只笨狗熊!  \033[0m")
    tries = tries +1
if guess == secret:
    print ("\033[32;1m我的上帝！你居然发现了我的秘密!\033[0m")
else:
    print ("\033[32;1m你唯一的机会已被你用完了！伙计!你就是只愚蠢的笨狗熊！\033[0m")
    print ("\033[31;1m还是让我告诉你吧！这个数字是:%s\033[0m" % secret)



'''
功能ok
'''
