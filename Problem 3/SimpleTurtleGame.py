import turtle
import random

player1 = turtle.Turtle()
player1.color("green")
player1.shape("turtle")
player1.penup()
player1.goto(-200,100)

player2 = player1.clone()
player2.color("blue")
player2.penup()
player2.goto(-200,-100)

player1.goto(200,60)
player1.pendown()
player1.circle(40)
player1.penup()
player1.goto(-200,100)

player2.goto(200,-120)
player2.pendown()
player2.circle(40)
player2.penup()
player2.goto(-200,-100)

dice = [1,2,3,4,5,6]

def checkIfWin():
    if player1.pos() >= (170,100):
        print("Player One Wins!!")
        return True
    elif player2.pos() >= (170,-80):
        print("Player Two Wins!!")
        return True
    else:
        return False

def nextTurnP1():
    player1_turn = input("Press 'Enter' to roll the dice:")
    dice_out = random.choice(dice)
    print("The result of Dice: ",dice_out)
    print("Steps : ",(20*dice_out))
    player1.forward(20*dice_out)

def nextTurnP2():
    player2_turn = input("Press 'Enter' to roll the dice:")
    dice_out = random.choice(dice)
    print("THe result od Dice:")
    print(dice_out)
    print("Steps : ",(20*dice_out))
    player2.forward(20*dice_out)   

while True:
    is_win = checkIfWin()
    if(is_win==False):
        nextTurnP1()
        player1_win = checkIfWin()
        if(player1_win==False):
            nextTurnP2()
            player2_win = checkIfWin()
            if(player2_win==False):
                pass
            else:
                break
        else:
            break
    else:
        break
        
