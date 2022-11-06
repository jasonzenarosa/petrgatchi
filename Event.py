import asyncio
from collections import defaultdict
from Petrgotchi import Petrgotchi 

class _Tasks:
    def __init__(self):
        self.feed = None
        self.clean = None
        self.entertain = None

class Event:
    def __init__(self):
        self._event_loop = asyncio.new_event_loop
        self._petrs = dict()
        self._tasks = defaultdict(_Tasks) #[hunger, play, clean]

    async def register(self, ip, **kargs):
        self._petrs[ip] = Petrgotchi(ip=ip, **kargs)
        await asyncio.gather(
            self.feed_manager(ip),  
            self.entertain_manager(ip),
            self.clean_manager(ip)
            )


    async def _feed(self, ip):
        try:
            await asyncio.sleep(2) # update delay for hunger
            if self._petrs[ip].hunger() > 0:
                self._petrs[ip].decrease_hunger()
                print(self._petrs[ip].hunger())
                await self._feed(ip)
        except asyncio.CancelledError:
            self._petrs[ip].increase_hunger(self._event_loop.time())
            self._tasks[ip].feed = None
            await self.hunger_manager(ip)
            
    async def feed_manager(self, ip):
        if self._tasks[ip].feed is None:
            self._tasks[ip].feed = asyncio.create_task(self._feed(ip))
        else:
            await asyncio.sleep(1) 
            self._tasks[ip].feed.cancel()
            self._tasks[ip].feed = asyncio.create_task(self._feed(ip))
        await self._tasks[ip].feed

    async def _entertain(self, ip):
        try:
            await asyncio.sleep(2) # update delay for entertainment
            if self._petrs[ip].entertainment() > 0:
                self._petrs[ip].decrease_entertainment()
                print(self._petrs[ip].entertainment())
                await self._entertain(ip)
        except asyncio.CancelledError:
            self._petrs[ip].increase_entertainment(self._event_loop.time())
            self._tasks[ip].entertain = None
            await self.entertain_manager(ip)
            
    async def entertain_manager(self, ip):
        if self._tasks[ip].entertain is None:
            self._tasks[ip].entertain = asyncio.create_task(self._entertain(ip))
        else:
            await asyncio.sleep(1) 
            self._tasks[ip].entertain.cancel()
            self._tasks[ip].entertain = asyncio.create_task(self._entertain(ip))
        await self._tasks[ip].entertain


    async def _clean(self, ip):
        try:
            await asyncio.sleep(2) # update delay for cleanliness
            if self._petrs[ip].cleanliness() > 0:
                self._petrs[ip].decrease_cleanliness()
                print(self._petrs[ip].cleanliness(), end='\n\n')
                await self._clean(ip)
        except asyncio.CancelledError:
            self._petrs[ip].increase_cleanliness(self._event_loop.time())
            await self.clean_manager(ip)
            
    async def clean_manager(self, ip):
        if self._tasks[ip].clean is None:
            self._tasks[ip].clean = asyncio.create_task(self._clean(ip))
        else:
            await asyncio.sleep(1) 
            self._tasks[ip].clean.cancel()
            self._tasks[ip].clean = None
            self._tasks[ip].clean = asyncio.create_task(self._clean(ip))
            
        await self._tasks[ip].clean

    def get_petrs(self):
        return self.petrs

    

    
if __name__ == "__main__":
    event = Event()
    asyncio.run(event.register(ip="169.234.33.95", username = 'n', sprite="image"))

    