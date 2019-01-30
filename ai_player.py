from AI.valueing import values

import copy


def minmax(main_list, x, father_max):
    if x == 2:
        return values(main_list, 1)
    next_play = []
    max_value = -1
    min_value = 21
    for cc in range(-1, 2):
        for table in range(1, 5):
            for i in range(6):
                for j in range(6):
                    if main_list[i][j] == 0:
                        if x == 1:
                            play_list = game.choose(copy.deepcopy(main_list), i, j, 2)
                            play_list = game.choose_circle(play_list, table, cc)
                            min_value = min(minmax(play_list, 2, 0), min_value)
                            if father_max > min_value:
                                return min_value
                        else:
                            play_list = game.choose(copy.deepcopy(main_list), i, j, 1)
                            play_list = game.choose_circle(play_list, table, cc)
                            my_val = minmax(play_list, 1, max_value)
                            if my_val > max_value:
                                next_play = copy.deepcopy(play_list)
                                max_value = my_val
    if x == 0:
        return next_play
    if x == 1:
        return min_value

def alpha_cut(max_father, min_father):
    pass

def betha_cut(min_father, max_father):
    pass


cc = [[0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0],
      [1, 1, 1, 1, 0, 0],
      [0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0]]

