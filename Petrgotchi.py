MAX = 10000

HUNGER_INCREASE_RATE = 50
HUNGER_DECREASE_RATE = 5

ENTERTAINMENT_INCREASE_RATE = 100
ENTERTAINMENT_DECREASE_RATE = 1

CLEANLINESS_INCREASE_RATE = 5000
CLEANLINESS_DECREASE_RATE = 2


class Petrgotchi:
    def __init__(self, **kargs):
        self._hunger = MAX
        self._entertainment = MAX
        self._cleanliness = MAX

        self._mood = "neutral"

        self._sprite = kargs["sprite"]
    

    def hunger(self) -> int:
        return self._hunger
    

    def entertainment(self) -> int:
        return self._entertainment
    

    def cleanliness(self) -> int:
        return self._cleanliness

    
    def mood(self) -> str:
        return self._mood
    

    def increase_hunger(self) -> None:
        # Increase the hunger
        if self._hunger > MAX - HUNGER_INCREASE_RATE:
            self._hunger = MAX
        else:
            self._hunger += HUNGER_INCREASE_RATE
        
        # Update the mood if necessary
        if self._mood != "neutral":
            if self._entertainment == 0:
                self._mood = "sad"
            elif self._cleanliness == 0:
                self._mood = "stinky"
        else:
            self._mood = "neutral"

    
    def decrease_hunger(self) -> None:
        # Decrease the hunger
        if self._hunger - HUNGER_DECREASE_RATE <= 0:
            self._hunger = 0
        else:
            self._hunger -= HUNGER_DECREASE_RATE

        # Update the mood if necessary
        if self._hunger == 0 and self._mood == "neutral":
            self._mood = "dead"
    

    def increase_entertainment(self) -> None:
        # Increase the entertainment
        if self._entertainment > MAX - ENTERTAINMENT_INCREASE_RATE:
            self._entertainment = MAX
        else:
            self._entertainment += ENTERTAINMENT_INCREASE_RATE
        
        # Update the mood if necessary
        if self._mood != "neutral":
            if self._hunger == 0:
                self._mood = "dead"
            elif self._cleanliness == 0:
                self._mood = "stinky"
        else:
            self._mood = "neutral"
    

    def decrease_entertainment(self) -> None:
        # Decrease the entertainment
        if self._entertainment - ENTERTAINMENT_DECREASE_RATE <= 0:
            self._entertainment = 0
        else:
            self._entertainment -= ENTERTAINMENT_DECREASE_RATE
        
        # Update the mood if necessary
        if self._entertainment == 0 and self._mood == "neutral":
            self._mood = "sad"
    

    def increase_cleanliness(self) -> None:
        # Increase the cleanliness
        if self._cleanliness > MAX - CLEANLINESS_INCREASE_RATE:
            self._cleanliness = MAX
        else:
            self._cleanliness += CLEANLINESS_INCREASE_RATE
        
        # Update the mood if necessary
        if self._mood != "neutral":
            if self._hunger == 0:
                self._mood = "dead"
            elif self._entertainment == 0:
                self._mood = "sad"
        else:
            self._mood = "neutral"

    
    def decrease_cleanliness(self) -> None:
        # Decrease the cleanliness
        if self._cleanliness - CLEANLINESS_DECREASE_RATE <= 0:
            self._cleanliness = 0
        else:
            self._cleanliness -= CLEANLINESS_DECREASE_RATE
        
        # Update the mood if necessary
        if self._cleanliness == 0 and self._mood == "neutral":
            self._mood = "stinky"