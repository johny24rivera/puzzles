import itertools

alphabets = [' ', 'z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a', '\n','.']
vals = [ 7,12,0,14,2,0,22,5,22,5,2,0,23,26,2,0,15,12,5,22,-2,
         7,19,22,0,14,12,12,13,0,26,13,23,0,7,19,22,0,
         8,7,26,9,8,0,26,9,22,0,23,9,18,20,19,7,22,9,-1,-2,
         7,19,22,0,8,6,13,0,8,22,7,8,0,22,5,22,13,0,
         8,4,22,22,7,22,9,-1,-2,
         7,19,22,0,4,12,9,15,23,0,8,7,26,2,8,0,-2,
         8,7,18,15,15,0,4,19,22,13,0,2,12,6,-2,
         19,12,15,23,0,14,22,0,13,22,26,9,0,26,13,23,0,-2,
         18,0,26,14,0,9,22,14,18,13,23,22,23,0,12,21,-2,
         7,18,14,22,0,4,12,9,7,19,0,4,26,18,7,18,13,20,-1,-2,
         2,12,6,9,0,21,9,18,22,13,23,8,19,18,11,0,18,0,-2,
         24,19,22,9,18,8,19,-1,2,12,6,9,0,11,9,12,7,22,24,
         7,18,12,13,0,18,0,26,11,11,9,22,24,18,26,7,22,-1,-2,
         2,12,6,9,0,24,12,14,11,26,13,18,12,13,8,19,18,11,-1,-2,
         18,0,11,9,26,2,-2,
         18,0,26,14,0,26,15,4,26,2,8,0,4,12,9,7,19,2,-1,-2,
         14,2,0,15,12,5,22,0,22,5,22,2,0,23,26,2,-2,
         22,5,22,2,0,14,12,14,22,13,7,-2,
         22,5,22,2,0,8,14,18,13,22,-1,-2,
         18,0,15,12,5,22,0,2,12,6,0,7,12,23,26,2,-2,
         26,13,23,0,22,5,22,2,0,23,26,2,0,-2,
         26,21,7,22,9,-1,-2,
         18,0,15,12,5,22,0,2,12,6]

puzzle = []

for n in vals:
    puzzle.append(alphabets[n])

print("".join(puzzle))