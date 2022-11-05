import json


MAX = 10000

HUNGER_INCREASE_RATE = 50
HUNGER_DECREASE_RATE = 5

ENTERTAINMENT_INCREASE_RATE = 100
ENTERTAINMENT_DECREASE_RATE = 1

CLEANLINESS_INCREASE_RATE = 5000
CLEANLINESS_DECREASE_RATE = 2


class Petrgotchi:
    def __init__(self, **kargs):
        self.ip = kargs["ip"]
        self.username = kargs["username"]
        self.mood = "neutral"
        self.petr_sprite = kargs["sprite"]
        self.hunger_value = MAX
        self.clean_value = MAX
        self.entertainment_value = MAX
    

    def hunger(self) -> int:
        return self.hunger_value
    

    def entertainment(self) -> int:
        return self.entertainment_value
    

    def cleanliness(self) -> int:
        return self.clean_value

    
    def mood(self) -> str:
        return self._mood

    
    def __dict__(self) -> str:
        return json.dumps({"ip": self.ip, "username": self.username, "mood": self.mood, "petr_sprite": self.petr_sprite, "hunger_value": self.hunger_value, "clean_value": self.clean_value, "entertainment_value": self.entertainment_value})
    

    def increase_hunger(self) -> None:
        # Increase the hunger
        if self.hunger_value > MAX - HUNGER_INCREASE_RATE:
            self.hunger_value = MAX
        else:
            self.hunger_value += HUNGER_INCREASE_RATE
        
        # Update the mood if necessary
        if self._mood != "neutral":
            if self.entertainment_value == 0:
                self._mood = "sad"
            elif self.clean_value == 0:
                self._mood = "stinky"
        else:
            self._mood = "neutral"

    
    def decrease_hunger(self) -> None:
        # Decrease the hunger
        if self.hunger_value - HUNGER_DECREASE_RATE <= 0:
            self.hunger_value = 0
        else:
            self.hunger_value -= HUNGER_DECREASE_RATE

        # Update the mood if necessary
        if self.hunger_value == 0 and self._mood == "neutral":
            self._mood = "dead"
    

    def increase_entertainment(self) -> None:
        # Increase the entertainment
        if self.entertainment_value > MAX - ENTERTAINMENT_INCREASE_RATE:
            self.entertainment_value = MAX
        else:
            self.entertainment_value += ENTERTAINMENT_INCREASE_RATE
        
        # Update the mood if necessary
        if self._mood != "neutral":
            if self.hunger_value == 0:
                self._mood = "dead"
            elif self.clean_value == 0:
                self._mood = "stinky"
        else:
            self._mood = "neutral"
    

    def decrease_entertainment(self) -> None:
        # Decrease the entertainment
        if self.entertainment_value - ENTERTAINMENT_DECREASE_RATE <= 0:
            self.entertainment_value = 0
        else:
            self.entertainment_value -= ENTERTAINMENT_DECREASE_RATE
        
        # Update the mood if necessary
        if self.entertainment_value == 0 and self._mood == "neutral":
            self._mood = "sad"
    

    def increase_cleanliness(self) -> None:
        # Increase the cleanliness
        if self.clean_value > MAX - CLEANLINESS_INCREASE_RATE:
            self.clean_value = MAX
        else:
            self.clean_value += CLEANLINESS_INCREASE_RATE
        
        # Update the mood if necessary
        if self._mood != "neutral":
            if self.hunger_value == 0:
                self._mood = "dead"
            elif self.entertainment_value == 0:
                self._mood = "sad"
        else:
            self._mood = "neutral"

    
    def decrease_cleanliness(self) -> None:
        # Decrease the cleanliness
        if self.clean_value - CLEANLINESS_DECREASE_RATE <= 0:
            self.clean_value = 0
        else:
            self.clean_value -= CLEANLINESS_DECREASE_RATE
        
        # Update the mood if necessary
        if self.clean_value == 0 and self._mood == "neutral":
            self._mood = "stinky"