from AI.valueing import devide_lists
from AI.ai_player import *
import copy


def circle(list, x):
    j = [list[0][:], list[1][:], list[2][:]]
    if x == 0:
        return list
    elif x > 0:
        for i in range(x):
            for a in range(0, 3):
                for b in range(0, 3):
                    j[a][b] = list[2-b][a]
            list = [j[0][:], j[1][:], j[2][:]]
    elif x < 0:
        for i in range(-x):
            for a in range(0, 3):
                for b in range(0, 3):
                    j[a][b] = list[b][2-a]
            list = [j[0][:], j[1][:], j[2][:]]
    return j


def choose_circle(mainlist, w, x):
    zz = copy.deepcopy(mainlist)
    if w == 1:
        z = circle(devide_lists(zz, 1, 1), x)
        for i in range(0,3):
            for j in range(0,3):
                zz[i][j] = z[i][j]
    if w == 2:
        z = circle(devide_lists(zz, 1, 2), x)
        for i in range(0,3):
            for j in range(0,3):
                zz[i][j+3] = z[i][j]
    if w == 3:
        z = circle(devide_lists(zz, 2, 1), x)
        for i in range(0,3):
            for j in range(0,3):
                zz[i+3][j] = z[i][j]
    if w == 4:
        z = circle(devide_lists(zz, 2, 2), x)
        for i in range(0,3):
            for j in range(0,3):
                zz[i+3][j+3] = z[i][j]
    return zz


def choose(list, x, y, t):
    if list[x][y] == 0:
        list[x][y] = t
    return list


def winner(list, t):
    for i in range(6):
        for j in range(6):
            if i <= 1 and j <= 1:
                if list[i][j] is list[i+1][j+1] is list[i+2][j+2] is list[i+3][j+3] is list[i+4][j+4] is t:
                    return True
            if i <= 1 and j >= 4:
                if list[i][j] is list[i+1][j-1] is list[i+2][j-2] is list[i+3][j-3] is list[i+4][j-4] is t:
                    return True
            if j <= 1:
                if list[i][j] is list[i][j+1] is list[i][j+2] is list[i][j+3] is list[i][j+4] is t:
                    return True
            if i <= 1:
                if list[i][j] is list[i+1][j] is list[i+2][j] is list[i+3][j] is list[i+4][j] is t:
                    return True
    return False

z = True
main_x = [[0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0],
          [1, 1, 1, 1, 0, 0],
          [0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0]]

while not z:
    pass

