
# =======================================================================
# divisor_game_agent(n, name, turnNum, agent)
#
# Mediates the divisor game starting with postive integer n
# between a human named "name" and agent "agent", which is a function that takes a list
# of the remaining divisors and returns one of them.
#
# turnNum = 1 if the human wants to go first, 2 if the human wants to go second.
#

def divisor_game_agent(n, name, turnNum, agent):
    checkNum = True
    k = 0
    visit = True
    track = 0
    numList = []
    count = 1
    a = 0
    while count < n + 1:
        if n % count == 0:
            numList.append(count)
        count = count + 1

    x = agent(numList)

    newList = numList.copy()
    lenOfList = len(newList)
    print(f'\nHere are the remaining numbers: {numList}')
    if turnNum == 1:
        a = int(input(f'{name} , pick a number from the list above: '))
        checkNum = True
        k = 1

    elif turnNum == 2:
        print(f'Agent picked {x}.')
        newList.remove(newList[0])
        checkNum = False
        k = 0

    while newList != []:
        # I am just checking when user enter a integer
        if checkNum == True:
            track = 0
            # checking there are number in the list or not
            if a in newList:
                track = 1
                visit = True

            elif track == 0:
                a = int(input(f'{name} ,pick something that is in the list: '))
                visit = False

        # storing  remaining value

        indexP = 0
        if track == 1:
            # this goes to until entering number
            while a != newList[indexP]:
                indexP = indexP + 1

            while indexP >= 0:
                if a % newList[indexP] == 0:
                    newList.remove(newList[indexP])
                indexP = indexP - 1

        if newList != [] and visit == True:
            print(f'\nHere are the remaining numbers: {newList}')

            if k == 0:
                a = int(input(f'{name}, pick a number from the list above : '))
                checkNum = True
                k = 1
                track = 1

            elif k == 1:
                x = agent(newList)
                print(f'Agent picked {x}.')
                newList.remove(newList[0])
                k = 0
                checkNum = False
                track = 0

    if k == 1:
        print(f'\n {name},you  lose ! Agent,you win ! ')
    else:
        print(f'\n Agent ,you lose  ! {name},you  win !')


# =======================================================================
# Don't alter anything below here!

# =======================================================================
# Simple agent always picks first number in list

def simple_agent(divisors):
    return divisors[0]


# =======================================================================
# Main program:
print("Welcome to the Divisor Game!")

name = input("\nEnter your name:  ")
n = int(input("Enter positive integer n:  "))
turnNum = int(input("Enter 1 if you want to go first, 2 for second:  "))

divisor_game_agent(n, name, turnNum, simple_agent)
