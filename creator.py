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
aim = 1
polearms = 2
invisible = 2
stagger = -2
weakArms = -1
abilities1 = [goodAbility, negAbility, noAbility, aim, invisible, stagger]
abilities2 = [goodAbility, negAbility, noAbility, polearms, weakArms]
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

tier1Total = 22
tier2Total = 30
tier3Total = 38
total = 0
card = [
    pAttk, mAttk, pDef, mDef, abilities1, abilities2, abilities3, move, ranged, hp
]



cardList = list(itertools.product(*card))

tier1CommonCardList = []
tier1UncommonCardList = []
tier1RareCardList = []
tier2CommonCardList = []
tier2UncommonCardList = []
tier2RareCardList = []
tier3CommonCardList = []
tier3UncommonCardList = []
tier3RareCardList = []

for unit in cardList:
    for stat in unit:
        
        total = stat + total
    if total == tier1Total - 1:
        tier1CommonCardList.append(unit)
    if total == tier1Total:
        tier1UncommonCardList.append(unit)
    if total == tier1Total + 1:
        tier1RareCardList.append(unit)
    if total == tier2Total - 1:
        tier2CommonCardList.append(unit)
    if total == tier2Total:
        tier2UncommonCardList.append(unit)
    if total == tier2Total + 1:
        tier2RareCardList.append(unit)
    if total == tier3Total - 1:
        tier3CommonCardList.append(unit)
    if total == tier3Total:
        tier3UncommonCardList.append(unit)
    if total == tier3Total + 1:
        tier3RareCardList.append(unit)
    
    total = 0


print("Tier 1 Common Cards: " )
print(len(tier1CommonCardList))
print("Tier 1 Uncommon Cards: " )
print(len(tier1UncommonCardList))
print("Tier 1 Rare Cards: " )
print(len(tier1RareCardList))

print("Tier 2 Common Cards: " )
print(len(tier2CommonCardList))
print("Tier 2 Uncommon Cards: " )
print(len(tier2UncommonCardList))
print("Tier 2 Rare Cards: " )
print(len(tier2RareCardList))

print("Tier 3 Common Cards: " )
print(len(tier3CommonCardList))
print("Tier 3 Uncommon Cards: " )
print(len(tier3UncommonCardList))
print("Tier 3 Rare Cards: " )
print(len(tier3RareCardList))

totalCards = len(tier1CommonCardList) + len(tier1UncommonCardList) + len(tier1RareCardList) + len(tier2CommonCardList) + len(tier2UncommonCardList) + len(tier2RareCardList) + len(tier3CommonCardList) + len(tier3UncommonCardList) + len(tier3RareCardList)
print("Total Cards")
print(totalCards)



for i in range(len(tier1CommonCardList)):
    print(tier1CommonCardList[i])

