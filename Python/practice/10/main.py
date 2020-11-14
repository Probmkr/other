import random

# 出拳
punches = ['石头','剪刀','布']
computer_choice = random.choice(punches)
user_choice = ''

# 亮拳
print('————战斗过程————')
print('你出了%s，电脑出了%s，' % (user_choice,computer_choice))