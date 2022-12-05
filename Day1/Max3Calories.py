f = open("./Day1/input.txt")

input = f.read()

sumOfCals = []

for cal in input.split("\n\n"):
    sumOfCals.append(sum(int(x) for x in cal.split("\n")))
    
sumOfCals.sort(reverse=True)

print("Sum of calories of top three elves is:", sumOfCals[0] + sumOfCals[1] + sumOfCals[2])