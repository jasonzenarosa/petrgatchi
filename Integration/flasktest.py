from flask import Flask, request
from flask_cors import CORS
from Event import Event
import asyncio

app = Flask(__name__)
CORS(app)

@app.route("/test")
def test():
    return "Hello world"

@app.route("/register")
async def register():
    jso = request.json.load() #mimetype must be application/json
    await event.register(username=jso["username"], ip=request.remote_addr, petr_sprite=jso["petr_sprite"])

@app.route("/Petrgotchi")
async def button_push():
    button = request.json.load()["button"]
    await exec(f"event.{button}({request.remote_addr})")

@app.route("/check")
async def on_load():
    if request.remote_addr in event.petrs:
        return dict(event.petrs[request.remote_addr])
    return 0

@app.route("/user/<username>")
async def get_info():
    return dict(event.petrs[request.remote_addr])

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
    event = Event()

