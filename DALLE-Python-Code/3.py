#Create an HTML Image Gallery from Dall E

import openai
from time import time, sleep
import urllib.request
import os

openai.api_key = "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"

response = openai.Image.create(
    prompt="A taco on mars",
    n=3,
    size="256x256"
)

print("All URLs")
for x in response["data"]:
    name = time()
    name = str(int(name)) + ".png"
    urllib.request.urlretrieve(x["url"], name)
    print(x["url"])
    print(name)
    print("****")
    sleep(1.5)

img_list = []
for x in os.listdir():
    if x.endswith(".png"):
        img_list.append(x)

try:
    os.remove("gallery.html")
except:
    pass

file = open("gallery.html", "a")
file.write("<style> img:hover {transform:scale(2);} img {height:250px; width:250px;}</style>")

img_list.sort(reverse=True)
for x in img_list:
    input = "<img src='" + x + "'>\n"
    file.write(input)
file.close()