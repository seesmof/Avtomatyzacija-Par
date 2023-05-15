from gtts import gTTS

tts = gTTS("Hello, bro! Today is March 12, 2023 and the weather outside is about 12 degrees Celcius. Have a great day!")
tts.save("hello.mp3")
