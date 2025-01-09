import os
import time

def create_board():
    boxes=[]
    sub_box=[]
    for i in range(9):
        sub_box.append("_ ")
        if(i==2 or i==5 or i==8):
            boxes.append(sub_box)
            sub_box=[]
    return boxes

def display_board(boxes):
    for i in range(3):
        print(boxes[i][0]," ",boxes[i][1]," ",boxes[i][2])
        print("\n")
        
def check_state(boxes,winner,turn):
    if(turn==1):
        player="O"
    else:
        player="X"
    
    if(boxes[0][0]==boxes[1][1] and boxes[1][1]==boxes[2][2]):
            if(player==boxes[0][0]):
                winner=boxes[0][0]
    elif(boxes[0][2]==boxes[1][1] and boxes[1][1]==boxes[2][0]):
            if(player==boxes[0][2]):
                winner=boxes[0][2]
    else:
        for i in range(3):
            if(boxes[i][0]==boxes[i][1] and boxes[i][1]==boxes[i][2]):
                if(player==boxes[i][0]):
                    winner=boxes[i][0]
                break
            elif(boxes[0][i]==boxes[1][i] and boxes[1][i]==boxes[2][i]):
                if(player==boxes[0][i]):
                    winner=boxes[0][i]
                break
    return winner

def main():
    moves=1
    turn=1
    winner =None
    boxes=create_board()
    moves_matching={    1:[0,0],    2:[0,1],   3:[0,2],
                        4:[1,0],    5:[1,1],   6:[1,2],
                        7:[2,0],    8:[2,1],   9:[2,2]
                    }
    while not winner:
        print("tic-tac-toe Game")
        print("The game starts with - 'X' then goes to 'O' and vice versa \n until a winner is declared or the game is drawed\n\n")
        if turn:
            print("X turn\n")
        else:
            print("O turn\n")
        
        display_board(boxes)

        player=int(input("Enter the Postion starting from \n 1 2 3\n 4 5 6 \n 7 8 9\nYour Position:- "))

        posX=moves_matching[player][0]
        posY=moves_matching[player][1]
        if(boxes[posX][posY]=="X" or boxes[posX][posY]=='O'):
            print(f"Wrong postion.Player {boxes[posX][posY]} have already used it.")
            moves-=1
            time.sleep(3)
        elif turn:
            boxes[posX][posY]="X"
            turn=0
        else:
            boxes[posX][posY]="O"
            turn=1

        display_board(boxes)
        winner=check_state(boxes,winner,turn)
        moves+=1
        if(winner=='X' or winner=='O'):
            print(f"Game has ended.\nThe winner is {winner}")
        elif(moves==9):
            print(f"Game has ended.\nThe winner is No one")
            break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
main()