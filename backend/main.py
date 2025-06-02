from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

class UserInfo(BaseModel):
    first_name : str | None = None
    last_name : str | None = None

app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:80",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post('/')
def backend_response(info : UserInfo):
    if ( (info.first_name is None) and (info.last_name is None) ) or (info.first_name == '' and info.last_name == ''):
        response = 'Hi, mysterious stranger!'
    else:
        response = f'Hi, {info.first_name} {info.last_name}'
    return {'response' : response}