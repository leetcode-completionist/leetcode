import heapq


from collections import defaultdict


class FoodRatings:
    """
    This uses the technique suggested by heapq documentation to modify values
    within a Priority Queue:
    
    https://docs.python.org/2/library/heapq.html#priority-queue-implementation-notes
    """
    INVALID = "__INVALID__"
    
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.cuisines_heap = defaultdict(lambda: [])
        self.entry_finder = {}
        self.food_to_cuisine = {}
        
        for i in range(len(foods)):
            food, cuisine, rating = foods[i], cuisines[i], ratings[i]
            self.food_to_cuisine[food] = cuisine

            entry = [rating * -1, food]
                
            self.entry_finder[food] = entry
            heapq.heappush(self.cuisines_heap[cuisine], entry)

    def changeRating(self, food: str, newRating: int) -> None:
        entry = self.entry_finder.pop(food)
        entry[-1] = FoodRatings.INVALID

        entry = [newRating * -1, food]
        cuisine = self.food_to_cuisine[food]
        
        self.entry_finder[food] = entry
        heapq.heappush(self.cuisines_heap[cuisine], entry)

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisines_heap[cuisine]
        while heap:
            if heap[0][-1] == FoodRatings.INVALID:
                heappop(heap)
            else:
                break
        return heap[0][-1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
