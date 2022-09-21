# https://leetcode.com/problems/design-parking-system/
class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.cars = [0, big, medium, small]

    def addCar(self, carType: int) -> bool:
        if not self.cars[carType]:
            return False
        
        self.cars[carType] -= 1
        return True


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
