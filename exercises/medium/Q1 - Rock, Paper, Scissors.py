"""
Create a function which takes two strings (p1 and p2 ⁠— which represent player 1 and 2) as arguments and returns a string stating the winner in a game of Rock, Paper, Scissors.

Each argument will contain a single string: "Rock", "Paper", or "Scissors". Return the winner according to the following rules:

Rock beats Scissors

Scissors beats Paper

Paper beats Rock

If p1 wins, return the string "The winner is p1". If p2 wins, return the string "The winner is p2" and if p1 and p2 are the same, return "It's a draw".

"""

def rps(p1,p2):
    p1,p2 = p1.lower(),p2.lower()
    if p1 == p2 :
        return "It's a draw"
    
    elif p1 == 'rock':
        
        if p2 == 'scissors':
            return 'The winner is p1'
        elif p2 == 'paper':
            return 'The winner is p2'
        else :
            return 'Please give a valid input'
        
    elif p1 == 'scissors':
        
        if p2 == 'rock':
            return 'The winner is p2'
        elif p2 == 'paper':
            return 'The winner is p1'
        else :
            return 'Please give a valid input'
        
    elif p1 == 'paper':
        
        if p2 == 'rock':
            return 'The winner is p1'
        elif p2 == 'scissors':
            return 'The winner is p2'
        else :
            return 'Please give a valid input'
        
    else :
        return 'Please give a valid input'
            
    return