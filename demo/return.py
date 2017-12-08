''' 
R  skill1 skill2
D  damage1 damage2
'''

def damage(skill1,skill2):
    damage1 = skill1 * 3
    damage2 = skill2 * 2 + 10
    return damage1,damage2

# 序列解包
skill1_damages,skill2_damages = damage(3,6)

print(skill1_damages,skill2_damages)
# print(damages,type(damages))