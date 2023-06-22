import requests
import pandas

auth = {
    "Authorization": ""
}



r = requests.get("https://discord.com/api/v9/channels/1066360420400636088/messages",headers=auth)
print(r)
print(type(r))
user_ids = []
user_names = []
timelaps = []
contents = []

text = r.json()

for t in text:
    user_ids.append(t["id"])


for t in text:
    user_names.append(t["author"]["username"])



for t in text:
    timelaps.append(t["timestamp"][:-13])


for t in text:
    contents.append(t["content"])


data = {
    "Name": user_names,
    "Content": contents,
    "Time": timelaps,
    "Id": user_ids
}


df = pandas.DataFrame(data)

print(df)

df.to_csv("cringe_chat.csv")

