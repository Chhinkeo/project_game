import tkinter as tk
from PIL import Image, ImageTk

#-----constants-----#
SCREEN_WIDTH= 1536
SCREEN_HEIGHT = 700

GRAVYTY_FORCE = 9
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

bg = Image.open("image/bg_level1.png")
bg_size = bg.resize((SCREEN_WIDTH,SCREEN_HEIGHT))
image = ImageTk.PhotoImage(bg_size)
canvas.create_image(600,350, image=image)


profile_file = Image.open("image/profile.png")
profile_size = profile_file.resize((125, 75))
profile = ImageTk.PhotoImage(profile_size)
profile_player = canvas.create_image(80,80, image=profile)


red_hp = canvas.create_rectangle(150,65,450,90, fill="red")
green_hp = canvas.create_rectangle(150,65,FULL_HP,90, fill="#00dc00")

nb_dm = canvas.create_text(100,150, text="Diamond:", fill="white", font=("Irish Grover", 20))
nb = canvas.create_text(175,150, text=DIAMOND, fill="white", font=("Irish Grover",20))

play_file = Image.open("image/ninja_right.png")
play_size = play_file.resize((55,55))
play = ImageTk.PhotoImage(play_size)
player = canvas.create_image(150,150, image=play)

play_left_file = Image.open("image/ninja_left.png")
play_left_size = play_left_file.resize((55,55))
play_left = ImageTk.PhotoImage(play_left_size)

d1_file = Image.open("image/diamond.png")
d1_size = d1_file.resize((35,35))
d1 = ImageTk.PhotoImage(d1_size)
dm1 = canvas.create_image(290,560, image=d1)

#---------stone block----------#
grass1_file = Image.open("image/grass.png")
grass_size = grass1_file.resize((200,70))
grass1 = ImageTk.PhotoImage(grass1_file)
block_grass1 = canvas.create_image(5,500, image=grass1, tags ="PLATFORM")

grass2_file = Image.open("image/grass.png")
grass2_size = grass2_file.resize((200,70))
grass2 = ImageTk.PhotoImage(grass2_size)
block_grass2 = canvas.create_image(300,600, image=grass2, tags = "PLATFORM")


grass3_file = Image.open("image/grass.png")
grass3_size = grass3_file.resize((200,70))
grass3 = ImageTk.PhotoImage(grass3_size)
block_grass3 = canvas.create_image(540,500, image=grass3, tags = "PLATFORM")


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


