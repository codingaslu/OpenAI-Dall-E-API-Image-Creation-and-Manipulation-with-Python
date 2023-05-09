# GUI App to Modify pictures with Dall E
# pip3 install pillow

from tkinter import *
from PIL import Image, ImageTk
import urllib.request
from time import time
import openai

openai.api_key = "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"

window = Tk()
window.geometry("800x600")
window.title("Dall E App")

frame_pic = Frame(window)
frame_pic.pack()

frame_control = Frame(window)
frame_control.pack()

def dalle():
    request = ent.get()
    ent.delete(0, END)

    response = openai.Image.create_edit(
        image=open("musk.png", "rb"),
        prompt=request,
        n=1,
        size="1024x1024"
    )

    response = response["data"][0]["url"]
    name = time()
    name = str(int(name)) + ".png"
    urllib.request.urlretrieve(response, name)

    image = Image.open(name)
    image = image.resize((300, 300))
    image = ImageTk.PhotoImage(image)
    lbl_image_response.configure(image=image)
    lbl_image_response.image = image
    lbl_request.configure(text=request)
    lbl_name.configure(text=name)

image_start = Image.open("musk.png")
image_start = image_start.resize((300, 300))
image_start = ImageTk.PhotoImage(image_start)

lbl_image = Label(frame_pic, image=image_start)
lbl_image.pack(side=LEFT)

lbl_image_response = Label(frame_pic, image=image_start)
lbl_image_response.pack(side=LEFT)

lbl_request = Label(frame_control)
lbl_request.pack()

lbl_name = Label(frame_control)
lbl_name.pack()

ent = Entry(frame_control)
ent.pack(side=BOTTOM)

btn_submit = Button(window, text="Submit", command=dalle).pack()

btn_exit = Button(window, text="Exit", command=window.destroy).pack()

window.mainloop()