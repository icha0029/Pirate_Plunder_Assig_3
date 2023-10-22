from island import Island
from data_structures.bst import BinarySearchTree

class Mode1Navigator:
    """
    ADTs: We used a BST as they are superior for searching, inserting & deleting
    - The search is always binary (Complexity varies depending on depth but max depth is log(n), according to assumption)
    - Modifying the links is constant (Once you find the element)
    Student-TODO: for examples and complexities refer to individual functions. Complexity variables: n refers to number of islands
    """

    def __init__(self, islands: list[Island], crew: int) -> None:
        """
        Example: Mode1Navigator(islands = [Island("Skypiea", 16, 8 ), Island("Land_Of_Wano", 20, 15 )], crew = 15)
        Result: The crew value of 15 is assigned to self.crew. 
        Then each island in the input island is added to the BST with their unique ratios. 
        With the key as their ratio and the item as the island itself. 
        Best/Worst Case: n(log(n)). This is because the for loop to add the islands to the BST runs n times 
        and each inserting into the BST ranges from O(1) to O(log(n)). 
        On average its O(log(n)), so its best and worst case is O(n(log(n)))
        """
        self.crew = crew
        self.island_bst = BinarySearchTree()
        for island in islands: 
            self.island_bst[island.ratio]=island

    def select_islands(self) -> list[tuple[Island, int]]:
        """
        Explanation: We create a copy of crew by assigning it to a new variable. 
        So we can use it again for later calls. 
        Then we use the BST inorder iterator to go through the islands in such a way that we attack the most optimal island first.
        Then for each island we attack we add the island + the number of crew we sent to the island and add as a tuple to the list.
        Then we keep going till we run out of crew or run out of islands to attack. 
        Best/Worst Case: Best case O(1): This occurs when the first island we attack has more marines than the crew 
        and when the BST has no islands to the left of the root node. 
        Worst Case O(n): This when we have enough crew to attack all the islands and since we go through all the islands once its O(n)
        """
        pirate_crew = self.crew
        island_to_attack = []
        for island in self.island_bst:
            if pirate_crew<=0:
                break
            pirates_to_attack = min(pirate_crew,island.item.marines)
            island_to_attack.append((island.item,pirates_to_attack))
            pirate_crew -= pirates_to_attack
        return island_to_attack

    def select_islands_from_crew_numbers(self, crew_numbers: list[int]) -> list[float]:
        """
        Example: select_islands_from_crew_numbers([12,10,6])
        Explanation: For each crew value configuration in crew number input list we go through each island using the BST inorder iterator. 
        Since the iterator return the most optimal island to attack first, 
        we keep attacking the islands until the crew all dies or we run out of islands. 
        As we go through each island we amount the loot the crew would collect and we add it to the list once the crew dies or we run out of islands.
        We repeat this process for all crews in the input list.
        Complexity Variable: C refers to number of crew configs in crew numbers list,
        Best/Worst Case: Best case = O(C): Happens when the number of marines in the first island are larger than or equal highest/max crew config in input list.
        and occurs when BST doesn't have islands to the left of the root node.
        Worst Case: O(CxN): Happens when all the crew configs in the input list are greater than or equal to the marines of all the islands combined. 
        """
        optimal_island_to_attack = []
        for pirate_crew in crew_numbers:
            money_to_loot = 0 
            for island in self.island_bst:
                if pirate_crew<=0:
                    break
                money_to_loot +=min(island.item.money,pirate_crew*island.item.money/island.item.marines)
                pirates_to_attack = min(pirate_crew,island.item.marines)
                pirate_crew -= pirates_to_attack
            optimal_island_to_attack.append(money_to_loot)
        return optimal_island_to_attack


    def update_island(self, island: Island, new_money: float, new_marines: int) -> None:
        """
        Example: update_islandIsland("Skypiea", 16, 8 ), 12, 30)
        Explanation: First we delete the island as theres a high chance that the new island marine to money ratio is different to the past ratio. 
        Which will most likely change the islands position in the BST. 
        Now we update the money, marines and ratio properties of the island. Then we add the island back into the BST into its new position
        Best/Worst Case: Worst case log(n), n is the number of islands. 
        Worst case occurs when we delete islands causing an unbalanced BST, so when we re insert it uses O(log(n))
        Best Case: O(1), occurs when we delete a parent node within the first log(n) nodes and it has either 0 or 1 child nodes
        and when make this island the child of a parent node within the first log(n) nodes.
        """

        del self.island_bst[island.ratio]
        island.money = new_money
        island.marines = new_marines
        try:
            island.ratio = max(island.marines,1)/island.money 
        except:
            island.ratio = float("inf")    
        self.island_bst[island.ratio] = island  