import tkinter as tk
from PIL import Image, ImageTk

#-----constants-----#
SCREEN_WIDTH = 1536
SCREEN_HEIGHT = 700

GRAVITY_FORCE = 9
JUMP_FORCE = 20
SPEED = 6

TIMED_LOOP = 10

FULL_HP = 450

DIAMOND = 0
#----Variables---#
keyPressed = []

#---Window----#
window = tk.Tk()
window.geometry(str(SCREEN_WIDTH) + "x" + str(SCREEN_HEIGHT))
window.title("Movement")
window.attributes("-fullscreen", True)
window.configure(bg="black")

frame = tk.Frame(window, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
frame.pack()

canvas = tk.Canvas(frame, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
canvas.pack()

#----Game_Level-1-----#
canvas.create_rectangle(0,800,SCREEN_WIDTH, SCREEN_HEIGHT, fill="black", tags="PLATFORM")

bg = Image.open("image/bg_l1.png")
bg_size = bg.resize((SCREEN_WIDTH, SCREEN_HEIGHT))
image = ImageTk.PhotoImage(bg_size)
canvas.create_image(600, 350, image=image)


profile_file = Image.open("image/profile.png")
profile_size = profile_file.resize((125, 75))
profile = ImageTk.PhotoImage(profile_size)
profile_player = canvas.create_image(80, 80, image=profile)


red_hp = canvas.create_rectangle(150, 65, 450, 90, fill="red")
green_hp = canvas.create_rectangle(150, 65, FULL_HP, 90, fill="#00dc00")

nb_dm = canvas.create_text(100, 150, text="Diamond:", fill="white", font=("Irish Grover", 20))
nb = canvas.create_text(175, 150, text=DIAMOND, fill="white", font=("Irish Grover", 20))

play_file = Image.open("image/ninja_right.png")
play_size = play_file.resize((55, 55))
play = ImageTk.PhotoImage(play_size)
player = canvas.create_image(150, 150, image=play)

play_left_file = Image.open("image/ninja_left.png")
play_left_size = play_left_file.resize((55, 55))
play_left = ImageTk.PhotoImage(play_left_size)

diamond = tk.PhotoImage(file="image/diamond.png")
dm1 = canvas.create_image(290, 560, image=diamond)
dm2 = canvas.create_image(970, 580, image=diamond)
dm3 = canvas.create_image(1200, 340, image=diamond)


# d1_file = Image.open("image/diamond.png")
# d1_size = d1_file.resize((35, 35))
# d1 = ImageTk.PhotoImage(d1_size)
# dm1 = canvas.create_image(290, 560, image=d1)

# d2_file = Image.open("image/diamond.png")
# d2_size = d2_file.resize((35, 35))
# d2 = ImageTk.PhotoImage(d2_size)
# dm2 = canvas.create_image(970, 580, image=d2)

# d3_file = Image.open("image/diamond.png")
# d3_size = d3_file.resize((35, 35))
# d3 = ImageTk.PhotoImage(d3_size)
# dm3 = canvas.create_image(1200, 340, image=d3)

#---------stone block----------#
grass1_file = Image.open("image/grass.png")
grass1_size = grass1_file.resize((200, 70))
grass1 = ImageTk.PhotoImage(grass1_size)
block_grass1 = canvas.create_image(90, 500, image=grass1, tags="PLATFORM")

grass2_file = Image.open("image/grass.png")
grass2_size = grass2_file.resize((200, 70))
grass2 = ImageTk.PhotoImage(grass2_size)
block_grass2 = canvas.create_image(300, 600, image=grass2, tags="PLATFORM")


grass3_file = Image.open("image/grass.png")
grass3_size = grass3_file.resize((200, 70))
grass3 = ImageTk.PhotoImage(grass3_size)
block_grass3 = canvas.create_image(540, 500, image=grass3, tags="PLATFORM")


grass4_file = Image.open("image/grass.png")
grass4_size = grass4_file.resize((300, 70))
grass4 = ImageTk.PhotoImage(grass4_size)
block_grass4 = canvas.create_image(790, 420, image=grass4, tags="PLATFORM")


grass5_file = Image.open("image/grass.png")
grass5_size = grass4_file.resize((300, 70))
grass5 = ImageTk.PhotoImage(grass5_size)
block_grass5 = canvas.create_image(900, 620, image=grass5, tags="PLATFORM")


grass6_file = Image.open("image/grass.png")
grass6_size = grass6_file.resize((250, 70))
grass6 = ImageTk.PhotoImage(grass6_size)
block_grass6 = canvas.create_image(1150, 510, image=grass6, tags="PLATFORM")


grass7_file = Image.open("image/grass.png")
grass7_size = grass7_file.resize((250, 70))
grass7 = ImageTk.PhotoImage(grass7_size)
block_grass7 = canvas.create_image(1280, 380, image=grass7, tags="PLATFORM")

grass8_file = Image.open("image/grass.png")
grass8_size = grass8_file.resize((150, 60))
grass8 = ImageTk.PhotoImage(grass8_size)
block_grass8 = canvas.create_image(250, 340, image=grass8, tags="PLATFORM")


#------challange---------

canvas.create_rectangle(0, 696, SCREEN_WIDTH, SCREEN_HEIGHT, fill="red", tags="PLATFORM")

bomp1_file = Image.open("image/bomp1.png")
bomp_size = bomp1_file.resize((50, 50))
bomp1 = ImageTk.PhotoImage(bomp_size)
canvas.create_image(810, 372, image=bomp1)

bomp2_file = Image.open("image/bomp1.png")
bomp_size = bomp1_file.resize((50, 50))
bomp2 = ImageTk.PhotoImage(bomp_size)
canvas.create_image(1170, 460, image=bomp2)

bomp3_file = Image.open("image/bomp1.png")
bomp_size = bomp3_file.resize((50, 50))
bomp3 = ImageTk.PhotoImage(bomp_size)
canvas.create_image(875, 570, image=bomp3)

thorn1_file = Image.open("image/thorns 1.png")
thorn1_size = thorn1_file.resize((60, 60))
thorn1 = ImageTk.PhotoImage(thorn1_size)
canvas.create_image(630, 450, image=thorn1)

thorn2_file = Image.open("image/thorns 1.png")
thorn2_size = thorn2_file.resize((60, 60))
thorn2 = ImageTk.PhotoImage(thorn2_size)
canvas.create_image(840, 570, image=thorn2)

thorn3_file = Image.open("image/thorns 1.png")
thorn3_size = thorn3_file.resize((60, 60))
thorn3 = ImageTk.PhotoImage(thorn3_size)
canvas.create_image(1200, 460, image=thorn3)

thorn4_file = Image.open("image/thorns 1.png")
thorn4_size = thorn4_file.resize((40, 40))
thorn4 = ImageTk.PhotoImage(thorn4_size)
canvas.create_image(310, 300, image=thorn4)

#----------------function--------------

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
    return True

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
        
def gravity():
    if check_movement(0, GRAVITY_FORCE, True):
        canvas.move(player, 0, GRAVITY_FORCE)
    window.after(TIMED_LOOP, gravity)

def stop_move(event):
    global keyPressed
    if event.keysym in keyPressed:
        keyPressed.remove(event.keysym)

gravity()

window.bind("<Key>", start_move)
window.bind("<KeyRelease>", stop_move)

window.mainloop()











