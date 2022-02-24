#Project is about simple console based rock paper scissors game
import random as rn

#main, play function used to play the game and return the result
def play():
    user=input("what's your choice 'r'- Rock, 'p'- Paper, 's'- Scissors\n")
    RPS=['r','p','s']
    computer=rn.choice(RPS)
    if user in RPS:
        pass
    else:
        return "Please enter only above any option accuratly"
    
    if user == computer:
        return "It\'s tie"
    
    if win(user,computer):
        return "you won!"

    #here i didn't state else line because if above two conditions failes then only controls come to here
    return "you lost!"

#win function will be decided whether human or computer will be winner
def win(human,computer):
    #r>s, s>p, p>r wining conditions
    if (human=='r' and computer=='s') or (human=='s' and computer=='p') or (human=='p' and computer=='r'):
        return True


i=True
while i==True:
    print(play())
    n=input("Press 1 to exit or to continue press ENTER\n")
    if n=='1':
        break