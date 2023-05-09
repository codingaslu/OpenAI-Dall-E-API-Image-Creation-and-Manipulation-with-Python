#GUI App to request pictures from Dall E
#pip3 install pillow

from tkinter import *
from PIL import Image, ImageTk
import urllib.request
from time import time
import openai

openai.api_key = "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"

window = Tk()
window.geometry("600x600")
window.title("Dall E App")

def dalle():
    request = ent.get()
    ent.delete(0,END)

    response = openai.Image.create(
        prompt=request,
        n=1,
        size="1024x1024"
    )

    response = response["data"][0]["url"]
    name = time()
    name = str(int(name)) + ".png"
    urllib.request.urlretrieve(response, name)

    image = Image.open(name)
    image = image.resize((450, 450))
    image = ImageTk.PhotoImage(image)
    lbl_image.configure(image=image)
    lbl_image.image = image
    lbl_request.configure(text=request)
    lbl_name.configure(text=name)


lbl_image = Label(window)
lbl_image.pack()

lbl_request = Label(window)
lbl_request.pack()

lbl_name = Label(window)
lbl_name.pack()

ent = Entry(window)
ent.pack()

btn_submit = Button(window, text="Submit", command=dalle).pack()

btn_exit = Button(window, text="Exit", command=window.destroy).pack()

window.mainloop()