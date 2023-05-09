#Edit an image that you feed DALL E
#The image must have a transparent layer

import openai

openai.api_key = "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"

response = openai.Image.create_edit(
    image=open("me.png", "rb"),
    prompt="with a dolphin",
    n=5,
    size="1024x1024"
)

for x in response["data"]:
    print(x["url"])
    print("")