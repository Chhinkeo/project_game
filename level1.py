import tkinter as tk
from PIL import Image , ImageTk

# ------------- Constants ---------------------
SCREEN_WIDTH = 1536
SCREEN_HEIGHT = 700

GRAVITY_FORCE = 9
JUMP_FORCE = 23
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

# ------------- Game --------------------------
canvas.create_rectangle(0,800,SCREEN_WIDTH,SCREEN_HEIGHT,fill="black",tags="PLATFORM")

bg = Image.open("bg2.jpg")
image_size = bg.resize((SCREEN_WIDTH,SCREEN_HEIGHT))
image = ImageTk.PhotoImage(image_size)
canvas.create_image(600,350, image=image)

profile_file = Image.open("profile.png")
profile_size = profile_file.resize((125, 75))
profile = ImageTk.PhotoImage(profile_size)
profile_player = canvas.create_image(80, 80, image = profile)

red_hp = canvas.create_rectangle(150,65,450,90, fill="red")
green_hp = canvas.create_rectangle(150,65,FULL_HP,90, fill="#00dc00")

nb_dm = canvas.create_text(100, 150, text = "Diamond: ", fill="white", font=("Irish Grover", 20))
nb = canvas.create_text(175,150, text = DIAMOND, fill = "white", font = ("Irish Grover", 20))

play_file = Image.open("ninja_right.png")
play_size = play_file.resize((55, 55))
play = ImageTk.PhotoImage(play_size)
player = canvas.create_image(100, 150, image=play)

#------------------grass block---------------------------------
canvas.create_rectangle(120,660,275,661, fill="black", tags = "PLATFORM")
grass1_file = Image.open("grass.png")
grass1_size = grass1_file.resize((200,65))
grass1 = ImageTk.PhotoImage(grass1_size)
block_grass1 = canvas.create_image(200,650, image=grass1)



def check_movement(dx=0, dy=0, checkGround=False):
    coord = canvas.coords(player)
    platforms = canvas.find_withtag("PLATFORM")

    if coord[0] + dx < 0 or coord[0]+play.width() + dx > SCREEN_WIDTH:
        return False

    if checkGround:
        overlap = canvas.find_overlapping(coord[0], coord[1], coord[0]+play.width() , coord[1]+play.height() + dy)
    else:
        overlap = canvas.find_overlapping(coord[0]+dx, coord[1]+dy, coord[0]+dx, coord[1]+play.width())

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
            x -= SPEED
        if "Right" in keyPressed:
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