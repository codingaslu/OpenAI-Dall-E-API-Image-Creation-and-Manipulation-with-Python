#Download Images from Dall E

import openai
from time import time, sleep
import urllib.request

openai.api_key = "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"

response = openai.Image.create(
  prompt="A cartoon bunny",
  n=4,
  size="1024x1024"
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