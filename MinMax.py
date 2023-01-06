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
    for i in range(1, n + 1):
        if n % i == 0:
            numList.append(i)

    print(f'\nHere are the remaining numbers: {numList}')
    if turnNum == 1:
        a = int(input(f'{name} , pick a number from the list above: '))
        checkNum = True
        k = 1
    # =========================================
    # when agents turn then I have to go to DG_max_value
    elif turnNum == 2:
        x = agent(numList)
        print(f'Agent picked {x[1]}.')
        print(f'(Agent visited {x[2]} nodes to determine this.)')
        numList = result(x[1], numList)
        checkNum = False
        k = 0

    while numList != []:
        # I am only checking for user number is in list or not
        if checkNum == True:
            track = 0

            if a in numList:
                track = 1
                visit = True

            elif track == 0:
                a = int(input(f'{name} ,pick something that is in the list: '))
                visit = False

        # store remaining value

        indexP = 0
        if track == 1:
            # this goes to until entering number
            while a != numList[indexP]:
                indexP = indexP + 1

            while indexP >= 0:
                if a % numList[indexP] == 0:
                    numList.remove(numList[indexP])
                indexP = indexP - 1

        if numList != [] and visit == True:
            print(f'\nHere are the remaining numbers: {numList}')

            if k == 0:
                a = int(input(f'{name}, pick a number from the list above : '))
                checkNum = True
                k = 1
                track = 1

            elif k == 1:
                x = DG_Max_Value(numList)
                print(f'Agent picked {x[1]} ')
                print(f'(Agent visited {x[2]} nodes to determine this.)')
                numList = result(x[1], numList)
                k = 0
                checkNum = False
                track = 0

    if k == 1:
        print(f'\n {name},you  lose ! Agent,you win ! ')
    else:
        print(f'\n Agent ,you lose  ! {name},you  win !')


#  to get remaining divisors
def result(value, div):
    newList = []
    for i in div:
        if value % i != 0:
            newList.append(i)

    return newList


# =======================================================================
# DG_Max_Value:
#
# Input: divisors, a list of the remaining divisors.
#
# Returns a list:  [u, a, numNodes]
#
#    where u = the maximum utility that can be achieved at this node (divisors)
#          a = the action (divisor to pick) that achieves maximum utility
#          numNodes = number of nodes examined (including the current node) to determine this

def DG_Max_Value(divisors):
    if divisors == []:
        return [1, 0, 1]
    else:
        current_u = - math.inf
        max_u = -math.inf
        best_a = 0
        total = 1
        for c in divisors:

            remDiv = divisors.copy()
            x = DG_Min_Value(result(c, remDiv))
            total += x[2]
            current_u = x[0]
            if current_u > max_u:
                max_u = current_u
                best_a = c

    return [max_u, best_a, total]


# =======================================================================
# DG_Min_Value:
#
# Input: divisors, a list of the remaining divisors.
#
# Returns a list:  [u, a, numNodes]
#
#    where u = the minimum utility that can be achieved at this node (divisors)
#          a = the action (divisor to pick) that achieves minimum utility
#          numNodes = number of nodes examined (including the current node) to determine this

def DG_Min_Value(divisors):
    if divisors == []:
        return [-1, 0, 1]
    else:
        current_u = math.inf
        min_u = math.inf
        best_a = 0
        total = 1
        for c in divisors:
            # need to work on min_val
            remDive = divisors.copy()
            y = DG_Max_Value(result(c, remDive))
            total += y[2]

            current_u = y[0]
            if current_u < min_u:
                min_u = current_u
                best_a = c

    return [min_u, best_a, total]


# =======================================================================
# Don't alter anything below here!
print("Welcome to the Divisor Game, version MINIMAX!")

name = input("\nEnter your name:  ")
n = int(input("Enter positive integer n:  "))
turnNum = int(input("Enter 1 if you want to go first, 2 for second:  "))

divisor_game_agent(n, name, turnNum, DG_Max_Value)
