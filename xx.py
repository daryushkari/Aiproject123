import random
import math


def copyGrid(grid):
    # To start a clean slate. i.e to ensure that change in newgrid doesn't change grid.
    # make a copy grid function for this.
    newgrid = [['.' for x in range(6)] for x in range(6)]
    for i in range(6):
        for j in range(6):
            newgrid[i][j] = grid[i][j]
    return newgrid


def rotate(grid, move):
    startCol = math.floor(((move[0] - 1) % 2) * 3)
    startRow = math.floor(((move[0] - 1) / 2) * 3)
    # For 4 and 2
    if move[0] % 2 is 0:
        startRow = startRow - 1

    newgrid = copyGrid(grid)
    if move[1] is 'R':
        for i in range(startRow, startRow + 3):
            for j in range(startCol, startCol + 3):
                newgrid[j + startRow - startCol][2 - i + startRow + startCol] = grid[i][j]

    elif move[1] is 'L':
        for i in range(startRow, startRow + 3):
            for j in range(startCol, startCol + 3):
                newgrid[2 - j + startRow + startCol][i - startRow + startCol] = grid[i][j]

    return newgrid


def makeMove(grid, color, move):
    startCol = math.floor(((move[0] - 1) % 2) * 3)
    startRow = math.floor(((move[0] - 1) / 2) * 3)
    if move[0] % 2 is 0:
        startRow = startRow - 1

    if move[1] <= 3:
        if grid[startRow][(startCol + move[1] - 1)] is '.':
            grid[startRow][(startCol + move[1] - 1)] = color
    elif move[1] <= 6:
        if grid[startRow + 1][(startCol + move[1] - 4)] is '.':
            grid[startRow + 1][(startCol + move[1] - 4)] = color
    elif move[1] <= 9:
        if grid[startRow + 2][(startCol + move[1]) - 7] is '.':
            grid[startRow + 2][(startCol + move[1]) - 7] = color

    return


def checkWinColor(c, grid):
    win = False
    for i in range(6):
        for j in range(6):
            if grid[i][j] is c:
                if j < 2 and i >= 2:
                    win = (grid[i][j] is grid[i][j + 1] is grid[i][j + 2] is grid[i][j + 3] is grid[i][j + 4] is c)
                elif j < 2:
                    win = ((grid[i][j] is grid[i + 1][j + 1] is grid[i + 2][j + 2] is grid[i + 3][j + 3] is grid[i + 4][
                        j + 4] is c) or win)
                elif i < 2:
                    win = ((grid[i][j] is grid[i + 1][j] is grid[i + 2][j] is grid[i + 3][j] is grid[i + 4][
                        j] is c) or win)
            break
    return win


def checkWin(grid):
    winW = checkWinColor('w', grid)
    winB = checkWinColor('b', grid)

    if winW and (not winB):
        return "P1 wins!"
    elif winW:
        return "A Tie"
    elif winB:
        return "P2 Wins!"

    if '.' not in (i[0] for i in initialGrid):
        return "A Tie!"

    return None


def scoreFrom(playscore, color, grid, pointer):
    if pointer[0] >= 6 or pointer[1] >= 6:
        return playscore

    if playscore >= 5:
        return playscore

    if grid[pointer[0]][pointer[1]] is not color:
        return playscore

    else:
        scoreh = scoreFrom(playscore + 1, color, grid, ((pointer[0] + 1), (pointer[1])))
        scorev = scoreFrom(playscore + 1, color, grid, ((pointer[0]), (pointer[1] + 1)))
        scored = scoreFrom(playscore + 1, color, grid, ((pointer[0] + 1), (pointer[1] + 1)))
        return max(scoreh, scorev, scored, playscore)


def scoreGrid(color, grid):
    playscore = 0
    for i in range(6):
        for j in range(6):
            temp = 0
            if grid[i][j] is color:
                temp = scoreFrom(0, color, grid, (i, j))
            playscore = max(playscore, temp)
    return playscore


def allPossibleMoves(grid):
    moves = []
    block = 0
    pos = 0
    for i in range(6):
        for j in range(6):
            if grid[i][j] is '.':
                if j < 3:
                    if i < 3:
                        block = 1
                    else:
                        block = 3
                else:
                    if i < 3:
                        block = 2
                    else:
                        block = 4

                startRow = math.floor(((block - 1) / 2) * 3)
                startCol = math.floor(((block - 1) % 2) * 3)
                if block % 2 is 0:
                    startRow = startRow - 1
                pos = (3 * (i - startRow)) + (j - startCol) + 1

                for x in [1, 2, 3, 4]:
                    moves.append(((block, pos), (x, 'L')))
                    moves.append(((block, pos), (x, 'R')))

    return moves


"""Move generator using MinMax Algorithm"""


def genMinMax(moves, playerno, grid, depth, alpha, beta, maximizing):
    colors = ['b', 'w']
    if moves is None or moves is []:
        moves = []
        moves.append(genMoveRandom(grid))
    if depth is 0:
        return (moves[-1], (scoreGrid(colors[playerno - 1], grid)))
    if checkWin(grid) is not None:
        return (moves[-1], 5)

    if maximizing:
        bestScoreAndMove = (genMoveRandom(grid), -5)
        for move in allPossibleMoves(grid):
            tempGrid = copyGrid(grid)
            makeMove(tempGrid, colors[playerno - 1], move[0])
            tempGrid = rotate(tempGrid, move[1])
            moves.append(move)
            score = genMinMax(moves, playerno, tempGrid, depth - 1, alpha, beta, False)[1]
            if bestScoreAndMove[1] < score:
                bestScoreAndMove = (move, score)
            alpha = max(score, beta)
            if beta <= alpha:
                break
        return bestScoreAndMove

    else:
        bestScoreAndMove = (genMoveRandom(grid), 5)
        for move in allPossibleMoves(grid):
            if moves is None:
                moves = []
            tempGrid = copyGrid(grid)
            makeMove(tempGrid, colors[-(playerno)], move[0])
            tempGrid = rotate(tempGrid, move[1])
            moves = moves.append(move)
            score = genMinMax(moves, playerno, tempGrid, depth - 1, alpha, beta, True)[1]
            if bestScoreAndMove[1] > score:
                bestScoreAndMove = (move, score)
            beta = min(score, beta)
            if beta <= alpha:
                break

        return bestScoreAndMove


"""Random move generator """


def genMoveRandom(grid):
    dropBlock = random.choice(range(1, 4))
    dropPos = random.choice(range(1, 9))

    valid = False
    while not valid:
        startCol = math.floor(((dropBlock - 1) % 2) * 3)
        startRow = math.floor(((dropBlock - 1) / 2) * 3)
        if dropBlock % 2 is 0:
            startRow = startRow - 1

        if dropPos <= 3:
            if grid[startRow][(startCol + dropPos - 1)] is '.':
                valid = True
                break

        elif dropPos <= 6:
            if grid[startRow + 1][(startCol + dropPos - 4)] is '.':
                valid = True
                break

        elif dropPos <= 9:
            if grid[startRow + 2][(startCol + dropPos - 7)] is '.':
                valid = True
                break

        dropBlock = random.choice(range(1, 4))
        dropPos = random.choice(range(1, 9))

    rotBlock = random.choice(range(1, 4))
    rotDir = random.choice(['L', 'R'])

    move = ((dropBlock, dropPos), (rotBlock, rotDir))
    return move


def printGrid(grid):
    row = ''
    for i in range(6):
        if i is 3:
            print('=======')
        for j in range(6):
            if j is 3:
                row += '|'
            row += grid[i][j]

        print(row)
        row = ''
    print('--------------------------')


""" The main function that will call all the other functions"""


def input2move(input):
    temp = input.split(' ')
    move = []
    move.append(temp[0].split('/'))
    move.append(list(temp[1]))
    move[0] = [int(x) for x in move[0]]
    move[1][0] = int(move[1][0])
    return move


def Pentago(userplayer, p1, p2, grid):
    if checkWin(grid) is not None:
        print(checkWin(grid))
        return
    print("Current grid")
    printGrid(grid)
    updateGrid = grid
    currmove = []
    # player 1 move
    if userplayer is 1:
        print(p1, "Make your move: ")
        inputmove = input()
        currmove = input2move(inputmove)

    else:
        print(p1, " is making it's move")
        currmove = genMinMax(list(), userplayer, updateGrid, 3, -5, 5, True)[0]
    print(currmove)
    makeMove(updateGrid, 'w', currmove[0])
    updateGrid = rotate(updateGrid, currmove[1])

    printGrid(updateGrid)
    if checkWin(updateGrid) is not None:
        print(checkWin(updateGrid))
        return

    # player 2 move
    if userplayer is 2:
        print(p2, "Make your move: ")
        inputmove = input()
        currmove = input2move(inputmove)

    else:
        print(p2, " is making it's move")
        currmove = genMinMax(list(), userplayer, updateGrid, 3, -5, 5, True)[0]

    print(currmove)
    makeMove(updateGrid, 'b', currmove[0])
    updateGrid = rotate(updateGrid, currmove[1])
    if checkWin(updateGrid) is not None:
        print(checkWin(updateGrid))
        return

    Pentago(userplayer, p1, p2, updateGrid)
    return


print("The starting grid is")

initialGrid = [['.' for x in range(6)] for x in range(6)]
printGrid(initialGrid)
userplayer = int(input("Do you wish to be player 1 or 2:"))
p1 = input('Enter a name of player 1: ')
p2 = input('Enter a name of player 2: ')
Pentago(userplayer, p1, p2, initialGrid)
# genMinMax(moves = list(), playerno = 1, grid = initialGrid, depth = 3, alpha = -5, beta = 5, maximizing = True)
