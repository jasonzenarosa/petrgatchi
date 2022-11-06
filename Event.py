import asyncio
from collections import defaultdict
from Petrgotchi import Petrgotchi 

class Tasks:
    def __init__(self):
        self.feed = None
        self.clean = None
        self.entertain = None

class Event:
    def __init__(self):
        self.event_loop = asyncio.new_event_loop
        self.petrs = dict()
        self.tasks = defaultdict(Tasks) #[hunger, play, clean]

    async def register(self, username, **kargs):
        self.petrs[username] = Petrgotchi(username=username, **kargs)
        await asyncio.gather(
            self.feed_manager(username),  
            self.entertain_manager(username),
            self.clean_manager(username)
            )


    async def feed(self, username):
        try:
            await asyncio.sleep(20)
            if self.petrs[username].hunger() > 0:
                self.petrs[username].decrease_hunger()
                print(self.petrs[username].hunger())
                await self.feed(username)
        except asyncio.CancelledError:
            self.petrs[username].increase_hunger(self.event_loop.time())
            self.tasks[username].feed = None
            await self.hunger_manager(username)
            
    async def feed_manager(self, username):
        if self.tasks[username].feed is None:
            self.tasks[username].feed = asyncio.create_task(self.feed(username))
        else:
            await asyncio.sleep(1) 
            self.tasks[username].feed.cancel()
            self.tasks[username].feed = asyncio.create_task(self.feed(username))
        await self.tasks[username].feed

    async def entertain(self, username):
        try:
            await asyncio.sleep(20)
            if self.petrs[username].entertainment() > 0:
                self.petrs[username].decrease_entertainment()
                print(self.petrs[username].entertainment())
                await self.entertain(username)
        except asyncio.CancelledError:
            self.petrs[username].increase_entertainment(self.event_loop.time())
            self.tasks[username].entertain = None
            await self.entertain_manager(username)
            
    async def entertain_manager(self, username):
        if self.tasks[username].entertain is None:
            self.tasks[username].entertain = asyncio.create_task(self.entertain(username))
        else:
            await asyncio.sleep(1) 
            self.tasks[username].entertain.cancel()
            self.tasks[username].entertain = asyncio.create_task(self.entertain(username))
        await self.tasks[username].feed


    async def clean(self, username):
        try:
            await asyncio.sleep(20)
            if self.petrs[username].cleanliness() > 0:
                self.petrs[username].decrease_cleanliness()
                print(self.petrs[username].cleanliness(), end='\n\n')
                await self.clean(username)
        except asyncio.CancelledError:
            self.petrs[username].increase_cleanliness(self.event_loop.time())
            await self.clean_manager(username)
            
    async def clean_manager(self, username):
        if self.tasks[username].clean is None:
            self.tasks[username].clean = asyncio.create_task(self.clean(username))
        else:
            await asyncio.sleep(1) 
            self.tasks[username].clean.cancel()
            self.tasks[username].clean = None
            self.tasks[username].clean = asyncio.create_task(self.clean(username))
            
        await self.tasks[username].clean

    

    
if __name__ == "__main__":
    event = Event()
    asyncio.run(event.register(username="169.234.33.95", ip="n", sprite="image"))

    