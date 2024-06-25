""" 
MeetingTime
< hour: int
< minute: int
< day: str

OnlineClass
< name: str
< time: MeetingTime
< denomination: str
< meeting_link: str
< meeting_passcode: optional[str]

try pydantic, sqlite and fastapi for backend and nextjs with bulma for frontend
"""

from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()


@app.get("/")
def testing_root() -> str:
    return "Hallelujah thank YOU Jesus Christ our Holy Lord GOD Almighty"
