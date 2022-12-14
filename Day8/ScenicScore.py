import numpy as np

file = open("./AdventOfCode22/Day8/input.txt")
input = file.read()
rows = input.split()
for i in range(0, len(rows)):
    rows[i] = [int(x) for x in rows[i]]
EWarray = np.array(rows)
NSarray = EWarray.transpose()

visibilityArray = np.zeros((EWarray.shape))
for row in range(0, len(EWarray)):
    for treei in range(0, len(EWarray[row])):
        EastVis = 0
        WestVis = 0
        tree = EWarray[row][treei]
        
        EastTrees =  EWarray[row][treei::-1]
        WestTrees =  EWarray[row][treei:]
        
        for x in EastTrees[1:]:
            if (x < EWarray[row][treei]):
                EastVis += 1
            else:
                EastVis += 1
                break
        for x in WestTrees[1:]:
            if (x < EWarray[row][treei]):
                WestVis += 1
            else:
                WestVis += 1
                break
            

        visibilityArray[row][treei] += EastVis * WestVis
        # print(visibilityArray)
        
# same thing but for NSarray
for row in range(0, len(NSarray)):
    for treei in range(0, len(NSarray[row])):
        NorthVis = 0
        SouthVis = 0
        tree = NSarray[row][treei]
        
        NorthTrees =  NSarray[row][treei::-1]
        SouthTrees =  NSarray[row][treei:]
        
        for x in NorthTrees[1:]:
            if (x < NSarray[row][treei]):
                NorthVis += 1
            else:
                NorthVis += 1
                break
        for x in SouthTrees[1:]:
            if (x < NSarray[row][treei]):
                SouthVis += 1
            else:
                SouthVis += 1
                break
            

        visibilityArray[treei][row] *= NorthVis * SouthVis # index are transposed
        # print(visibilityArray)

print(f"Highest scenic score is {np.amax(visibilityArray)}")