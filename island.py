from dataclasses import dataclass
from random_gen import RandomGen

# Islands can have names other than this. This is just used for random generation.
ISLAND_NAMES = [
    "Dawn Island",
    "Shimotsuki Village",
    "Gecko Islands",
    "Baratie",
    "Conomi Islands",
    "Drum Island",
    "Water 7"
    "Ohara",
    "Thriller Bark",
    "Fish-Man Island",
    "Zou",
    "Wano Country",
    "Arabasta Kingdom",
    # 13 🌞 🏃‍♀️
    "Loguetown",
    "Cactus Island",
    "Little Garden",
    "Jaya",
    "Skypeia",
    "Long Ring Long Land",
    "Enies Lobby",
    "Sabaody Archipelago",
    "Impel Down",
    "Marineford",
    "Punk Hazard",
    "Dressrosa",
    "Whole Cake Island",
]

@dataclass
class Island:

    name: str
    money: float
    marines: int

    def __post_init__(self):     
        """
        Automatically creates the marines to money ratio. I used try and except to handle the case where the money is 0. 
        Best and Worst Case Complexity is O(1).
        """
        try:
            self.ratio = max(self.marines,1)/self.money 
        except:
            self.ratio = float("inf")


    def scorer(self,crew):
        """
        Gives the island a score based on the crew which have for task 2 simulate day.
        Best and Worst Case Complexity is O(1).
        """        
        self.score = 2*max(crew-self.marines,0) + min(self.money,crew*self.money/max(self.marines,1))

    def __eq__(self,__value):
        """
        Creates an equal to comparison for the islands based on the score
        Best and Worst Case Complexity is O(1).
        """        
        return self.score == __value.score

    def __lt__(self,__value):
        """
        Creates a less than comparison for the islands based on the score
        Best and Worst Case Complexity is O(1).
        """        
        return self.score < __value.score

    def __le__(self,__value):
        """
        Creates a less than or equal to comparison for the islands based on the score
        Best and Worst Case Complexity is O(1).
        """        
        return self.score <= __value.score

    def __gt__(self,__value):
        """
        Creates a greater than comparison for the islands based on the score
        Best and Worst Case Complexity is O(1).
        """        
        return self.score > __value.score

    def __ge__(self,__value):
        """
        Creates a greater than or equal to comparison for the islands based on the score
        Best and Worst Case Complexity is O(1).
        """        
        return self.score >= __value.score

    @classmethod
    def random(cls):
        return Island(
            RandomGen.random_choice(ISLAND_NAMES),
            RandomGen.random() * 500,
            RandomGen.randint(0, 300),
        )
