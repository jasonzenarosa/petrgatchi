import asyncio
from collections import defaultdict
from Petrgotchi import Petrgotchi 

class Tasks:
    def __init__(self):
        self.hunger = None
        self.clean = None
        self.bored = None

class Event:
    def __init__(self):
        self.event_loop = asyncio.new_event_loop
        self.petrs = dict()
        self.tasks = defaultdict(Tasks) #[hunger, play, clean]

    async def register(self, username, **kargs):
        self.petrs[username] = Petrgotchi(**kargs)
        asyncio.gather(
            self.feed(username), self.clean(username), self.play(username))


    async def feed(self, username):
        try:
            await asyncio.sleep("time")
            if self.petrs[username].hunger() > 0:
                self.petrs[username].decrease_hunger()

        except asyncio.CancelledError:
            self.petrs[username].increase_hunger(self.event_loop.time())

        finally:
            await self.create_hunger(username)
            

    async def create_hunger(self, username):
        self.tasks[username].hunger = asyncio.create_task(self.feed())

        await asyncio.sleep(1)

        await self.tasks[username].hunger


    async def entertain(self, username):
        try:
            await asyncio.sleep("time")
            if self.petrs[username].entertainment() > 0:
                self.petrs[username].decrease_entertainment()

        except asyncio.CancelledError:
            self.petrs[username].increase_entertainment(self.event_loop.time())

        finally:
            await self.create_entertainment(username)
            
    async def create_entertain(self, username):
        self.tasks[username].hunger = asyncio.create_task(self.entertain())

        await asyncio.sleep(1)

        await self.tasks[username].entertain


    async def clean(self, username):
        try:
            await asyncio.sleep("time")
            if self.petrs[username].cleanliness() > 0:
                self.petrs[username].decrease_cleanliness()

        except asyncio.CancelledError:
            self.petrs[username].increase_cleanliness(self.event_loop.time())

        finally:
            await self.create_clean(username)
            
    async def create_clean(self, username):
        self.tasks[username].clean = asyncio.create_task(self.clean())

        await asyncio.sleep(1)

        await self.tasks[username].clean