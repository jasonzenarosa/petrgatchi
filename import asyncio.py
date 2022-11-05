import asyncio
from collections import defaultdict
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

    async def register("params"):
        self.petrs[]Petrgatchi(**kargs)
        # use asyncio.gather(feed(), shower(), play())

    # async def feed(self, "params"):
    #     self.tasks[].hunger = asyncio.create_task(create_hunger())
    #     self.tasks[][0].cancel()
    #     self.tasks[][0] = self.create_task(self.create_hunger())
    #     try:
    #         await asyncio.sleep("value")
    #     except asyncio.CancelledError:
            
    # async def create_hunger(self, "params"):
    #     try:
    #         await asyncio.sleep("time")
    #     except asyncio.CancelledError:
    #         self.petrs["username"].
    #         if self.petrs["username"] == 0:
    #             pass # do some interaction with the UI that demonstrates it has died
 
        


