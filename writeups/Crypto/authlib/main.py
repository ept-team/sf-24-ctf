from authlib.jose import jwt
from fastapi import FastAPI, Response, Request
from Crypto.PublicKey import RSA
import uvicorn
import time

app = FastAPI()
key = RSA.generate(2048)
PRIVATE_KEY = key.export_key(format='PEM')
PUBLIC_KEY = key.public_key().export_key(format='PEM')

@app.get("/")
async def root(response: Response):
    token = jwt.encode({'alg': 'RS256'}, {'admin': False, 'exp':int(time.time())+3600}, PRIVATE_KEY).decode()
    response.set_cookie(key="Authorization", value=token, httponly=True)
    return {"message": "Send a GET request to /flag with a valid admin token to get the flag!"}

@app.get("/flag")
async def flag(request: Request):
    try:
        token = request.cookies.get("Authorization")
        claims = jwt.decode(token, PUBLIC_KEY)
        assert claims["exp"] > int(time.time())
        assert claims.header["alg"] != "HS256"
        if claims["admin"]:
            return {
                "message": "Hello, admin! here is your flag.",
                "flag": open('flag.txt','r').read()
            }
        return {"message": "You are not admin, begone!"}
    except Exception:
        return {"message": "Invalid token."}


uvicorn.run(app, host="0.0.0.0", port=8000, reload=False)