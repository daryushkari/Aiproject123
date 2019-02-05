import tkinter as tk
from tkinter import messagebox
import math
from AI import game
import copy
from AI import ai_player
import time

x = 0
y = 0
prev_x = 0
prev_y = 0
counter = 0

# player is 2
# AI player is 1

root = tk.Tk()

root.title('The game')
root.geometry("500x500")
root.resizable(0, 0)
z = 0

main_x = [[0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0]]

B = tk.Button(root, text="easy difficulty", command=root.destroy)
BB = tk.Button(root, text="hard difficulty", command=root.destroy)

B.pack()
BB.pack()
root.mainloop()


def getorigin(event):
    global x, y
    x = event.x
    y = event.y
    return



root = tk.Tk()
root.bind("<Button 1>", getorigin)

canvas = tk.Canvas(root, width=900, height=780, borderwidth=0, highlightthickness=0, bg="#eee8aa")
canvas.grid()


def x_int(mlist):
    global x, y
    ii = math.floor((x - 125) / 100)
    jj = math.floor((y - 105) / 100)
    if (ii in range(0, 6)) and (jj in range(0, 6)):
        return game.choose(mlist, jj, ii, 2)
    return False


def cikin(mlist):
    global x, y
    w = 0
    ss = 0

    if (x in range(50, 75)) and (y in range(130, 155)):
        w = 1
        ss = -1
    elif (x in range(150, 175)) and (y in range(30, 55)):
        w = 1
        ss = 1

    elif (x in range(650, 675)) and (y in range(30, 55)):
        w = 2
        ss = -1
    elif (x in range(750, 775)) and (y in range(130, 155)):
        w = 2
        ss = 1

    elif (x in range(50, 75)) and (y in range(630, 655)):
        w = 3
        ss = 1
    elif (x in range(150, 175)) and (y in range(730, 755)):
        w = 3
        ss = -1

    elif (x in range(650, 675)) and (y in range(730, 755)):
        w = 4
        ss = 1
    elif (x in range(750, 775)) and (y in range(630, 655)):
        w = 4
        ss = -1

    elif (x in range(200, 500)) and (y in range(200, 500)):
        w = 1
        ss = 0

    else:
        return False

    return game.choose_circle(mlist, w, ss)


while True:
    canvas.delete("all")
    main_moraba = canvas.create_polygon(100, 80, 725, 80, 725, 705, 100, 705, fill="#ffcc99")
    oval = canvas.create_oval(50, 130, 75, 155, fill="white")
    ovalw = canvas.create_oval(150, 30, 175, 55, fill="black")

    # 4
    oval12 = canvas.create_oval(650, 730, 675, 755, fill="red")
    ovalw32 = canvas.create_oval(750, 630, 775, 655, fill="blue")

    # 3
    oval3232 = canvas.create_oval(50, 630, 75, 655, fill="red")
    ovalw43 = canvas.create_oval(150, 730, 175, 755, fill="white")

    #2
    oval3232r = canvas.create_oval(650, 30, 675, 55, fill="black")
    ovalw43r = canvas.create_oval(750, 130, 775, 155, fill="blue")

    lien1 = canvas.create_line(400, 80, 400, 705, fill="#994C00")
    lien12 = canvas.create_line(401, 80, 401, 705, fill="#994C00")
    lien13 = canvas.create_line(399, 80, 399, 705, fill="#994C00")

    lien112w = canvas.create_line(300, 80, 300, 705, fill="#994C00")
    lien112wsd = canvas.create_line(200, 80, 200, 705, fill="#994C00")
    lien112wx = canvas.create_line(500, 80, 500, 705, fill="#994C00")
    lien112wxc = canvas.create_line(600, 80, 600, 705, fill="#994C00")

    lien2 = canvas.create_line(100, 387, 725, 387, fill="#994C00")
    lien24 = canvas.create_line(100, 386, 725, 386, fill="#994C00")
    lien25 = canvas.create_line(100, 388, 725, 388, fill="#994C00")

    l32ie3n2 = canvas.create_line(100, 287, 725, 287, fill="#994C00")
    l23ien2 = canvas.create_line(100, 187, 725, 187, fill="#994C00")
    leeien2 = canvas.create_line(100, 487, 725, 487, fill="#994C00")
    lirren2 = canvas.create_line(100, 587, 725, 587, fill="#994C00")

    for i in range(6):
        for j in range(6):
            if main_x[j][i] == 1:
                oval = canvas.create_oval(i*100+125, j*100+105, i*100+175, j*100+155, fill="#331900")
            if main_x[j][i] == 2:
                oval = canvas.create_oval(i * 100 + 125, j * 100 + 105, i * 100 + 175, j * 100 + 155, fill="#ffffff")

    if counter == 0:
        ssdf = canvas.create_text(100, 10, text="مهره را انتخاب کنید")

    if counter == 1:
        ssdf = canvas.create_text(100, 10, text="جداول را بچرخانید")

    if counter == 2:
        ssdf = canvas.create_text(100, 10, text="نوبت کامپیوتر")

    root.update_idletasks()
    root.update()

    if game.winner(copy.deepcopy(main_x), 1):
        print("AI wins")
        time.sleep(3)
        break

    if game.winner(copy.deepcopy(main_x), 2):
        print("human wins")
        time.sleep(3)
        break

    if counter == 2:
        main_x = ai_player.minmax(copy.deepcopy(main_x), 0, 0)
        counter = 0

    if ((prev_x != x) or (prev_y != y)) and (counter == 0):
        prev_y = y
        prev_x = x

        if x_int(copy.deepcopy(main_x)):
            counter = 1
            main_x = x_int(copy.deepcopy(main_x))

    if ((prev_x != x) or (prev_y != y)) and (counter == 1):
        prev_y = y
        prev_x = x
        if cikin(copy.deepcopy(main_x)):
            counter = 2
            main_x = cikin(copy.deepcopy(main_x))


