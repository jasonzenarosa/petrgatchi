from aiohttp import web
from Event import Event
import asyncio

routes = web.RouteTableDef()
event = Event()

@routes.get("/register")
async def register(request):
    jso = request.json #mimetype must be application/json
    await event.register(username=jso["username"], ip=request.remote, sprite='normal_petr')

@routes.get("/Petrgotchi")
async def button_push(request):
    button = request.json.load()["button"]
    await exec(f"event.{button}({request.remote_addr})")

@routes.get("/check")
async def on_load(request):
    if request.remote_addr in event.petrs:
        return dict(event.petrs[request.remote_addr])
    return '0'

@routes.get("/user")
async def get_info(request):
    return dict(event.petrs[request.remote_addr])

app = web.Application()
app.add_routes(routes)

async def main():
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner)    
    await site.start()
    await asyncio.Event().wait()

asyncio.run(main())
    
    
    
# if __name__ == "__main__":
#     event = Event()
    # app.run(host='0.0.0.0', port=8000)

