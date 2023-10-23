import tkinter as tk
<<<<<<< HEAD
from PIL import Image, ImageTk

#-----constants-----#
SCREEN_WIDTH= 1536
SCREEN_HEIGHT = 700

GRAVYTY_FORCE = 9
=======
from PIL import Image , ImageTk

# ------------- Constants ---------------------
SCREEN_WIDTH = 1536
SCREEN_HEIGHT = 700

GRAVITY_FORCE = 9
>>>>>>> 27f6f3cfdf778dd75d2886270b70a17286c8d21a
JUMP_FORCE = 20
SPEED = 6

TIMED_LOOP = 10

FULL_HP = 450

DIAMOND = 0
<<<<<<< HEAD
#----Variables---#
keyPressed = []

#---Window----#
=======
# ------------- Variables ---------------------
keyPressed = []

# ------------- Window ------------------------

>>>>>>> 27f6f3cfdf778dd75d2886270b70a17286c8d21a
window = tk.Tk()
window.geometry(str(SCREEN_WIDTH) + "x" + str(SCREEN_HEIGHT))
window.title("Movement")
window.attributes("-fullscreen", True)
window.configure(bg="black")

<<<<<<< HEAD
=======

>>>>>>> 27f6f3cfdf778dd75d2886270b70a17286c8d21a
frame = tk.Frame(window, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
frame.pack()

canvas = tk.Canvas(frame, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
canvas.pack()

<<<<<<< HEAD
#----Game_Level-1-----#
canvas.create_rectangle(0,800,SCREEN_WIDTH, SCREEN_HEIGHT, fill="black", tags="PLATFORM")

bg = Image.open("image/bg_level1.png")
bg_size = bg.resize((SCREEN_WIDTH,SCREEN_HEIGHT))
image = ImageTk.PhotoImage(bg_size)
canvas.create_image(600,350, image=image)


profile_file = Image.open("image/profile.png")
profile_size = profile_file.resize((125, 75))
profile = ImageTk.PhotoImage(profile_size)
profile_player = canvas.create_image(80,80, image=profile)

=======
# ----------------- Game --------------------------
canvas.create_rectangle(0,800,SCREEN_WIDTH,SCREEN_HEIGHT,fill="black",tags="PLATFORM")

bg = Image.open("image/bg2.jpg")
image_size = bg.resize((SCREEN_WIDTH,SCREEN_HEIGHT))
image = ImageTk.PhotoImage(image_size)
canvas.create_image(600,350, image=image)

profile_file = Image.open("image/profile.png")
profile_size = profile_file.resize((125, 75))
profile = ImageTk.PhotoImage(profile_size)
profile_player = canvas.create_image(80, 80, image = profile)
>>>>>>> 27f6f3cfdf778dd75d2886270b70a17286c8d21a

red_hp = canvas.create_rectangle(150,65,450,90, fill="red")
green_hp = canvas.create_rectangle(150,65,FULL_HP,90, fill="#00dc00")

<<<<<<< HEAD
nb_dm = canvas.create_text(100,150, text="Diamond:", fill="white", font=("Irish Grover", 20))
nb = canvas.create_text(175,150, text=DIAMOND, fill="white", font=("Irish Grover",20))

play_file = Image.open("image/ninja_right.png")
play_size = play_file.resize((55,55))
play = ImageTk.PhotoImage(play_size)
player = canvas.create_image(150,150, image=play)

play_left_file = Image.open("image/ninja_left.png")
play_left_size = play_left_file.resize((55,55))
play_left = ImageTk.PhotoImage(play_left_size)

#-----------------diamond------------------------------------
d1_file = Image.open("image/diamond.png")
d1_size = d1_file.resize((35,35))
d1 = ImageTk.PhotoImage(d1_size)
dm1 = canvas.create_image(290,560, image=d1)

<<<<<<<< HEAD:level3.py
d2_file = Image.open("image/diamond.png")
d2_size = d2_file.resize((35,35))
d2 = ImageTk.PhotoImage(d2_size)
dm2 = canvas.create_image(980,600, image=d2)

#------------------grass block---------------------------------
========
#---------stone block----------#
>>>>>>>> 27f6f3cfdf778dd75d2886270b70a17286c8d21a:level1.py
grass1_file = Image.open("image/grass.png")
grass_size = grass1_file.resize((200,70))
grass1 = ImageTk.PhotoImage(grass1_file)
block_grass1 = canvas.create_image(5,500, image=grass1, tags ="PLATFORM")
=======
nb_dm = canvas.create_text(100, 150, text = "Diamond: ", fill="white", font=("Irish Grover", 20))
nb = canvas.create_text(175,150, text = DIAMOND, fill = "white", font = ("Irish Grover", 20))

play_file = Image.open("image/ninja_right.png")
play_size = play_file.resize((55, 55))
play = ImageTk.PhotoImage(play_size)
player = canvas.create_image(150, 150, image=play)

play_left_file = Image.open("image/ninja_left.png")
play_left_size = play_left_file.resize((55, 55))
play_left = ImageTk.PhotoImage(play_left_size)

d1_file = Image.open("image/diamond.png")
d1_size = d1_file.resize((35,35))
d1 = ImageTk.PhotoImage(d1_size)
dm1 = canvas.create_image(490,560, image=d1)

#------------------grass block---------------------------------
grass1_file = Image.open("image/grass.png")
grass1_size = grass1_file.resize((200,70))
grass1 = ImageTk.PhotoImage(grass1_size)
block_grass1 = canvas.create_image(200,650, image=grass1, tags = "PLATFORM")
>>>>>>> 27f6f3cfdf778dd75d2886270b70a17286c8d21a

grass2_file = Image.open("image/grass.png")
grass2_size = grass2_file.resize((200,70))
grass2 = ImageTk.PhotoImage(grass2_size)
<<<<<<< HEAD
block_grass2 = canvas.create_image(300,600, image=grass2, tags = "PLATFORM")

<<<<<<<< HEAD:level3.py
grass3_file = Image.open("image/grass.png")
grass3_size = grass3_file.resize((100,70))
grass3 = ImageTk.PhotoImage(grass3_size)
block_grass3 = canvas.create_image(630,520, image=grass3, tags = "PLATFORM")

grass4_file = Image.open("image/grass.png")
grass4_size = grass4_file.resize((100,70))
grass4 = ImageTk.PhotoImage(grass4_size)
block_grass4 = canvas.create_image(750,585, image=grass4, tags = "PLATFORM")

grass5_file = Image.open("image/grass.png")
grass5_size = grass5_file.resize((150,70))
grass5 = ImageTk.PhotoImage(grass5_size)
block_grass5 = canvas.create_image(950,640, image=grass5, tags = "PLATFORM")

grass6_file = Image.open("image/grass.png")
grass6_size = grass6_file.resize((150,70))
grass6 = ImageTk.PhotoImage(grass6_size)
block_grass6 = canvas.create_image(1200,585, image=grass6, tags = "PLATFORM")

grass7_file = Image.open("image/grass.png")
grass7_size = grass7_file.resize((150,70))
grass7 = ImageTk.PhotoImage(grass7_size)
block_grass7 = canvas.create_image(1100,420, image=grass7, tags = "PLATFORM")

grass8_file = Image.open("image/grass.png")
grass8_size = grass8_file.resize((80,70))
grass8 = ImageTk.PhotoImage(grass8_size)
block_grass8 = canvas.create_image(1300,500, image=grass8, tags = "PLATFORM")
=======
block_grass2 = canvas.create_image(450,595, image=grass2, tags = "PLATFORM")
>>>>>>> 27f6f3cfdf778dd75d2886270b70a17286c8d21a

#----------------challange------------------------------
thorns1_file = Image.open("image/thorns.png")
thorns1_size = thorns1_file.resize((200,40))
thorns1 = ImageTk.PhotoImage(thorns1_size)
canvas.create_image(350,675, image=thorns1)

<<<<<<< HEAD
fire1_file = Image.open("Image/fire2.png")
fire1_size = fire1_file.resize((50,50))
fire1 = ImageTk.PhotoImage(fire1_size)
canvas.create_image(905, 610, image = fire1)
#-----------------function-------------------------------
========

grass3_file = Image.open("image/grass.png")
grass3_size = grass3_file.resize((200,70))
grass3 = ImageTk.PhotoImage(grass3_size)
block_grass3 = canvas.create_image(540,500, image=grass3, tags = "PLATFORM")
>>>>>>>> 27f6f3cfdf778dd75d2886270b70a17286c8d21a:level1.py


grass4_file = Image.open("image/grass.png")
grass4_size = grass4_file.resize((200,70))
grass4 = ImageTk.PhotoImage(grass4_size)
block_grass4 = canvas.create_image(790,420, image=grass4, tags = "PLATFORM")


grass5_file = Image.open("image/grass.png")
grass5_size = grass4_file.resize((200,70))
grass5 = ImageTk.PhotoImage(grass5_size)
block_grass5 = canvas.create_image(900,620, image=grass5, tags = "PLATFORM")


#------challange---------
fire1_file = Image.open("image/fire2.png")
fire1_size = fire1_file.resize((60,70))
fire1 = ImageTk.PhotoImage(fire1_size)
canvas.create_image(370,545, image=fire1)



window.mainloop()


=======
#-----------------function-------------------------------

def check_movement(dx=0, dy=0, checkGround=False):
    coord = canvas.coords(player)
    platforms = canvas.find_withtag("PLATFORM")

    if coord[0] + dx < 0 or coord[0]+play.width() + dx > SCREEN_WIDTH:
        return False

    if checkGround:
        overlap = canvas.find_overlapping(coord[0], coord[1], coord[0]+20+ dx , coord[1]+ 20 + dy)
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
>>>>>>> 27f6f3cfdf778dd75d2886270b70a17286c8d21a
