import math  # use math.inf and -math.inf for infinity and negative infinity


# =======================================================================
# COPY YOUR FUNCTION "divisor_game_agent(n, name, turnNum, agent)" here:
#

def divisor_game_agent(n, name, turnNum, agent):
    checkNum = True
    k = 0
    visit = True
    track = 0
    numList = []
    count = 1
    a = 0
    rem_forPrint = 0
    while count < n + 1:
        if n % count == 0:
            numList.append(count)
        count = count + 1

    # x = agent(numList)
    # print(x)
    newList = numList.copy()
    lenOfList = len(newList)
    print(f'\nHere are the remaining numbers: {numList}')
    if turnNum == 1:
        a = int(input(f'{name} , pick a number from the list above: '))
        checkNum = True
        k = 1
    # =========================================
    # when agents turn then I have to go to DG_max_value
    elif turnNum == 2:
        x = agent(newList, -math.inf, math.inf)
        print(f'Agent picked {x[1]} ')
        print(f'(Agent visited {x[2]}  nodes to determine this.)')
        newList = result(x[1], newList)
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

        # store remaining value
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
                x = agent(newList, -math.inf, math.inf)
                print(f'Agent picked {x[1]} ')
                print(f'(Agent visited {x[2]} nodes to determine this.)')
                newList = result(x[1], newList)
                k = 0
                checkNum = False
                track = 0

    if k == 1:
        print(f'\n{name},you  lose ! Agent,you win ! ')
    else:
        print(f'\nAgent ,you lose  ! {name},you  win !')


def result(value, div):
    newList = []
    for i in div:
        if value % i != 0:
            newList.append(i)

    return newList


# =======================================================================
# DG_Max_Value:  IMPLEMENTS ALPHA BETA PRUNING
#
# Input:   divisors = list of the remaining divisors'
#          alpha   = a lower bound on the minimax value of the node
#          beta    = an upper bound on the minimax value of the node
#
# Returns a list:  [u, a, numNodes]
#
#    where u = the maximum utility that can be achieved at this node (divisors)
#          a = the action (divisor to pick) that achieves maximum utility
#          numNodes = number of nodes examined (including the current node) to determine this

def DG_Max_Value(divisors, alpha, beta):
    if divisors == []:
        return [1, 0, 1]
    else:
        # current_u = alpha
        max_u = alpha
        best_a = 0

        total = 1
        for c in divisors:

            x = DG_Min_Value(result(c, divisors), alpha, beta)
            total += x[2]
            current_u = x[0]
            if current_u > max_u:
                max_u = current_u
                best_a = c

            if current_u >= beta:
                return [max_u, best_a, total]

            if current_u > alpha:
                alpha = current_u

    return [max_u, best_a, total]


# =======================================================================
# DG_Min_Value:  IMPLEMENTS ALPHA BETA PRUNING
#
# Input:   divisors = list of the remaining divisors'
#          alpha   = a lower bound on the minimax value of the node
#          beta    = an upper bound on the minimax value of the node
#
# Returns a list:  [u, a, numNodes]
#
#    where u = the minimum utility that can be achieved at this node (divisors)
#          a = the action (divisor to pick) that achieves minimum utility
#          numNodes = number of nodes examined (including the current node) to determine this

def DG_Min_Value(divisors, alpha, beta):
    if divisors == []:
        return [-1, 0, 1]
    else:
        current_u = beta

        min_u = beta
        current_a = 0
        best_a = 0

        # need to work on for loop
        total = 1
        for c in divisors:
            # need to work on min_val
            y = DG_Max_Value(result(c, divisors), alpha, beta)
            total += y[2]

            current_u = y[0]
            if current_u < min_u:
                min_u = current_u
                best_a = c
            if current_u <= alpha:
                return [min_u, best_a, total]

            if current_u < beta:
                beta = current_u

    return [min_u, best_a, total]


# =======================================================================
# Don't alter anything below here!
print("Welcome to the Divisor Game, version ALPHA-BETA!")

name = input("\nEnter your name:  ")
n = int(input("Enter positive integer n:  "))
turnNum = int(input("Enter 1 if you want to go first, 2 for second:  "))

divisor_game_agent(n, name, turnNum, DG_Max_Value)
