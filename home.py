import tkinter as tk
from PIL import Image, ImageTk

# ------------- Constants ---------------------
SCREEN_WIDTH = 1536
SCREEN_HEIGHT = 800

TIMED_LOOP = 10

# ------------- Variables ---------------------
keyPressed = []

# ------------- Window ------------------------

window = tk.Tk()

window.geometry(str(SCREEN_WIDTH) + "x" + str(SCREEN_HEIGHT))
window.title("Movement")
window.configure(bg="black")
window.attributes("-fullscreen", True)

frame = tk.Frame(window, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
frame.pack()
window.geometry("750x280")
canvas = tk.Canvas(frame, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
canvas.pack()
bg = Image.open("image/home.jpg")
image = ImageTk.PhotoImage(bg)
canvas.create_image(600,450, image=image)

title = Image.open("image/name_game.png")
i = ImageTk.PhotoImage(title)
canvas.create_image(400,150, image=i)

def btn1_click():
    canvas.create_rectangle(10,10,100,100,fill='red')
canvas.tag_bind("btn", "<Button-1>", btn1_click) 
# canvas.create_image(680,540,image=btn1_click, tags="btn")

btn = Image.open("image/btn_play.png")
btn_size = btn.resize((300,100))
btn1 = ImageTk.PhotoImage(btn_size)
btn_click = canvas.create_image(400,300, image = btn1, tag = btn1_click)

window.mainloop()