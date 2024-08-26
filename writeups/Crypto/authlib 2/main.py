from authlib.jose import JsonWebEncryption
from fastapi import FastAPI, Body
import json

from Crypto.PublicKey import RSA
import uvicorn
import time

app = FastAPI()
key = RSA.generate(2048)
PUBLIC_KEY = key.public_key().export_key(format='PEM')
protected = {
    'alg': 'RSA-OAEP',
    'enc': 'A256GCM',
    'zip': 'DEF'
}

jwe = JsonWebEncryption()

FLAG = open('flag.txt', 'r').read()

@app.get("/")
async def root():
    return {
        "message": "Send a POST request to /encrypt with a JSON-serialized message you'd like to encrypt.",
        "example": """curl http://127.0.0.1:8000/ -X POST -d '{"message": "Hello, world!"}'""",
        "tip": "If you get error messages from pydantic, try setting the Content-Type header of your POST requests to `application/x-www-form-urlencoded`."
    }

@app.post("/encrypt")
async def encrypt(message: str = Body(...)):
    try:
        message = json.loads(message)
        plaintext = {
            "flag": FLAG,
            "message": message["message"]
        }
        payload = json.dumps(plaintext).encode()
        ciphertext = jwe.serialize_compact(protected, payload, PUBLIC_KEY).decode()
        response = {"ciphertext": ciphertext}
        return response
    except Exception:
        return {"response": "Invalid message."}

try:
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=False)
except KeyboardInterrupt:
    print("Quitting...")