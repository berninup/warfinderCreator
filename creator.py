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

majorPositiveAbility = 2
minorPositiveAbility = 1
minorNegativeAbility = -1
majorNegativeAbility = -2
noAbility = 0

abilities1 = [majorPositiveAbility, minorPositiveAbility, noAbility, minorNegativeAbility, majorNegativeAbility]
abilities2 = [majorPositiveAbility, minorPositiveAbility, noAbility, minorNegativeAbility, majorNegativeAbility]
abilities3 = [majorPositiveAbility, minorPositiveAbility, noAbility, minorNegativeAbility, majorNegativeAbility]

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

tier1Total = 26
tier2Total = 34
tier3Total = 42
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


# print("Tier 1 Common Cards: " )
# print(len(tier1CommonCardList))
# print("Tier 1 Uncommon Cards: " )
# print(len(tier1UncommonCardList))
# print("Tier 1 Rare Cards: " )
# print(len(tier1RareCardList))

# print("Tier 2 Common Cards: " )
# print(len(tier2CommonCardList))
# print("Tier 2 Uncommon Cards: " )
# print(len(tier2UncommonCardList))
# print("Tier 2 Rare Cards: " )
# print(len(tier2RareCardList))

# print("Tier 3 Common Cards: " )
# print(len(tier3CommonCardList))
# print("Tier 3 Uncommon Cards: " )
# print(len(tier3UncommonCardList))
# print("Tier 3 Rare Cards: " )
# print(len(tier3RareCardList))

# totalCards = len(tier1CommonCardList) + len(tier1UncommonCardList) + len(tier1RareCardList) + len(tier2CommonCardList) + len(tier2UncommonCardList) + len(tier2RareCardList) + len(tier3CommonCardList) + len(tier3UncommonCardList) + len(tier3RareCardList)
# print("Total Cards")
# print(totalCards)



# for i in range(len(tier1CommonCardList)):
#     print(tier1CommonCardList[i])

completeTier1CommonCardList = []
completeTier1UncommonCardList = []
completeTier1RareCardList = []
# cardDataList = []

# def cardDataFunction(cardList, tier, rarity):
    
#     for cardData in cardList:
#         newCardDataList = list(cardData)
#     if newCardDataList[0] == 2:
#         newCardDataList[0] = 'D4'
#     if newCardDataList[0] == 4:
#         newCardDataList[0] = 'D6'
#     if newCardDataList[0] == 6:
#         newCardDataList[0] = 'D8'
#     if newCardDataList[0] == 8:
#         newCardDataList[0] = 'D10'
#     if newCardDataList[0] == 10:
#         newCardDataList[0] = 'D12'
#     if newCardDataList[1] == 2:
#         newCardDataList[1] = 'D4'
#     if newCardDataList[1] == 4:
#         newCardDataList[1] = 'D6'
#     if newCardDataList[1] == 6:
#         newCardDataList[1] = 'D8'
#     if newCardDataList[1] == 8:
#         newCardDataList[1] = 'D10'
#     if newCardDataList[1] == 10:
#         newCardDataList[1] = 'D12'
#     if newCardDataList[2] == 2:
#         newCardDataList[2] = 'D4'
#     if newCardDataList[2] == 4:
#         newCardDataList[2] = 'D6'
#     if newCardDataList[2] == 6:
#         newCardDataList[2] = 'D8'
#     if newCardDataList[2] == 8:
#         newCardDataList[2] = 'D10'
#     if newCardDataList[2] == 10:
#         newCardDataList[2] = 'D12'
#     if newCardDataList[3] == 2:
#         newCardDataList[3] = 'D4'
#     if newCardDataList[3] == 4:
#         newCardDataList[3] = 'D6'
#     if newCardDataList[3] == 6:
#         newCardDataList[3] = 'D8'
#     if newCardDataList[3] == 8:
#         newCardDataList[3] = 'D10'
#     if newCardDataList[3] == 10:
#         newCardDataList[3] = 'D12'
#     if newCardDataList[4] == 0:
#         newCardDataList[5] = 'No Ability'
#         newCardDataList[6] = 'No Ability'
#         newCardDataList[4] = 'No Ability'
#     if newCardDataList[5] == 0:
#         newCardDataList[5] = 'No Ability'
#         newCardDataList[6] = 'No Ability'
#     if newCardDataList[6] == 0:
#         newCardDataList[6] = 'No Ability'        
#     if newCardDataList[4] == 1:
#         newCardDataList[4] = 'Minor Positive Ability'
#     if newCardDataList[4] == 2:
#         newCardDataList[4] = 'Major Positive Ability'
#     if newCardDataList[4] == -1:
#         newCardDataList[4] = 'Minor Negative Ability'
#     if newCardDataList[4] == -2:
#         newCardDataList[4] = 'Major Negative Ability'
#     if newCardDataList[5] == 1:
#         newCardDataList[5] = 'Minor Positive Ability'
#     if newCardDataList[5] == 2:
#         newCardDataList[5] = 'Major Positive Ability'
#     if newCardDataList[5] == -1:
#         newCardDataList[5] = 'Minor Negative Ability'
#     if newCardDataList[5] == -2:
#         newCardDataList[5] = 'Major Negative Ability'
#     if newCardDataList[6] == 1:
#         newCardDataList[6] = 'Minor Positive Ability'
#     if newCardDataList[6] == 2:
#         newCardDataList[6] = 'Major Positive Ability'
#     if newCardDataList[6] == -1:
#         newCardDataList[6] = 'Minor Negative Ability'
#     if newCardDataList[6] == -2:
#         newCardDataList[6] = 'Major Negative Ability'
#     if newCardDataList[7] == 2:
#         newCardDataList[7] = 'Move 1'
#     if newCardDataList[7] == 4:
#         newCardDataList[7] = 'Move 2'
#     if newCardDataList[7] == 6:
#         newCardDataList[7] = 'Move 3'
#     if newCardDataList[8] == 2:
#         newCardDataList[8] = 'Range 1'
#     if newCardDataList[8] == 4:
#         newCardDataList[8] = 'Range 2'
#     if newCardDataList[8] == 6:
#         newCardDataList[8] = 'Range 3'
#     if newCardDataList[9] == 2:
#         newCardDataList[9] = 'Hp 1'
#     if newCardDataList[9] == 4:
#         newCardDataList[9] = 'Hp 2'
#     if newCardDataList[9] == 6:
#         newCardDataList[9] = 'Hp 3'
        
#     cardDataList.append(newCardDataList)
#     print(tier + " " + rarity + "List")
#     for card in cardDataList:
#         print(card)

# cardDataFunction(tier1CommonCardList, "tier 1", 'common')

# for tier1CommonCardData in tier1CommonCardList:
#     newtier1CommonCardData = list(tier1CommonCardData)
#     if newtier1CommonCardData[0] == 2:
#         newtier1CommonCardData[0] = 'D4'
#     if newtier1CommonCardData[0] == 4:
#         newtier1CommonCardData[0] = 'D6'
#     if newtier1CommonCardData[0] == 6:
#         newtier1CommonCardData[0] = 'D8'
#     if newtier1CommonCardData[0] == 8:
#         newtier1CommonCardData[0] = 'D10'
#     if newtier1CommonCardData[0] == 10:
#         newtier1CommonCardData[0] = 'D12'
#     if newtier1CommonCardData[1] == 2:
#         newtier1CommonCardData[1] = 'D4'
#     if newtier1CommonCardData[1] == 4:
#         newtier1CommonCardData[1] = 'D6'
#     if newtier1CommonCardData[1] == 6:
#         newtier1CommonCardData[1] = 'D8'
#     if newtier1CommonCardData[1] == 8:
#         newtier1CommonCardData[1] = 'D10'
#     if newtier1CommonCardData[1] == 10:
#         newtier1CommonCardData[1] = 'D12'
#     if newtier1CommonCardData[2] == 2:
#         newtier1CommonCardData[2] = 'D4'
#     if newtier1CommonCardData[2] == 4:
#         newtier1CommonCardData[2] = 'D6'
#     if newtier1CommonCardData[2] == 6:
#         newtier1CommonCardData[2] = 'D8'
#     if newtier1CommonCardData[2] == 8:
#         newtier1CommonCardData[2] = 'D10'
#     if newtier1CommonCardData[2] == 10:
#         newtier1CommonCardData[2] = 'D12'
#     if newtier1CommonCardData[3] == 2:
#         newtier1CommonCardData[3] = 'D4'
#     if newtier1CommonCardData[3] == 4:
#         newtier1CommonCardData[3] = 'D6'
#     if newtier1CommonCardData[3] == 6:
#         newtier1CommonCardData[3] = 'D8'
#     if newtier1CommonCardData[3] == 8:
#         newtier1CommonCardData[3] = 'D10'
#     if newtier1CommonCardData[3] == 10:
#         newtier1CommonCardData[3] = 'D12'
#     if newtier1CommonCardData[4] == 0:
#         newtier1CommonCardData[5] = 'No Ability'
#         newtier1CommonCardData[6] = 'No Ability'
#         newtier1CommonCardData[4] = 'No Ability'
#     if newtier1CommonCardData[5] == 0:
#         newtier1CommonCardData[5] = 'No Ability'
#         newtier1CommonCardData[6] = 'No Ability'
#     if newtier1CommonCardData[6] == 0:
#         newtier1CommonCardData[6] = 'No Ability'        
#     if newtier1CommonCardData[4] == 1:
#         newtier1CommonCardData[4] = 'Minor Positive Ability'
#     if newtier1CommonCardData[4] == 2:
#         newtier1CommonCardData[4] = 'Major Positive Ability'
#     if newtier1CommonCardData[4] == -1:
#         newtier1CommonCardData[4] = 'Minor Negative Ability'
#     if newtier1CommonCardData[4] == -2:
#         newtier1CommonCardData[4] = 'Major Negative Ability'
#     if newtier1CommonCardData[5] == 1:
#         newtier1CommonCardData[5] = 'Minor Positive Ability'
#     if newtier1CommonCardData[5] == 2:
#         newtier1CommonCardData[5] = 'Major Positive Ability'
#     if newtier1CommonCardData[5] == -1:
#         newtier1CommonCardData[5] = 'Minor Negative Ability'
#     if newtier1CommonCardData[5] == -2:
#         newtier1CommonCardData[5] = 'Major Negative Ability'
#     if newtier1CommonCardData[6] == 1:
#         newtier1CommonCardData[6] = 'Minor Positive Ability'
#     if newtier1CommonCardData[6] == 2:
#         newtier1CommonCardData[6] = 'Major Positive Ability'
#     if newtier1CommonCardData[6] == -1:
#         newtier1CommonCardData[6] = 'Minor Negative Ability'
#     if newtier1CommonCardData[6] == -2:
#         newtier1CommonCardData[6] = 'Major Negative Ability'
#     if newtier1CommonCardData[7] == 2:
#         newtier1CommonCardData[7] = 'Move 1'
#     if newtier1CommonCardData[7] == 4:
#         newtier1CommonCardData[7] = 'Move 2'
#     if newtier1CommonCardData[7] == 6:
#         newtier1CommonCardData[7] = 'Move 3'
#     if newtier1CommonCardData[8] == 2:
#         newtier1CommonCardData[8] = 'Range 1'
#     if newtier1CommonCardData[8] == 4:
#         newtier1CommonCardData[8] = 'Range 2'
#     if newtier1CommonCardData[8] == 6:
#         newtier1CommonCardData[8] = 'Range 3'
#     if newtier1CommonCardData[9] == 2:
#         newtier1CommonCardData[9] = 'Hp 1'
#     if newtier1CommonCardData[9] == 4:
#         newtier1CommonCardData[9] = 'Hp 2'
#     if newtier1CommonCardData[9] == 6:
#         newtier1CommonCardData[9] = 'Hp 3'
    
    
#     completeTier1CommonCardList.append(newtier1CommonCardData)

# print(completeTier1CommonCardList)

# tier1CommonFinalCardList = []
# for i in completeTier1CommonCardList:
#         if i not in tier1CommonFinalCardList:
#             tier1CommonFinalCardList.append(i)

# print("Final Tier 1 Common Card Total:")
# print(len(tier1CommonFinalCardList))
# for i in tier1CommonFinalCardList:
#     print(i)

for tier1UncommonCardData in tier1UncommonCardList:
    newtier1UncommonCardData = list(tier1UncommonCardData)
    if newtier1UncommonCardData[0] == 2:
        newtier1UncommonCardData[0] = 'D4'
    if newtier1UncommonCardData[0] == 4:
        newtier1UncommonCardData[0] = 'D6'
    if newtier1UncommonCardData[0] == 6:
        newtier1UncommonCardData[0] = 'D8'
    if newtier1UncommonCardData[0] == 8:
        newtier1UncommonCardData[0] = 'D10'
    if newtier1UncommonCardData[0] == 10:
        newtier1UncommonCardData[0] = 'D12'
    if newtier1UncommonCardData[1] == 2:
        newtier1UncommonCardData[1] = 'D4'
    if newtier1UncommonCardData[1] == 4:
        newtier1UncommonCardData[1] = 'D6'
    if newtier1UncommonCardData[1] == 6:
        newtier1UncommonCardData[1] = 'D8'
    if newtier1UncommonCardData[1] == 8:
        newtier1UncommonCardData[1] = 'D10'
    if newtier1UncommonCardData[1] == 10:
        newtier1UncommonCardData[1] = 'D12'
    if newtier1UncommonCardData[2] == 2:
        newtier1UncommonCardData[2] = 'D4'
    if newtier1UncommonCardData[2] == 4:
        newtier1UncommonCardData[2] = 'D6'
    if newtier1UncommonCardData[2] == 6:
        newtier1UncommonCardData[2] = 'D8'
    if newtier1UncommonCardData[2] == 8:
        newtier1UncommonCardData[2] = 'D10'
    if newtier1UncommonCardData[2] == 10:
        newtier1UncommonCardData[2] = 'D12'
    if newtier1UncommonCardData[3] == 2:
        newtier1UncommonCardData[3] = 'D4'
    if newtier1UncommonCardData[3] == 4:
        newtier1UncommonCardData[3] = 'D6'
    if newtier1UncommonCardData[3] == 6:
        newtier1UncommonCardData[3] = 'D8'
    if newtier1UncommonCardData[3] == 8:
        newtier1UncommonCardData[3] = 'D10'
    if newtier1UncommonCardData[3] == 10:
        newtier1UncommonCardData[3] = 'D12'
    if newtier1UncommonCardData[4] == 0:
        newtier1UncommonCardData[5] = 'No Ability'
        newtier1UncommonCardData[6] = 'No Ability'
        newtier1UncommonCardData[4] = 'No Ability'
    if newtier1UncommonCardData[5] == 0:
        newtier1UncommonCardData[5] = 'No Ability'
        newtier1UncommonCardData[6] = 'No Ability'
    if newtier1UncommonCardData[6] == 0:
        newtier1UncommonCardData[6] = 'No Ability'        
    if newtier1UncommonCardData[4] == 1:
        newtier1UncommonCardData[4] = 'Minor Positive Ability'
    if newtier1UncommonCardData[4] == 2:
        newtier1UncommonCardData[4] = 'Major Positive Ability'
    if newtier1UncommonCardData[4] == -1:
        newtier1UncommonCardData[4] = 'Minor Negative Ability'
    if newtier1UncommonCardData[4] == -2:
        newtier1UncommonCardData[4] = 'Major Negative Ability'
    if newtier1UncommonCardData[5] == 1:
        newtier1UncommonCardData[5] = 'Minor Positive Ability'
    if newtier1UncommonCardData[5] == 2:
        newtier1UncommonCardData[5] = 'Major Positive Ability'
    if newtier1UncommonCardData[5] == -1:
        newtier1UncommonCardData[5] = 'Minor Negative Ability'
    if newtier1UncommonCardData[5] == -2:
        newtier1UncommonCardData[5] = 'Major Negative Ability'
    if newtier1UncommonCardData[6] == 1:
        newtier1UncommonCardData[6] = 'Minor Positive Ability'
    if newtier1UncommonCardData[6] == 2:
        newtier1UncommonCardData[6] = 'Major Positive Ability'
    if newtier1UncommonCardData[6] == -1:
        newtier1UncommonCardData[6] = 'Minor Negative Ability'
    if newtier1UncommonCardData[6] == -2:
        newtier1UncommonCardData[6] = 'Major Negative Ability'
    if newtier1UncommonCardData[7] == 2:
        newtier1UncommonCardData[7] = 'Move 1'
    if newtier1UncommonCardData[7] == 4:
        newtier1UncommonCardData[7] = 'Move 2'
    if newtier1UncommonCardData[7] == 6:
        newtier1UncommonCardData[7] = 'Move 3'
    if newtier1UncommonCardData[8] == 2:
        newtier1UncommonCardData[8] = 'Range 1'
    if newtier1UncommonCardData[8] == 4:
        newtier1UncommonCardData[8] = 'Range 2'
    if newtier1UncommonCardData[8] == 6:
        newtier1UncommonCardData[8] = 'Range 3'
    if newtier1UncommonCardData[9] == 2:
        newtier1UncommonCardData[9] = 'Hp 1'
    if newtier1UncommonCardData[9] == 4:
        newtier1UncommonCardData[9] = 'Hp 2'
    if newtier1UncommonCardData[9] == 6:
        newtier1UncommonCardData[9] = 'Hp 3'    
    
    completeTier1UncommonCardList.append(newtier1UncommonCardData)

Tier1UncommonFinalCardList = []
for i in completeTier1UncommonCardList:
        if i not in Tier1UncommonFinalCardList:
            Tier1UncommonFinalCardList.append(i)

for i in Tier1UncommonFinalCardList:
    print(i)

# # print("Final Tier 1 Uncommon Card Total:")
# # print(len(Tier1UncommonFinalCardList))

# for tier1RareCardData in tier1RareCardList:
#     newtier1RareCardData = list(tier1RareCardData)
#     if newtier1RareCardData[0] == 2:
#         newtier1RareCardData[0] = 'D4'
#     if newtier1RareCardData[0] == 4:
#         newtier1RareCardData[0] = 'D6'
#     if newtier1RareCardData[0] == 6:
#         newtier1RareCardData[0] = 'D8'
#     if newtier1RareCardData[0] == 8:
#         newtier1RareCardData[0] = 'D10'
#     if newtier1RareCardData[0] == 10:
#         newtier1RareCardData[0] = 'D12'
#     if newtier1RareCardData[1] == 2:
#         newtier1RareCardData[1] = 'D4'
#     if newtier1RareCardData[1] == 4:
#         newtier1RareCardData[1] = 'D6'
#     if newtier1RareCardData[1] == 6:
#         newtier1RareCardData[1] = 'D8'
#     if newtier1RareCardData[1] == 8:
#         newtier1RareCardData[1] = 'D10'
#     if newtier1RareCardData[1] == 10:
#         newtier1RareCardData[1] = 'D12'
#     if newtier1RareCardData[2] == 2:
#         newtier1RareCardData[2] = 'D4'
#     if newtier1RareCardData[2] == 4:
#         newtier1RareCardData[2] = 'D6'
#     if newtier1RareCardData[2] == 6:
#         newtier1RareCardData[2] = 'D8'
#     if newtier1RareCardData[2] == 8:
#         newtier1RareCardData[2] = 'D10'
#     if newtier1RareCardData[2] == 10:
#         newtier1RareCardData[2] = 'D12'
#     if newtier1RareCardData[3] == 2:
#         newtier1RareCardData[3] = 'D4'
#     if newtier1RareCardData[3] == 4:
#         newtier1RareCardData[3] = 'D6'
#     if newtier1RareCardData[3] == 6:
#         newtier1RareCardData[3] = 'D8'
#     if newtier1RareCardData[3] == 8:
#         newtier1RareCardData[3] = 'D10'
#     if newtier1RareCardData[3] == 10:
#         newtier1RareCardData[3] = 'D12'
#     if newtier1RareCardData[4] == 0:
#         newtier1RareCardData[5] = 'No Ability'
#         newtier1RareCardData[6] = 'No Ability'
#         newtier1RareCardData[4] = 'No Ability'
#     if newtier1RareCardData[5] == 0:
#         newtier1RareCardData[5] = 'No Ability'
#         newtier1RareCardData[6] = 'No Ability'
#     if newtier1RareCardData[6] == 0:
#         newtier1RareCardData[6] = 'No Ability'        
#     if newtier1RareCardData[4] == 1:
#         newtier1RareCardData[4] = 'Minor Positive Ability'
#     if newtier1RareCardData[4] == 2:
#         newtier1RareCardData[4] = 'Major Positive Ability'
#     if newtier1RareCardData[4] == -1:
#         newtier1RareCardData[4] = 'Minor Negative Ability'
#     if newtier1RareCardData[4] == -2:
#         newtier1RareCardData[4] = 'Major Negative Ability'
#     if newtier1RareCardData[5] == 1:
#         newtier1RareCardData[5] = 'Minor Positive Ability'
#     if newtier1RareCardData[5] == 2:
#         newtier1RareCardData[5] = 'Major Positive Ability'
#     if newtier1RareCardData[5] == -1:
#         newtier1RareCardData[5] = 'Minor Negative Ability'
#     if newtier1RareCardData[5] == -2:
#         newtier1RareCardData[5] = 'Major Negative Ability'
#     if newtier1RareCardData[6] == 1:
#         newtier1RareCardData[6] = 'Minor Positive Ability'
#     if newtier1RareCardData[6] == 2:
#         newtier1RareCardData[6] = 'Major Positive Ability'
#     if newtier1RareCardData[6] == -1:
#         newtier1RareCardData[6] = 'Minor Negative Ability'
#     if newtier1RareCardData[6] == -2:
#         newtier1RareCardData[6] = 'Major Negative Ability'
#     if newtier1RareCardData[7] == 2:
#         newtier1RareCardData[7] = 'Move 1'
#     if newtier1RareCardData[7] == 4:
#         newtier1RareCardData[7] = 'Move 2'
#     if newtier1RareCardData[7] == 6:
#         newtier1RareCardData[7] = 'Move 3'
#     if newtier1RareCardData[8] == 2:
#         newtier1RareCardData[8] = 'Range 1'
#     if newtier1RareCardData[8] == 4:
#         newtier1RareCardData[8] = 'Range 2'
#     if newtier1RareCardData[8] == 6:
#         newtier1RareCardData[8] = 'Range 3'
#     if newtier1RareCardData[9] == 2:
#         newtier1RareCardData[9] = 'Hp 1'
#     if newtier1RareCardData[9] == 4:
#         newtier1RareCardData[9] = 'Hp 2'
#     if newtier1RareCardData[9] == 6:
#         newtier1RareCardData[9] = 'Hp 3'    
    
#     completeTier1RareCardList.append(newtier1RareCardData)

# Tier1RareFinalCardList = []
# for i in completeTier1RareCardList:
#         if i not in Tier1RareFinalCardList:
#             Tier1RareFinalCardList.append(i)

