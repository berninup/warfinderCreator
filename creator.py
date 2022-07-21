import itertools
d4 = 2
d6 = 4
d8 = 6
d10 = 8
d12 = 10

pAttk = [d4, d6, d8, d10, d12]
mAttk = [d4, d6, d8, d10, d12]
pDef = [d4, d6, d8, d10, d12]
mDef = [d4, d6, d8, d10, d12]

goodAbility = 1
negAbility = -1
noAbility = 0
abilities1 = [goodAbility, negAbility, noAbility]
abilities2 = [goodAbility, negAbility, noAbility]
abilities3 = [goodAbility, negAbility, noAbility]

hp1 = 2
hp2 = 4
hp3 = 6
hp = [hp1, hp2, hp3]

move1 = 2
move2 = 4
move3 = 6
move  = [move1, move2, move3]

range1 = 2
range2 = 4
range3 = 6
ranged = [range1, range2, range3]

totals = 38
total = 0
card = [
    pAttk, mAttk, pDef, mDef, abilities1, abilities2, abilities3, move, ranged, hp
]

cardList = list(itertools.product(*card))
finalCardList =[]
for unit in cardList:
    for stat in unit:
        
        total = stat + total
    if total == totals | total == totals - 1 | total == totals + 1:
        finalCardList.append(unit)
    
    total = 0
print(len(finalCardList))

for i in range(200):
    print(finalCardList[i])

# card = {
#     pAttk : {d4 : 2, d6 : 4, d8 : 6, d10 : 8, d12 : 10},
#     mAttk : {d4 : 2, d6 : 4, d8 : 6, d10 : 8, d12 : 10},
#     pDef : {d4 : 2, d6 : 4, d8 : 6, d10 : 8, d12 : 10},
#     mDef : {d4 : 2, d6 : 4, d8 : 6, d10 : 8, d12 : 10},
#     hp : {hp1 : 2, hp2 : 4, hp3 : 6},
#     move : {move1 : 2, move2: 4, move3 : 6},
#     ranged : {range1 : 2, range2: 4, range3 : 6},
#     abilities1 : {goodAbility : 1, negAbility : -1, noAbility : 0},
#     abilities2 : {goodAbility : 1, negAbility : -1, noAbility : 0},
#     abilities3 : {goodAbility : 1, negAbility : -1, noAbility : 0}
# }