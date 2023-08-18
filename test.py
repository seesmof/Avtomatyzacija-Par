import requests

url = 'https://www.deepl.com/en/translator?sl=auto&tl=en&q={text}'
text = 'Hello, how are you?'

translated_url = url.format(text=text)
response = requests.post(translated_url)


translated_text = response.text
print(translated_text)
