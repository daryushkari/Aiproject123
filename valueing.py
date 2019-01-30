
# x > 0 saat gard
# x < 0 pad saat gard

# oxo
# xoo
# ooo


def oxval(list, x):
    if (list[0][1] is list[1][2] is x) or (list[0][1] is list[1][0] is x):
        return 2
    if (list[2][1] is list[1][2] is x) or (list[2][1] is list[1][0] is x):
        return 2
    return 0

# 100
# 000
# 000


def corners(list, x):
    for i in list:
        if (i[0] is x) or (i[2] is x):
            return 1
    return 0


# 001
# 010
# 100

def xxval(list, x):
    if (list[1][1] is list[0][0] is list[2][2] is x) or (list[1][1] is list[0][2] is list[2][0] is x):
        return 3
    if (list[1][1] is list[0][0] is x) or (list[1][1] is list[2][2] is x):
        return 2
    if (list[1][1] is list[0][2] is x) or (list[1][1] is list[2][0] is x):
        return 2
    if list[1][1] is x:
        return 1
    return 0

#111
#001
#001


def horval(list, x):
    for i in range(3):
        for j in range(3):
            if i == 0 and j != 1:
                if list[i][j] is list[i+1][j] is list[i+2][j] is x:
                    return 3
            if i <= 1 and j != 1:
                if list[i][j] is list[i+1][j] is x:
                    return 2
            if j == 0 and i != 1:
                if list[i][j] is list[i][j+1] is list[i][j+2] is x:
                    return 3
            if j <= 1 and i != 1:
                if list[i][j] is list[i][j+1] is x:
                    return 2
    return 0


def horval_mid(list, x):
    for i in range(3):
        for j in range(3):
            if i == 0 and j == 1:
                if list[i][j] is list[i+1][j] is list[i+2][j] is x:
                    return 3
            if i <= 1 and j == 1:
                if list[i][j] is list[i+1][j] is x:
                    return 2
            if j == 0 and i == 1:
                if list[i][j] is list[i][j+1] is list[i][j+2] is x:
                    return 3
            if j <= 1 and i == 1:
                if list[i][j] is list[i][j+1] is x:
                    return 2
    return 0


def winner_value(mainlist, t):
    for i in range(6):
        for j in range(6):
            if i <= 1 and j <= 1:
                if mainlist[i][j] is mainlist[i+1][j+1] is mainlist[i+2][j+2] is mainlist[i+3][j+3] is mainlist[i+4][j+4] is t:
                    return 20
            if i <= 1 and j >= 4:
                if mainlist[i][j] is mainlist[i+1][j-1] is mainlist[i+2][j-2] is mainlist[i+3][j-3] is mainlist[i+4][j-4] is t:
                    return 20
            if j <= 1:
                if mainlist[i][j] is mainlist[i][j+1] is mainlist[i][j+2] is mainlist[i][j+3] is mainlist[i][j+4] is t:
                    return 20
            if i <= 1:
                if mainlist[i][j] is mainlist[i+1][j] is mainlist[i+2][j] is mainlist[i+3][j] is mainlist[i+4][j] is t:
                    return 20
    return 0


def devide_lists(mainlist, i, j):
    list = []
    for i in range(3*(i-1), 3*i):
        z = mainlist[i]
        list.append(z[3*(j-1):3*j])
    return list

###############################3


def ox_co_value(main_list, x):
    list1 = main_list["list1"]
    list2 = main_list["list2"]
    list3 = main_list["list3"]
    list4 = main_list["list4"]
    a = oxval(list2, x)+oxval(list3, x)+corners(list1, x)
    b = oxval(list2, x)+oxval(list3, x)+corners(list4, x)
    c = oxval(list1, x)+oxval(list4, x)+corners(list3, x)
    d = oxval(list1, x)+oxval(list4, x)+corners(list2, x)
    return max(a, b, c, d)


def xss_value(main_list, x):
    list1 = main_list["list1"]
    list2 = main_list["list2"]
    list3 = main_list["list3"]
    list4 = main_list["list4"]
    return max(xxval(list1, x)+xxval(list4, x), xxval(list2, x)+xxval(list3, x))


def horound_value(main_list, x):
    list1 = main_list["list1"]
    list2 = main_list["list2"]
    list3 = main_list["list3"]
    list4 = main_list["list4"]
    return max(horval(list1, x)+horval(list2, x), horval(list1, x)+horval(list3, x),
               horval(list2, x) + horval(list4, x), horval(list3, x) + horval(list4, x),
               horval_mid(list1, x) + horval_mid(list2, x), horval_mid(list1, x) + horval_mid(list3, x),
               horval_mid(list2, x) + horval_mid(list4, x), horval_mid(list3, x) + horval_mid(list4, x)
               )


def values(mainlist, x):
    main_list = {"list1": devide_lists(mainlist, 1, 1),
                 "list2": devide_lists(mainlist, 1, 2),
                 "list3": devide_lists(mainlist, 2, 1),
                 "list4": devide_lists(mainlist, 2, 2)}
    return max(ox_co_value(main_list, x), xss_value(main_list, x), horound_value(main_list, x),
               winner_value(mainlist, x))-winner_value(mainlist, 2)

