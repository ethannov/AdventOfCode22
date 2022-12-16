## USING DICT
import numpy as np

file = open("./AdventOfCode22/Day9/input.txt")
input = file.read()
commands = input.split('\n')
for i in range(0, len(commands)):
    commands[i] = commands[i].split(' ')

Hvisited = dict()
Tvisited = dict()

H = [0, 0] # x, y
T = [0, 0]

maxHx = 0
maxHy = 0

# record initial positions
for i, c in enumerate(commands):
    # move H
    for n in range(0, int(c[1])):
        if (c[0] == 'R'):
            H[0] += 1
        elif (c[0] == 'L'):
            H[0] -= 1
        elif (c[0] == 'U'):
            H[1] += 1
        elif (c[0] == 'D'):
            H[1] -= 1
    
        # move T
        distance = (T[0]-H[0])**2 + (T[1]-H[1])**2
        if (distance > 1):
            # check direction to move
            # R
            if (H[0] - T[0] == 2):
                T[0] = H[0]-1
                T[1] = H[1]
            # L
            if (H[0] - T[0] == -2):
                T[0] = H[0]+1
                T[1] = H[1]
            # U
            if (H[1] - T[1] == 2):
                T[0] = H[0]
                T[1] = H[1]-1
            # D
            if (H[1] - T[1] == -2):
                T[0] = H[0]
                T[1] = H[1]+1
            
        #print(f"Bridge. dir {c[0]}. num {c[1]}. n {n}.")
        #print(np.flipud(HTarray))
        
        if (H[0] > maxHx):
            maxHx = H[0]
        if (H[1] > maxHy):
            maxHy = H[1]
            
        # record new position
        Hvisited[str(H[0])+str(H[1])] = i
        Tvisited[str(T[0])+str(T[1])] = i
            
print("Finished Simulation")
print(f"Tiles visited at least once: {len(Tvisited)}")
# 6642 correct
        
        
# USING NUMPY ARRAY
# import numpy as np

# file = open("./AdventOfCode22/Day9/input.txt")
# input = file.read()
# commands = input.split('\n')
# for i in range(0, len(commands)):
#     commands[i] = commands[i].split(' ')

# HTshape = (1000,1000)
# HTarray = np.zeros(HTshape)
# Tvisited = np.zeros(HTshape)

# H = [0, 0] # x, y
# T = [0, 0]

# maxHx = 0
# maxHy = 0
# for c in commands:
#     # move H
#     for n in range(0, int(c[1])):
#         HTarray[H[1]][H[0]] = 0
#         if (c[0] == 'R'):
#             H[0] += 1
#         elif (c[0] == 'L'):
#             H[0] -= 1
#         elif (c[0] == 'U'):
#             H[1] += 1
#         elif (c[0] == 'D'):
#             H[1] -= 1
            
#         # Set positions of H and T in array
#         Tvisited[T[1]][T[0]] += 1# record T's position
#         HTarray[T[1]][T[0]] = 2
#         HTarray[H[1]][H[0]] = 1
    
#         # move T
#         distance = (T[0]-H[0])**2 + (T[1]-H[1])**2
#         if (distance > 1):
#             HTarray[T[1]][T[0]] = 0 # reset T's prev position
#             # check direction to move
#             # R
#             if (H[0] - T[0] == 2):
#                 T[0] = H[0]-1
#                 T[1] = H[1]
#             # L
#             if (H[0] - T[0] == -2):
#                 T[0] = H[0]+1
#                 T[1] = H[1]
#             # U
#             if (H[1] - T[1] == 2):
#                 T[0] = H[0]
#                 T[1] = H[1]-1
#             # D
#             if (H[1] - T[1] == -2):
#                 T[0] = H[0]
#                 T[1] = H[1]+1
#             HTarray[T[1]][T[0]] = 2
            
#         #print(f"Bridge. dir {c[0]}. num {c[1]}. n {n}.")
#         #print(np.flipud(HTarray))
        
#         if (H[0] > maxHx):
#             maxHx = H[0]
#         if (H[1] > maxHy):
#             maxHy = H[1]
            
# print("Finished Simulation")
# print(f"Tiles visited at least once: {np.count_nonzero(Tvisited)}")
# print(np.flipud(Tvisited))
        
# # 6641
# # 6700 that's not the right answer
# # 6800
# # 7000