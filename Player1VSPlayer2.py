
# =======================================================================
# divisor_game(n, player1, player2)
#
# Mediates the divisor game starting with positive integer n
# between player1 and player2 (both are strings of their names).
#
# This function has no return value.
# =======================================================================

def divisor_game(n, player1, player2):
    checkNum = True
    numList = []
    for i in range(1, n + 1):
        if n % i == 0:
            numList.append(i)

    print(f'Here are the remaining numbers: {numList}')

    a = int(input(f"{player1}, pick a number from the list above : "))

    count = 1
    remain = 1

    while numList != []:
        if a not in numList:
            count = 1
            checkNum = False
        else:
            count = 0
            checkNum = True

        if checkNum == False:
            if count == 1 and remain == 1:
                a = int(input(f'{player1} ,pick something that is in the list: '))
            else:
                a = int(input(f'{player2}, pick something that is in the list: '))
        # store remaining value

        indexP = 0
        if checkNum == True:
            while a != numList[indexP]:
                indexP = indexP + 1
            if indexP > 0:
                while indexP != 0:
                    if a % numList[indexP] == 0:
                        numList.remove(numList[indexP])
                    indexP = indexP - 1
                if a % numList[indexP] == 0:
                    numList.remove(numList[indexP])
            else:
                numList.remove(numList[indexP])

            if numList != []:
                if remain == 1:
                    print(f'\n\nHere are the remaining numbers: {numList}')
                    a = int(input(f'{player2}, pick a number from the list above : '))
                    remain = 0

                else:
                    print(f'\n\nHere are the remaining numbers: {numList}')
                    a = int(input(f'{player1}, pick a number from the list above : '))
                    remain = 1
    if remain == 1:
        print(f'\n {player1},you  lose ! {player2},you win ! ')
    else:

        print(f'\n{player2},you lose  ! {player1},you  win !')


# =======================================================================
# Main program below (do not alter!)
# =======================================================================

print("\nWelcome to the Divisor Game!")
player1 = input("\nPlayer 1, enter your name:  ")
player2 = input("Player 2, enter your name:  ")

n = int(input("Enter positive integer n:  "))

while n > 0:
    divisor_game(n, player1, player2)
    print("=========================================================")
    n = int(input("\n\nEnter positive integer n to play again (or 0 to quit):  "))

print("\nBye!")
