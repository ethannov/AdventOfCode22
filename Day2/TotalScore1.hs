{-
A,B,C is opponents
X,Y,Z is what I play

A,B,C = X,Y,Z = rock, paper, scissors

rock  = 1 point
paper = 2 point
scis  = 3 point

lose = 0 point
draw = 3 points
win  = 6 points
-}

getScore :: String -> Int
getScore "A X" = 1 + 3
getScore "A Y" = 2 + 6
getScore "A Z" = 3 + 0
getScore "B X" = 1 + 0
getScore "B Y" = 2 + 3
getScore "B Z" = 3 + 6
getScore "C X" = 1 + 6
getScore "C Y" = 2 + 0
getScore "C Z" = 3 + 3

main = do  
        contents <- readFile "input.txt"
        let parsed = [getScore x | x <- lines contents]
        print (sum parsed)
