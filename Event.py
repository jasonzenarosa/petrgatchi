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

    async def register(self, "username"):
        self.petrs["username"] = Petrgotchi(**kargs)
        # use asyncio.gather(feed(), shower(), play())
        

    async def feed(self, "username"):
        try:
            await asyncio.sleep("time")
            if self.petrs["username"].hunger() > 0:
                self.petrs["username"].decrease_hunger()

        except asyncio.CancelledError:
            self.petrs["username"].increase_hunger(self.event_loop.time())

        finally:
            await self.create_hunger("username")
            
    async def create_hunger(self, "username"):
        self.tasks["username"].hunger = asyncio.create_task(self.feed())

        await asyncio.sleep(1)

        await self.tasks["username"].hunger
