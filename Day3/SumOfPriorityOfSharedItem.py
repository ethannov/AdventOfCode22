def findSharedItem(c1, c2):
    for item1 in c1:
        for item2 in c2:
            if (item1 == item2):
                # print(item1)
                return item1

f = open("input.txt")

input = f.read()

sharedItems = []

for sack in input.split("\n"):
    size = len(sack) / 2
    compartment1 = sack[0:size]
    compartment2 = sack[size:-1]
    # print(sack)
    sharedItems.append(findSharedItem(compartment1, compartment2))


# print(len(input.split("\n")))
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
        
