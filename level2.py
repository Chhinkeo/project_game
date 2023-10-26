import tkinter as tk
from PIL import Image, ImageTk

# ------------- Constants ---------------------
SCREEN_WIDTH = 1536
SCREEN_HEIGHT = 700

MOVE_INCREMENT = 10

GRAVITY_FORCE = 9
JUMP_FORCE = 23
SPEED = 6

TIMED_LOOP = 10

FULL_HP = 450

DIAMOND = 0

# -------------------------------- Variables ----------------------------------
keyPressed = []

# -------------------------------- Window -------------------------------------
window = tk.Tk()
window.geometry(str(SCREEN_WIDTH) + "x" + str(SCREEN_HEIGHT))
window.title("Movement")
window.attributes("-fullscreen", True)
window.configure(bg="black")

frame = tk.Frame(window, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
frame.pack()

canvas = tk.Canvas(frame, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
canvas.pack()

# -------------------------------- Game --------------------------------------
canvas.create_rectangle(0, 800, SCREEN_WIDTH, SCREEN_HEIGHT, fill="black", tags="PLATFORM")

bg = Image.open("image/bg1.jpg")
image_size = bg.resize((SCREEN_WIDTH, SCREEN_HEIGHT))
image = ImageTk.PhotoImage(image_size)
canvas.create_image(600, 350, image=image)

profile_file = Image.open("image/profile.png")
profile_size = profile_file.resize((125, 75))
profile = ImageTk.PhotoImage(profile_size)
profile_player = canvas.create_image(80, 80, image=profile)

red_hp = canvas.create_rectangle(150, 65, 450, 90, fill="red")

# HP____________________
green_hp = canvas.create_rectangle(150, 65, FULL_HP, 90, fill="#00dc00")


# ----dellet 1 line------
nb_dm = canvas.create_text(100, 150, text="Diamond: 0", fill="white", font=("Irish Grover", 20))



play_file = Image.open("image/ninja_right.png")
play_size = play_file.resize((55, 55))
play = ImageTk.PhotoImage(play_size)
player = canvas.create_image(150, 150, image=play)

play_left_file = Image.open("image/ninja_left.png")
play_left_size = play_left_file.resize((55, 55))
play_left = ImageTk.PhotoImage(play_left_size)

#-----------------------------------grass block-------------------------------------
grass1_file = Image.open("image/grass.png")

grass1_size = grass1_file.resize((600, 70))
grass1 = ImageTk.PhotoImage(grass1_size)
block_grass1 = canvas.create_image(30, 680, image=grass1, tags="PLATFORM")

grass2_size = grass1_file.resize((150, 120))
grass2 = ImageTk.PhotoImage(grass2_size)
block_grass2 = canvas.create_image(450, 580, image=grass2, tags="PLATFORM")

grass4_size = grass1_file.resize((100, 100))
grass4 = ImageTk.PhotoImage(grass4_size)
block_grass4 = canvas.create_image(50, 350, image=grass4, tags="PLATFORM")

grass6_size = grass1_file.resize((160, 70))
grass6 = ImageTk.PhotoImage(grass6_size)
block_grass6 =canvas.create_image(475, 320, image=grass6, tags="PLATFORM")

grass7_size = grass1_file.resize((160, 70))
grass7 = ImageTk.PhotoImage(grass7_size)
block_grass7 =canvas.create_image(625, 320, image=grass7, tags="PLATFORM")

grass8_size = grass1_file.resize((150, 25))
grass8 = ImageTk.PhotoImage(grass8_size)
block_grass8 =canvas.create_image(700, 500, image=grass8, tags="PLATFORM")

grass9_size = grass1_file.resize((900, 70))
grass9 = ImageTk.PhotoImage(grass9_size)
block_grass9 = canvas.create_image(1070, 650, image=grass9, tags="PLATFORM")

#----------------------------------challenges------------------------------------
wall_enemy1 = canvas.create_rectangle(700, 800, 700, 900, outline="")
wall_enemy2 = canvas.create_rectangle(1000, 1000, 1000, 1000, outline="")

wall_fire1 = canvas.create_rectangle(430, 300, 430, 300, outline="")
wall_fire2 = canvas.create_rectangle(670, 300, 670, 300, outline="")

wall_grass1 = canvas.create_rectangle(100, 200, 100, 200, outline="")
wall_grass2 = canvas.create_rectangle(270, 200, 270, 200, outline="")

# wall_eval =canvas.create_oval(400, 350, 450, 400, fill="red", outline="")
# wall_id1 = canvas.create_rectangle(0, 0, 900, 50, outline="")
# wall_id2 = canvas.create_rectangle(0, 200, 900, 300, outline="")

enemy_l_file =Image.open("image/enemy_right.png")
enemy_l_size =enemy_l_file.resize((100, 80))
enemy_l = ImageTk.PhotoImage(enemy_l_size)

enemy_r_file =Image.open("image/enemy_left.png")
enemy_r_size =enemy_r_file.resize((100, 80))
enemy_r = ImageTk.PhotoImage(enemy_r_size)
team_enemy = canvas.create_image(700, 585, image=enemy_r, tags="PLATFORM")

fire2_file = Image.open("image/fire1.png")
fire2_size = fire2_file.resize((50, 40))
fire2 = ImageTk.PhotoImage(fire2_size)
block_fire2 = canvas.create_image(700, 283, image=fire2, tags= "won")

thorn1_file = Image.open("image/Thorns 2.jpg")
thorn1_size = thorn1_file.resize((60, 195))
thorn1 = ImageTk.PhotoImage(thorn1_size)
block_thorn1 = canvas.create_image(500, 440, image=thorn1, tags="PLATFORM")

grass3_size = grass1_file.resize((100, 70))
grass3 = ImageTk.PhotoImage(grass3_size)
block_grass3 = canvas.create_image(225, 460, image=grass3, tags="PLATFORM")

#------------------fire block---------------------------------


fire2_file = Image.open("image/fire1.png")
fire2_size = fire2_file.resize((50, 40))
fire2 = ImageTk.PhotoImage(fire2_size)
block_fire2 = canvas.create_image(700, 283, image=fire2, tags="lost")






#------------------enemy block---------------------------------


enemy_l_file = Image.open("image/enemy_right.png")
enemy_l_size = enemy_l_file.resize((100, 80))
enemy_l = ImageTk.PhotoImage(enemy_l_size)

enemy_r_file = Image.open("image/enemy_left.png")
enemy_r_size = enemy_r_file.resize((100, 80))
enemy_r = ImageTk.PhotoImage(enemy_r_size)
team_enemy = canvas.create_image(700, 585, image=enemy_r, tags="PLATFORM")


#----------------challange------------------------------

wall_grass1_file = Image.open("image/wall_grass.jpg")
wall_grass1_size = wall_grass1_file.resize((100, 300))
wall_grass1_1 = ImageTk.PhotoImage(wall_grass1_size)
block_wall_grass1 = canvas.create_image(825, 250, image=wall_grass1_1, tags="PLATFORM")

#-----------------------------------gifts----------------------------------------
d1_file = Image.open("image/diamond.png")
d1_size = d1_file.resize((35, 35))
diamond = ImageTk.PhotoImage(d1_size)

dm1 = canvas.create_image(260, 400, image=diamond, tags = "diamond")
dm2 = canvas.create_image(550, 260, image=diamond, tags = "diamond")
dm3 = canvas.create_image(820, 70, image=diamond, tags = "diamond")

#----------------------------------function---------------------------------------
def check_movement(dx=0, dy=0, checkGround=False):
    coord = canvas.coords(player)
    platforms = canvas.find_withtag("PLATFORM")

    if coord[0] + dx < 0 or coord[0]+play.width() + dx > SCREEN_WIDTH:
        return False

    if checkGround:
        overlap = canvas.find_overlapping(coord[0], coord[1], coord[0]+20 + dx, coord[1] + 20 + dy)
    else:
        overlap = canvas.find_overlapping(coord[0]+dx, coord[1]+dy, coord[0] - dx, coord[1] - play.width())

    for platform in platforms:
        if platform in overlap:
            return False

    # coord = canvas.coords(player)
    # platforms = canvas.find_withtag("PLATFORM")
    # wonner = canvas.find_withtag("won")
    # for plf in wonner:
    #     if plf in overlap:
    #         global FULL_HP
    #         # check_winner()
    #         FULL_HP -= 50
    #
    #         print(FULL_HP)
    # for plf in wonner:
    #     if plf in overlap:
    #         return False
    # for platform in platforms:
    #     if platform in overlap:
    #         return False

    return True
#----------player to check diamond---------
def check_move_dimond():
    coord = canvas.coords(player)
    platforms = canvas.find_withtag("diamond")
    overlap = canvas.find_overlapping(coord[0], coord[1], coord[0] + play.width() , coord[1] + play.height() )
    for platform in platforms:
        if platform in overlap:
            return platform
    return 0
def jump(force):
    if force > 0:
        if check_movement(0, -force):
            canvas.move(player, 0, -force)
            window.after(TIMED_LOOP, jump, force-1)

def start_move(event):
    if event.keysym not in keyPressed:
        keyPressed.append(event.keysym)
        if len(keyPressed) == 1:
            move()

def move():
    global DIAMOND
    if not keyPressed == []:
        x = 0
        if "Left" in keyPressed:
            canvas.itemconfig(player, image=play_left)
            x -= SPEED
        if "Right" in keyPressed:
            canvas.itemconfig(player, image=play)
            x += SPEED
        if "space" in keyPressed and not check_movement(0, GRAVITY_FORCE, True):
            jump(JUMP_FORCE)
        if check_movement(x):
            canvas.move(player, x, 0)
        window.after(TIMED_LOOP, move)

        #--------plerc diamond-------
        dimond_id = check_move_dimond()
        if dimond_id > 0:
            DIAMOND += 1
            canvas.itemconfig(nb_dm, text="Diamond: " + str(DIAMOND))
            #--------dellet diamond---------
            canvas.delete("dimond_id")

def gravity():
    if check_movement(0, GRAVITY_FORCE, True):
        canvas.move(player, 0, GRAVITY_FORCE)
    window.after(TIMED_LOOP, gravity)

def stop_move(event):
    global keyPressed
    if event.keysym in keyPressed:
        keyPressed.remove(event.keysym)

def gravity_right():
    ball2_coords = canvas.coords(block_fire2)
    wall4_coords = canvas.coords(wall_fire2)
    if ball2_coords <= wall4_coords:
        canvas.move(block_fire2, 2, 0)
        canvas.after(20, gravity_right)
    else:
        gravity_left()

def gravity_left():
    ball2_coords = canvas.coords(block_fire2)
    wall3_coords = canvas.coords(wall_fire1)
    if ball2_coords >= wall3_coords:
        canvas.move(block_fire2, -2, 0)
        canvas.after(20, gravity_left)
    else:
        gravity_right()

def enemy_right():
    ball2_coords = canvas.coords(team_enemy)
    wall4_coords = canvas.coords(wall_enemy2)
    if ball2_coords <= wall4_coords:
        canvas.itemconfig(team_enemy, image=enemy_l)
        canvas.move(team_enemy, 2, 0)
        canvas.after(20, enemy_right)
    else:
        enemy_left()

def enemy_left():
    ball2_coords = canvas.coords(team_enemy)
    wall3_coords = canvas.coords(wall_enemy1)
    if ball2_coords >= wall3_coords:
        canvas.itemconfig(team_enemy, image=enemy_r)
        canvas.move(team_enemy, -2, 0)
        canvas.after(20, enemy_left)
    else:
        enemy_right()

def grass_right():
    ball2_coords = canvas.coords(block_grass3)
    wall4_coords = canvas.coords(wall_grass2)
    if ball2_coords <= wall4_coords:
        canvas.move(block_grass3, 1, 0)
        canvas.after(10, grass_right)
    else:
        grass_left()

def grass_left():
    ball2_coords = canvas.coords(block_grass3)
    wall3_coords = canvas.coords(wall_grass1)
    if ball2_coords >= wall3_coords:
        canvas.move(block_grass3, -1, 0)
        canvas.after(10, grass_left)
    else:
        grass_right() 

# def gravity_down():
#     ball_coords = canvas.coords(block_grass5)
#     wall2_coords = canvas.coords(wall_id2)
#     if ball_coords <= wall2_coords:
#         canvas.move(block_grass5, 0, -1)
#         canvas.after(10, gravity_down)
#     else:
#         gravity_up()
#
# def gravity_up():
#     ball_coords = canvas.coords(block_grass5)
#     wall1_coords = canvas.coords(wall_id1)
#     if ball_coords >= wall1_coords:
#         canvas.move(block_grass5, 0, 1)
#         canvas.after(30, gravity_up)
#     else:
#         gravity_down()


gravity()
# gravity_down()
gravity_right()
enemy_right()
grass_right()

window.bind("<Key>", start_move)
window.bind("<KeyRelease>", stop_move)

window.mainloop()


