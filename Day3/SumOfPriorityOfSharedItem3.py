def findSharedItem(s1, s2, s3):
    for item1 in s1:
        for item2 in s2:
            for item3 in s3:
                if (item1 == item2 == item3):
                    # print(item1)
                    return item1

f = open("input.txt")

input = f.read()
sacks = input.split("\n")

sharedItems = []

for i in range(0, len(sacks), 3):
    elf1 = sacks[i]
    elf2 = sacks[i+1]
    elf3 = sacks[i+2]
    sharedItems.append(findSharedItem(elf1, elf2, elf3))

# print(len(sacks))
# print(len(sharedItems))

sumPriorities = 0
for item in sharedItems:
    if (ord(item) >= ord('a')):
        sumPriorities += ord(item) - 96 
        # print(item, ord(item) - 96 )
    
    elif (ord(item) >= ord('A')):
        sumPriorities += ord(item) - 64 + 26
        # print(item, ord(item) - 64+ 26)
        
print("The sum of priorities is", sumPriorities)
        
