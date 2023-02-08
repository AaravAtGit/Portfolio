import requests 

headers = {
    "authorization": "OTg1ODM5NzYxNDU1NDQ4MTE0.Gj28Bo.zqaq0OXx9YEzzksvdyM-nFBZI7N9DPRrHRByQM"
}

r = requests.get("https://discord.com/api/v9/channels/1060597485682294894/messages",headers=headers)
print(r.json())

