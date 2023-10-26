import tkinter as tk
from PIL import Image, ImageTk

# ------------- Constants ---------------------
SCREEN_WIDTH = 1536
SCREEN_HEIGHT = 700

GRAVITY_FORCE = 9
JUMP_FORCE = 20
SPEED = 6

TIMED_LOOP = 10

FULL_HP = 450

DIAMOND = 0
# ------------- Variables ---------------------
keyPressed = []

# ------------- Window ------------------------

window = tk.Tk()
window.geometry(str(SCREEN_WIDTH) + "x" + str(SCREEN_HEIGHT))
window.title("Movement")
window.attributes("-fullscreen", True)
window.configure(bg="black")


frame = tk.Frame(window, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
frame.pack()

canvas = tk.Canvas(frame, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
canvas.pack()

# ----------------- Game --------------------------
canvas.create_rectangle(0, 800, SCREEN_WIDTH, SCREEN_HEIGHT, fill="black", tags="PLATFORM")

bg = Image.open("image/bg2.jpg")
image_size = bg.resize((SCREEN_WIDTH, SCREEN_HEIGHT))
image = ImageTk.PhotoImage(image_size)
canvas.create_image(600, 350, image=image)

profile_file = Image.open("image/profile.png")
profile_size = profile_file.resize((125, 75))
profile = ImageTk.PhotoImage(profile_size)
profile_player = canvas.create_image(80, 80, image=profile)

red_hp = canvas.create_rectangle(150, 65, 450, 90, fill="red")
green_hp = canvas.create_rectangle(150, 65, FULL_HP, 90, fill="#00dc00")

nb_dm = canvas.create_text(100, 150, text="Diamond: 0", fill="white", font=("Irish Grover", 20))

play_file = Image.open("image/ninja_right.png")
play_size = play_file.resize((55, 55))
play = ImageTk.PhotoImage(play_size)
player = canvas.create_image(150, 150, image=play)

play_left_file = Image.open("image/ninja_left.png")
play_left_size = play_left_file.resize((55, 55))
play_left = ImageTk.PhotoImage(play_left_size)

temple_file = Image.open("image/win.png")
temple_size = temple_file.resize((60,60))
temple = ImageTk.PhotoImage(temple_size)
temple_win = canvas.create_image(1250,95, image=temple)

#-----------------diamond------------------------------------
d1_file = Image.open("image/diamond.png")
d1_size = d1_file.resize((35, 35))
d1 = ImageTk.PhotoImage(d1_size)
dm1 = canvas.create_image(490,555, image=d1, tags="diamond")

d2_file = Image.open("image/diamond.png")
d2_size = d2_file.resize((35,35))
d2 = ImageTk.PhotoImage(d2_size)
dm2 = canvas.create_image(1100,380, image=d2, tags="diamond")

d3_file = Image.open("image/diamond.png")
d3_size = d3_file.resize((35,35))
d3 = ImageTk.PhotoImage(d3_size)
dm3 = canvas.create_image(500,290, image=d3, tags="diamond")

#------------------grass block---------------------------------
grass1_file = Image.open("image/grass.png")
grass1_size = grass1_file.resize((200,55))
grass1 = ImageTk.PhotoImage(grass1_size)
block_grass1 = canvas.create_image(200, 650, image=grass1, tags="PLATFORM")

grass2_file = Image.open("image/grass.png")
grass2_size = grass2_file.resize((200,55))
grass2 = ImageTk.PhotoImage(grass2_size)
block_grass2 = canvas.create_image(450, 595, image=grass2, tags="PLATFORM")

grass3_file = Image.open("image/grass.png")
grass3_size = grass3_file.resize((100,55))
grass3 = ImageTk.PhotoImage(grass3_size)
block_grass3 = canvas.create_image(630, 520, image=grass3, tags="PLATFORM")

grass4_file = Image.open("image/grass.png")
grass4_size = grass4_file.resize((100,55))
grass4 = ImageTk.PhotoImage(grass4_size)
block_grass4 = canvas.create_image(750, 585, image=grass4, tags="PLATFORM")

grass5_file = Image.open("image/grass.png")
grass5_size = grass5_file.resize((150,55))
grass5 = ImageTk.PhotoImage(grass5_size)
block_grass5 = canvas.create_image(950, 640, image=grass5, tags="PLATFORM")

grass6_file = Image.open("image/grass.png")
grass6_size = grass6_file.resize((150,55))
grass6 = ImageTk.PhotoImage(grass6_size)
block_grass6 = canvas.create_image(1200, 585, image=grass6, tags="PLATFORM")

grass7_file = Image.open("image/grass.png")
grass7_size = grass7_file.resize((200,55))
grass7 = ImageTk.PhotoImage(grass7_size)
block_grass7 = canvas.create_image(1100, 420, image=grass7, tags="PLATFORM")

grass8_file = Image.open("image/grass.png")
grass8_size = grass8_file.resize((80,55))
grass8 = ImageTk.PhotoImage(grass8_size)
block_grass8 = canvas.create_image(1300, 500, image=grass8, tags="PLATFORM")

grass9_file = Image.open("image/grass.png")
grass9_size = grass9_file.resize((100,55))
grass9 = ImageTk.PhotoImage(grass9_size)
block_grass9 = canvas.create_image(900,420, image=grass9, tags = "PLATFORM")

grass10_file = Image.open("image/grass.png")
grass10_size = grass10_file.resize((500,55))
grass10 = ImageTk.PhotoImage(grass10_size)
block_grass10 = canvas.create_image(560, 330, image=grass10, tags="PLATFORM")

grass11_file = Image.open("image/grass.png")
grass11_size = grass11_file.resize((200,55))
grass11 = ImageTk.PhotoImage(grass11_size)
block_grass11 = canvas.create_image(990,230, image=grass11, tags = "PLATFORM")

grass12_file = Image.open("image/grass.png")
grass12_size = grass12_file.resize((350,55))
grass12 = ImageTk.PhotoImage(grass12_size)
block_grass12 = canvas.create_image(1250,150, image=grass12, tags = "PLATFORM")

#----------------challange------------------------------
thorns1_file = Image.open("image/thorns.png")
thorns1_size = thorns1_file.resize((200, 40))
thorns1 = ImageTk.PhotoImage(thorns1_size)
canvas.create_image(350, 675, image=thorns1)

thorns2_file = Image.open("image/thorns.png")
thorns2_size = thorns2_file.resize((200, 40))
thorns2 = ImageTk.PhotoImage(thorns2_size)
canvas.create_image(500, 675, image=thorns2)

thorns3_file = Image.open("image/thorns.png")
thorns3_size = thorns3_file.resize((200, 40))
thorns3 = ImageTk.PhotoImage(thorns3_size)
canvas.create_image(650, 675, image=thorns3)

thorns4_file = Image.open("image/thorns.png")
thorns4_size = thorns4_file.resize((200, 40))
thorns4 = ImageTk.PhotoImage(thorns4_size)
canvas.create_image(800, 675, image=thorns4)

thorns5_file = Image.open("image/thorns.png")
thorns5_size = thorns5_file.resize((200, 40))
thorns5 = ImageTk.PhotoImage(thorns5_size)
canvas.create_image(950, 675, image=thorns5)

thorns6_file = Image.open("image/thorns.png")
thorns6_size = thorns6_file.resize((200, 40))
thorns6 = ImageTk.PhotoImage(thorns6_size)
canvas.create_image(1100, 675, image=thorns6)

thorns7_file = Image.open("image/thorns.png")
thorns7_size = thorns7_file.resize((200, 40))
thorns7 = ImageTk.PhotoImage(thorns7_size)
canvas.create_image(1250, 675, image=thorns7)

fire1_file = Image.open("Image/fire2.png")
fire1_size = fire1_file.resize((50, 50))
fire1 = ImageTk.PhotoImage(fire1_size)
canvas.create_image(905, 610, image=fire1)

fire2_file = Image.open("image/fire2.png")
fire2_size = fire2_file.resize((50,50))
fire2 = ImageTk.PhotoImage(fire2_size)
canvas.create_image(700,290, image=fire2)

wall_id3 = canvas.create_rectangle(350, 300, 350, 300, outline="")
wall_id4 = canvas.create_rectangle(700, 300, 700, 300, outline="")

enemy_l_file = Image.open("image/enemy_r.png")
enemy_l_size = enemy_l_file.resize((100, 80))
enemy_l = ImageTk.PhotoImage(enemy_l_size)

enemy_r_file = Image.open("image/enemy_l.png")
enemy_r_size = enemy_r_file.resize((100, 80))
enemy_r = ImageTk.PhotoImage(enemy_r_size)
team_enemy = canvas.create_image(700, 265, image=enemy_r, tags="PLATFORM")

#-----------------function-------------------------------

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
    dimond_id = check_move_dimond()
    if dimond_id > 0:
        DIAMOND += 1
        canvas.itemconfig(nb_dm, text="Diamond: " + str(DIAMOND))
        canvas.delete("dimond_id")
    diamond_id = get_diamond()
    if diamond_id>0:
        coord = canvas.coords(diamond_id)
        canvas.delete(diamond_id)   
        
def gravity():
    if check_movement(0, GRAVITY_FORCE, True):
        canvas.move(player, 0, GRAVITY_FORCE)
    window.after(TIMED_LOOP, gravity)

def stop_move(event):
    global keyPressed
    if event.keysym in keyPressed:
        keyPressed.remove(event.keysym)

gravity()

def gravity_right():
    ball2_coords = canvas.coords(team_enemy)
    wall4_coords = canvas.coords(wall_id4)
    if ball2_coords <= wall4_coords:
        canvas.itemconfig(team_enemy, image=enemy_l)
        canvas.move(team_enemy, 4, 0)
        canvas.after(20, gravity_right)
    else:
        gravity_left()


def gravity_left():
    ball2_coords = canvas.coords(team_enemy)
    wall3_coords = canvas.coords(wall_id3)
    if ball2_coords >= wall3_coords:
        canvas.itemconfig(team_enemy, image=enemy_r)
        canvas.move(team_enemy, -4, 0)
        canvas.after(20, gravity_left)
    else:
        gravity_right()
gravity_right()

def get_diamond():
    coord = canvas.coords(player)
    diamonds = canvas.find_withtag("diamond")
    overlap = canvas.find_overlapping(coord[0], coord[1], coord[0]+ play.width(),coord[1]+play.height())
    for dm in diamonds:
        if dm in overlap:
            return dm
        return 0

window.bind("<Key>", start_move)
window.bind("<KeyRelease>", stop_move)

window.mainloop()