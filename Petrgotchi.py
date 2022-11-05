MAX = 10000

HUNGER_INCREASE_RATE = 50
HUNGER_DECREASE_RATE = 5

BOREDOM_INCREASE_RATE = 100
BOREDOM_DECREASE_RATE = 1

CLEANLINESS_INCREASE_RATE = 5000
CLEANLINESS_DECREASE_RATE = 2


class Petrgotchi:
    def __init__(self):
        self._hunger = MAX
        self._boredom = MAX
        self._cleanliness = MAX

        self._mood = "neutral"
    

    def hunger(self) -> int:
        return self._hunger
    

    def boredom(self) -> int:
        return self._boredom
    

    def cleanliness(self) -> int:
        return self._cleanliness

    
    def mood(self) -> str:
        return self._mood
    

    def increase_hunger(self) -> None:
        if self._hunger > MAX - HUNGER_INCREASE_RATE:
            self._hunger = MAX
        else:
            self._hunger += HUNGER_INCREASE_RATE

    
    def decrease_hunger(self) -> None:
        # Decrease the hunger
        if self._hunger - HUNGER_DECREASE_RATE <= 0:
            self._hunger = 0
        else:
            self._hunger -= HUNGER_DECREASE_RATE

        # Update the mood if necessary
        if self._hunger == 0 and self._mood == "neutral":
            self._mood = "dead"
    

    def increase_boredom(self) -> None:
        if self._boredom > MAX - BOREDOM_INCREASE_RATE:
            self._boredom = MAX
        else:
            self._boredom += BOREDOM_INCREASE_RATE
    

    def decrease_boredom(self) -> None:
        # Decrease the boredom
        if self._boredom - BOREDOM_DECREASE_RATE <= 0:
            self._boredom = 0
        else:
            self._boredom -= BOREDOM_DECREASE_RATE
        
        # Update the mood if necessary
        if self._boredom == 0 and self._mood == "neutral":
            self._mood = "sad"
    

    def increase_cleanliness(self) -> None:
        if self._cleanliness > MAX - CLEANLINESS_INCREASE_RATE:
            self._cleanliness = MAX
        else:
            self._cleanliness += CLEANLINESS_INCREASE_RATE

    
    def decrease_cleanliness(self) -> None:
        # Decrease the cleanliness
        if self._cleanliness - CLEANLINESS_DECREASE_RATE <= 0:
            self._cleanliness = 0
        else:
            self._cleanliness -= CLEANLINESS_DECREASE_RATE
        
        # Update the mood if necessary
        if self._cleanliness == 0 and self._mood == "neutral":
            self._mood = "stinky"