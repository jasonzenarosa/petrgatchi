import json


MAX = 10000

HUNGER_INCREASE_RATE = 500
HUNGER_DECREASE_RATE = 100 # 5

ENTERTAINMENT_INCREASE_RATE = 100
ENTERTAINMENT_DECREASE_RATE = 10

CLEANLINESS_INCREASE_RATE = 5000
CLEANLINESS_DECREASE_RATE = 2


class Petrgotchi:
    def __init__(self):
        self._mood = "neutral"
        self._hunger_value = MAX
        self._clean_value = MAX
        self._entertainment_value = MAX


    def hunger(self) -> float:
        return 1 - self._hunger_value / MAX
    

    def entertainment(self) -> float:
        return 1 - self._entertainment_value / MAX
    

    def cleanliness(self) -> float:
        return 1 - self._clean_value / MAX
    

    def mood(self) -> str:
        return self._mood


    def increase_hunger(self) -> None:
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

    
    def decrease_hunger(self) -> None:
        # Decrease the hunger
        if self._hunger_value - HUNGER_DECREASE_RATE <= 0:
            self._hunger_value = 0
        else:
            self._hunger_value -= HUNGER_DECREASE_RATE

        # Update the mood if necessary
        if self._hunger_value == 0 and self._mood == "neutral":
            self._mood = "dead"
    

    def increase_entertainment(self) -> None:
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
    

    def decrease_entertainment(self) -> None:
        # Decrease the entertainment
        if self._entertainment_value - ENTERTAINMENT_DECREASE_RATE <= 0:
            self._entertainment_value = 0
        else:
            self._entertainment_value -= ENTERTAINMENT_DECREASE_RATE
        
        # Update the mood if necessary
        if self._entertainment_value == 0 and self._mood == "neutral":
            self._mood = "sad"
    

    def increase_cleanliness(self) -> None:
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

    
    def decrease_cleanliness(self) -> None:
        # Decrease the cleanliness
        if self._clean_value - CLEANLINESS_DECREASE_RATE <= 0:
            self._clean_value = 0
        else:
            self._clean_value -= CLEANLINESS_DECREASE_RATE
        
        # Update the mood if necessary
        if self._clean_value == 0 and self._mood == "neutral":
            self._mood = "stinky"
