from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware

from datetime import datetime, timedelta
from jose import JWTError, jwt
import os
import json

app = FastAPI()
origins = [ "http://localhost:3000", "http://fomocoin" ]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Set up JWT authentication
JWT_SECRET = "secret"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Sample user data for testing purposes
# database = {
#     "adam": {
#         "username": "adam",
#         "password": "password",
#         "wallet": 2.8,
#         "disabled": False,
#     },
#     "ian": {
#         "username": "ian",
#         "password": "password",
#         "disabled": False,
#     }
# }

# Generate the access token for a user
def GenerateToken(data:dict, delta:timedelta):
    toEncode = data.copy()
    expire = datetime.utcnow() + delta
    toEncode.update({"exp": expire})

    jsonwebtoken = jwt.encode(toEncode, JWT_SECRET, algorithm=ALGORITHM)
    return jsonwebtoken

# Find user in database
def GetUser(username:str):
    with open("database.json", 'r') as f:
        database = json.load(f)

    if username in database:
        user = database[username]
        return user

    return None

# Obtain token
@app.post("/token")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user = GetUser(form.username)

    if not user: 
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    if user["password"] != form.password: 
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    tokenExpiresIn = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    token = GenerateToken(data={"sub": user["username"]}, delta=tokenExpiresIn)
    return {"access_token": token, "token_type": "bearer"}


# Protected route that requires authentication
@app.get("/protected")
async def hydrate(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid authentication credentials")

        user = GetUser(username)
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")

    return user


# Get the secret identifier
@app.get("/2bb80d537b1da3e38bd30361aa855686bde0eacd7162fef6a25fe97bf527a25b")
async def GetSecret():
    return JWT_SECRET

