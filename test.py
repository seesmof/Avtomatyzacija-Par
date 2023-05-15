import time

t = time.localtime()
date = time.strftime("%b %dth %Y", t)
print(date.lower())
