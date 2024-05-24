import requests
import json

url = "https://udayogra-images-to-video-v1.p.rapidapi.com/am"

querystring = {"state":"videoapi"}

payload = {
	"data": [
		{
			"url": "https://t3.ftcdn.net/jpg/05/15/63/82/360_F_515638234_Leo0UBEay0ozXWnObkkxLRNJXM9xhdWG.jpg",
			"delay": "3"
		},
		{
			"url": "https://t3.ftcdn.net/jpg/05/15/63/82/360_F_515638234_Leo0UBEay0ozXWnObkkxLRNJXM9xhdWG.jpg",
			"delay": "5"
		},
		{
			"url": "https://t3.ftcdn.net/jpg/05/15/63/82/360_F_515638234_Leo0UBEay0ozXWnObkkxLRNJXM9xhdWG.jpg",
			"delay": "4"
		}
	],
	"width": "760",
	"height": "400"
}
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "a366c2e67dmsh7e5a795330767afp134e91jsn48c5d2b8ddb7",
	"X-RapidAPI-Host": "udayogra-images-to-video-v1.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers, params=querystring)

print(response.text)


