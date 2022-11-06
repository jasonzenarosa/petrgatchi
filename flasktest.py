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
    await exec(f"event.{button}({request.remote})")

@routes.get("/check")
async def on_load(request):
    if request.remote in event.petrs:
        return dict(event.petrs[request.remote])
    return '0'

@routes.get("/user")
async def get_info(request):
    return dict(event.petrs[request.remote])

app = web.Application()
app.add_routes(routes)



async def main():
    runner = web.AppRunner(app) # holds information about app
    print(1)
    await runner.setup()
    print(2)
    site = web.TCPSite(runner, host="127.0.0.1", port=5500)    
    print(3)
    await site.start()
    # await asyncio.sleep(4)
    # await event.register(username='x', ip='1.1', sprite='normal_petr')
    asyncio.get_event_loop().stop()
    asyncio.get_event_loop().close()
    asyncio.get_event_loop().run_forever()

asyncio.run(main())
    