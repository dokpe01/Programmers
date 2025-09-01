def solution(bandage, health, attacks):
    cnt = 0
    max_hp = health
    for i in range((attacks[-1][0])+1):
        if i == attacks[0][0]:
            health -= attacks[0][1]
            attacks.pop(0)
            cnt = 0
            if health <= 0:
                return -1
        else:
            cnt += 1
            health += bandage[1]
            if health > max_hp:
                health = max_hp
            if cnt >= bandage[0]:
                health += bandage[2]
                if health > max_hp:
                    health = max_hp
                cnt = 0
    return health