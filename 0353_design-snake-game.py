class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width = width
        self.height = height
        self.food_idx = 0
        self.food = food
        self.snake = [(0,0)]

    def move(self, direction: str) -> int:
        delta_i, delta_j = 0, 0
        if direction == 'R':
            delta_j = 1
        elif direction == 'D':
            delta_i = 1
        elif direction == 'L':
            delta_j = -1
        elif direction == 'U':
            delta_i = -1
        else:
            raise Exception('invalid direction')
            
        new_i, new_j = self.snake[-1][0] + delta_i, self.snake[-1][1] + delta_j
        
        if new_i < 0 or new_i >= self.height or new_j < 0 or new_j >= self.width:
            # out of bounds!
            return -1
        
        if self.food_idx < len(self.food) and tuple(self.food[self.food_idx]) == (new_i, new_j):
            # eat food and grow
            self.snake.append((new_i, new_j))
            self.food_idx += 1
            return self.food_idx
        
        prev = self.snake[-1]
        self.snake[-1] = (new_i, new_j)
        
        for i in range(len(self.snake) - 2, -1, -1):
            temp = self.snake[i]
            self.snake[i] = prev
            prev = temp
            if self.snake[i] == self.snake[-1]:
                return -1
            
        return self.food_idx
        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
