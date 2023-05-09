#create variations of an image

import openai

openai.api_key = "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"

image = "musk2.png"
response = openai.Image.create_variation(
  image=open(image, "rb"),
  n=5,
  size="1024x1024"
)

print(response)

file = open("variation.html", "w")

file.write("<img style='height:250;width:250;border:3px solid green;' src='" + image + "'>")

for x in response["data"]:
    file.write("<img style='height:250;width:250;border:3px solid red;' src='" + x["url"] + "'>")
    print(x["url"])

file.close()
