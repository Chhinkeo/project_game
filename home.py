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
# canvas.create_text(380, 130, text="NINJA's Advanture", fill="white", font=("Irish Grover", 50))

# play_btn = tk.Button(300,500, text="PLAY NOW", command="level1.py", bg="#733700")
# play_btn.pack()

window.mainloop()