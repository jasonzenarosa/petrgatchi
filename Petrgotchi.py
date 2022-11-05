import json


MAX = 10000

HUNGER_INCREASE_RATE = 50
HUNGER_DECREASE_RATE = 5

ENTERTAINMENT_INCREASE_RATE = 100
ENTERTAINMENT_DECREASE_RATE = 1

CLEANLINESS_INCREASE_RATE = 5000
CLEANLINESS_DECREASE_RATE = 2


class Petrgotchi:
    def __init__(self, **kwargs):
        self._ip = kwargs["ip"]
        self._username = kwargs["username"]
        self._mood = "neutral"
        self._petr_sprite = kwargs["sprite"]
        self._hunger_value = MAX
        self._clean_value = MAX
        self._entertainment_value = MAX

        self._last_feed_time = None
        self._last_clean_time = None
        self._last_entertainment_time = None
    

    def __dict__(self) -> str:
        return json.dumps({"ip": self._ip, "username": self._username, "mood": self._mood, "petr_sprite": self._petr_sprite, "hunger_value": self._hunger_value, "clean_value": self._clean_value, "entertainment_value": self._entertainment_value, "last_feed": self._last_feed_time, "last_clean": self._last_clean_time, "last_entertainment": self._last_entertainment_time}, indent=4)
    

    def hunger(self) -> int:
        return self._hunger_value
    

    def entertainment(self) -> int:
        return self._entertainment_value
    

    def cleanliness(self) -> int:
        return self._clean_value

    
    def last_feed(self) -> float or None:
        return self._last_feed_time
    

    def last_clean(self) -> float or None:
        return self._last_clean_time
    

    def last_entertainment(self) -> float or None:
        return self._last_entertainment_time


    def increase_hunger(self, time) -> None:
        # Increase the hunger
        if self._hunger_value > MAX - HUNGER_INCREASE_RATE:
            self._hunger_value = MAX
        else:
            self._hunger_value += HUNGER_INCREASE_RATE
        
        # Update the mood if necessary
        if self._mood != "neutral":
            if self._entertainment_value == 0:
                self._mood = "sad"
            elif self._clean_value == 0:
                self._mood = "stinky"
        else:
            self._mood = "neutral"
        
        # Update last feed time
        self._last_feed_time = time

    
    def decrease_hunger(self) -> None:
        # Decrease the hunger
        if self._hunger_value - HUNGER_DECREASE_RATE <= 0:
            self._hunger_value = 0
        else:
            self._hunger_value -= HUNGER_DECREASE_RATE

        # Update the mood if necessary
        if self._hunger_value == 0 and self._mood == "neutral":
            self._mood = "dead"
    

    def increase_entertainment(self, time) -> None:
        # Increase the entertainment
        if self._entertainment_value > MAX - ENTERTAINMENT_INCREASE_RATE:
            self._entertainment_value = MAX
        else:
            self._entertainment_value += ENTERTAINMENT_INCREASE_RATE
        
        # Update the mood if necessary
        if self._mood != "neutral":
            if self._hunger_value == 0:
                self._mood = "dead"
            elif self._clean_value == 0:
                self._mood = "stinky"
        else:
            self._mood = "neutral"
        
        # Update last entertainment time
        self._last_entertainment_time = time
    

    def decrease_entertainment(self) -> None:
        # Decrease the entertainment
        if self._entertainment_value - ENTERTAINMENT_DECREASE_RATE <= 0:
            self._entertainment_value = 0
        else:
            self._entertainment_value -= ENTERTAINMENT_DECREASE_RATE
        
        # Update the mood if necessary
        if self._entertainment_value == 0 and self._mood == "neutral":
            self._mood = "sad"
    

    def increase_cleanliness(self, time) -> None:
        # Increase the cleanliness
        if self._clean_value > MAX - CLEANLINESS_INCREASE_RATE:
            self._clean_value = MAX
        else:
            self._clean_value += CLEANLINESS_INCREASE_RATE
        
        # Update the mood if necessary
        if self._mood != "neutral":
            if self._hunger_value == 0:
                self._mood = "dead"
            elif self._entertainment_value == 0:
                self._mood = "sad"
        else:
            self._mood = "neutral"
        
        # Update last clean time
        self._last_clean_time = time

    
    def decrease_cleanliness(self) -> None:
        # Decrease the cleanliness
        if self._clean_value - CLEANLINESS_DECREASE_RATE <= 0:
            self._clean_value = 0
        else:
            self._clean_value -= CLEANLINESS_DECREASE_RATE
        
        # Update the mood if necessary
        if self._clean_value == 0 and self._mood == "neutral":
            self._mood = "stinky"
