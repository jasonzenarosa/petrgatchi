from flask import Flask, request
from flask_cors import CORS
from Event import Event
import asyncio

app = Flask(__name__)
CORS(app)

@app.route("/")
def test():
    return "Hello world"

@app.route("/register", methods=['POST'])
async def register():
    print(request.json)
    jso = request.json #mimetype must be application/json
    await event.register(username=jso["username"], ip=request.remote_addr, sprite='normal_petr')

@app.route("/Petrgotchi")
async def button_push():
    button = request.json.load()["button"]
    await exec(f"event.{button}({request.remote_addr})")

@app.route("/check")
async def on_load():
    print(request.remote_addr)
    if request.remote_addr in event.petrs:
        return dict(event.petrs[request.remote_addr])
    return '0'

@app.route("/user/<username>")
async def get_info():
    return dict(event.petrs[request.remote_addr])

if __name__ == "__main__":
    event = Event()
    app.run(host='0.0.0.0', port=8000)
    

