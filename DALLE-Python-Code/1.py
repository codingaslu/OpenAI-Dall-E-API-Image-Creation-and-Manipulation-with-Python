#Requests images from Dall E

import openai

openai.api_key = "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"

response = openai.Image.create(
  prompt="A ostrich riding an elephant",
  n=1,
  size="1024x1024"
)

print("JSON Response")
print(response)

print("First/ Only URL Result")
print(response["data"][0]["url"])

print("All URLs")
for x in response["data"]:
    print(x["url"])
    print("****")