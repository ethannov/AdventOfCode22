{-
A,B,C is opponents play
X,Y,Z is how the game should end

A,B,C = rock, paper, scissors
X,Y,Z = lose, draw, win

rock  = 1 point
paper = 2 point
scis  = 3 point

lose = 0 point
draw = 3 points
win  = 6 points
-}

getScore :: String -> Int
getScore "A X" = 3 + 0
getScore "A Y" = 1 + 3
getScore "A Z" = 2 + 6
getScore "B X" = 1 + 0
getScore "B Y" = 2 + 3
getScore "B Z" = 3 + 6
getScore "C X" = 2 + 0
getScore "C Y" = 3 + 3
getScore "C Z" = 1 + 6

main = do  
        contents <- readFile "input.txt"
        let parsed = [getScore x | x <- lines contents]
        print (sum parsed)
