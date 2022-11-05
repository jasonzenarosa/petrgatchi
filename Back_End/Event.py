import asyncio
from collections import defaultdict
from Petrgotchi import Petrgotchi 

def start():
    return Event()

class Tasks:
    def __init__(self):
        self.feed = None
        self.clean = None
        self.entertain = None

class Event:
    def __init__(self):
        self.event_loop = asyncio.new_event_loop()
        self.petrs = dict()
        self.tasks = defaultdict(Tasks) #[hunger, play, clean]

    async def register(self, **kargs):
        self.petrs[kargs[ip]] = Petrgotchi(**kargs)
        await asyncio.gather(
            self.feed_manager(kargs[ip]),  
            self.entertain_manager(kargs[ip]),
            self.clean_manager(kargs[ip])
            )


    async def feed(self, id):
        try:
            await asyncio.sleep(2)
            if self.petrs[id].hunger() > 0:
                self.petrs[id].decrease_hunger()
                print(self.petrs[ip].hunger())
                await self.feed(ip)
        except asyncio.CancelledError:
            self.petrs[ip].increase_hunger(self.event_loop.time())
            self.tasks[ip].feed = None
            await self.hunger_manager(ip)
            
    async def feed_manager(self, ip):
        if self.tasks[ip].feed is None:
            self.tasks[ip].feed = asyncio.create_task(self.feed(ip))
        else:
            await asyncio.sleep(1) 
            self.tasks[ip].feed.cancel()
            self.tasks[ip].feed = asyncio.create_task(self.feed(ip))
        await self.tasks[ip].feed

    async def entertain(self, ip):
        try:
            await asyncio.sleep(2)
            if self.petrs[ip].entertainment() > 0:
                self.petrs[ip].decrease_entertainment()
                print(self.petrs[ip].entertainment())
                await self.entertain(ip)
        except asyncio.CancelledError:
            self.petrs[ip].increase_entertainment(self.event_loop.time())
            self.tasks[ip].entertain = None
            await self.entertain_manager(ip)
            
    async def entertain_manager(self, ip):
        if self.tasks[ip].entertain is None:
            self.tasks[ip].entertain = asyncio.create_task(self.entertain(ip))
        else:
            await asyncio.sleep(1) 
            self.tasks[ip].entertain.cancel()
            self.tasks[ip].entertain = asyncio.create_task(self.entertain(ip))
        await self.tasks[ip].feed


    async def clean(self, ip):
        try:
            await asyncio.sleep(2)
            if self.petrs[ip].cleanliness() > 0:
                self.petrs[ip].decrease_cleanliness()
                print(self.petrs[ip].cleanliness(), end='\n\n')
                await self.clean(ip)
        except asyncio.CancelledError:
            self.petrs[ip].increase_cleanliness(self.event_loop.time())
            await self.clean_manager(ip)
            
    async def clean_manager(self, ip):
        if self.tasks[ip].clean is None:
            self.tasks[ip].clean = asyncio.create_task(self.clean(ip))
        else:
            await asyncio.sleep(1) 
            self.tasks[ip].clean.cancel()
            self.tasks[ip].clean = None
            self.tasks[ip].clean = asyncio.create_task(self.clean(ip))
            
        await self.tasks[ip].clean

    

    
if __name__ == "__main__":
    event = Event()
    asyncio.run(event.register(ip="169.234.33.95", ip="n", sprite="image"))

    