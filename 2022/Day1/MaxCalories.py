f = open("./Day1/input.txt")

input = f.read()

max = 0
elfNum = 0
maxCalElf = 0

for cal in input.split("\n\n"):
    if (max < sum(int(x) for x in cal.split("\n"))):
        max = sum(int(x) for x in cal.split("\n"))
        maxCalElf = elfNum
    elfNum += 1
    
print("Elf with max calories is elf no.", maxCalElf)
print("They have", max, "calories")