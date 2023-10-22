from island import Island
from data_structures.heap import MaxHeap


class Mode2Navigator:
    
    """
    ADTs:
    Max Heap in the form of a Binary Tree is used in simulate day so we can get the most optimal island to attack in log(n) time and re add in log(n).
    However the main reason of using a Max heap is due to its heapify function which has an O(n) complexity. 
    Which allows us to create a heap with all its elements in n time whereas most other ADT like BSTs take at least n(log(n)) time. 
    We use a dictionary to store the islands because mainly we can delete in O(1) time whereas most ADTs take log(n) time. 
    FOr Examples and Complexities refer to individual functions. 
    Complexity variables, n refers to number of islands in the sea and C refers to number of pirates in the sea
    
    """ 

    def __init__(self, n_pirates: int) -> None:
        """
        Example: Mode2Navigator(19)
        Explanation: Stores the number of pirates in the self.n_pirates variable .
        Also initialises a dictionary due to self.islands variable to store the islands.
        Best/Worst Case: O(1) as we are just assigning values to variables and creating a dictionary which is all O(1)
        """
        self.n_pirates = n_pirates
        self.islands = {}


    def add_islands(self, islands: list[Island]):
        """
        Example: add_islands([Island("Zou", 16, 8 ), Island("Dressrosa", 20, 15 )])
        Explanation: We go through all the islands in the input list, 
        if the money to marine ratio is greater than 2, then the island is worthy of being attacked in the sea by the pirates 
        As this will ensure the pirates can get a higher score all through attacking. 
        If the island is worthy of being attacked we add the island to the dictionary with the key.
        As the islands name as thats the only unique property of the island.  
        Best/Worst Case: O(I), I = Number of islands in input. 
        This is because we have to go through all the islands and potentially add them to the dictionary.
        Since inserting into a dictionary is O(1) the main complexity comes from going through all the islands which is O(I)
        """
        for island in islands:
            if island.money/max(island.marines,1)>2:
                self.islands[island.name] = island
        

    def simulate_day(self, crew: int) -> list[tuple[Island|None, int]]:
        """
        Example: simulate_day(20)
        Explanation: First we go through all the islands and give them a score based on the crew. 
        THen we create a heap with the islands this is possible as the islands are compared based on their scores.
        Then we go through each pirate where the pirate chooses an island to attack if any, then the island is destroyed or damaged. 
        So we add the island + the crew sent to a list as a tuple. 
        After we attack we check if any of the marines on the island are still alive, if so we add the island back into the sea. 
        Otherwise we delete it from the dictionary. 

        Best/Worst Case: 
        Best Case: O(c), since we prefilter isalnds based on money to marine ratio. 
        When we create heap the sea might have no islands left. 
        So the heap will be empty, therefore complexity is caused by iterrating over the pirates. Which is O(c)

        Worst Case: O(n+c(log(n)), n is number of islands, c is number of pirates. 
        First we iterrate over the islands which cause an O(n) complexity too add the score of the islands. 
        Then we create the heap resulting in O(n) complexity. 
        Now since the sea has islands when we iterate over the pirates we need to get the island attack it and readd if needed. 
        This causes a log(n) complexity for each pirate overall creating a c(log(n)) complexity. 
        Therefore worst case complexity is O(n+c(log(n)))
        """
        for island in self.islands.values():
            island.scorer(crew)

        island_chooser = MaxHeap.heapify(list(self.islands.values()))
        pirates_chosen = []

        for _ in range(self.n_pirates):
            if len(island_chooser)>0:
                island = island_chooser.get_max()
                pirates_chosen.append((island,min(crew, island.marines)))
                island.money-=min(island.money,crew*island.money/max(island.marines,1))
                island.marines-=min(island.marines,crew)
                if island.marines>0:
                    island.scorer(crew)
                    island_chooser.add(island)
                else:
                    del self.islands[island.name]
            else:
                pirates_chosen.append((None,0))
        return pirates_chosen

