# import os
# print(os.getcwd())

import numpy as np

file = open("./AdventOfCode22/Day8/input.txt")
input = file.read()
rows = input.split()
for i in range(0, len(rows)):
    rows[i] = [int(x) for x in rows[i]]
EWarray = np.array(rows)
NSarray = EWarray.transpose()

visibilityArray = np.zeros((EWarray.shape))
# check each number if it's visible
for row in range(0, len(EWarray)):
    for treei in range(0, len(EWarray[row])):
        EastVis = True
        WestVis = True
        # tree = EWarray[row][treei]
        for E in range(0, treei):
            # temp = EWarray[row][E]
            if (EWarray[row][E] >= EWarray[row][treei]):
                EastVis = False
                continue
        for W in range(treei+1, len(EWarray[row])):
            # temp = EWarray[row][W]
            if (EWarray[row][W] >= EWarray[row][treei]):
                WestVis = False
                continue
        if (EastVis or WestVis):
            visibilityArray[row][treei] = True
        else:
            visibilityArray[row][treei] = False
        # print(visibilityArray)
        # print(f"row: {row}, treei: {treei}")
        
# same thing but for NWarray
for row in range(0, len(NSarray)):
    for treei in range(0, len(NSarray[row])):
        NorthVis = True
        SouthVis = True
        # tree = NSarray[row][treei]
        for N in range(0, treei):
            # temp = NSarray[row][N]
            if (NSarray[row][N] >= NSarray[row][treei]):
                NorthVis = False
                continue
        for S in range(treei+1, len(NSarray[row])):
            # temp = NSarray[row][S]
            if (NSarray[row][S] >= NSarray[row][treei]):
                SouthVis = False
                continue
        if (NorthVis or SouthVis or visibilityArray[treei][row]): # make vis true if already true
            visibilityArray[treei][row] = True # index are transposed
        else:
            visibilityArray[treei][row] = False
        # print(visibilityArray)
        # print(f"row: {row}, treei: {treei}")
        
print(f"Number of visible trees is {np.count_nonzero(visibilityArray == 1)}")
            
    
# check if outside
# check if any number north is >
# check if any number east is >
# check if any number south is >
# check if any number west is >