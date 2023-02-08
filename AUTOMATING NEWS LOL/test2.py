import requests

url = "https://cdn.discordapp.com/attachments/1060597485682294894/1072085103733379072/idk.txt"

response = requests.get(url)
print(response.content)
