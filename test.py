import requests
import re

question = input(": ")

url = "https://www.phind.com/api/infer/creative"
data = {
    "question": question,
    "codeContext": "",
    "options": {
        "skill": "intermediate",
        "date": "14/04/2023",
        "language": "en-GB",
        "detailed": False,
        "creative": True
    }
}
headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
    "Accept": "*/*",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Origin": "https://www.phind.com",
    "Referer": "https://www.phind.com/search?q=Go+vs+Rust+vs+C%2B%2B&c=&source=searchbox&init=true",
    "sec-ch-ua": "\"Chromium\";v=\"112\", \"Google Chrome\";v=\"112\", \";Not A Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "Connection": "keep-alive",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site"
}

response = requests.post(url, json=data, headers=headers)
print(response.status_code)

data = response.text
text = data.replace("data: ", "")
text = text.replace("\n ", "")
text = f'''{text}'''
text = text.replace('''\r\n\r\n''', "")
text = text.replace('''\r\n\r''', " ")

print(text)
