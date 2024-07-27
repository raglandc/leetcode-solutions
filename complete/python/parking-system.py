class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.parking_spots = {}
        self.parking_spots[1] = big
        self.parking_spots[2] = medium
        self.parking_spots[3] = small

    
    def add_car(self, car_type: int) -> bool:
        if self.parking_spots[car_type] > 0:
            self.parking_spots[car_type] -= 1
            return True
        return False


if __name__ == "__main__":
    print("Welcome to my parking garage")
    parking_system = ParkingSystem(1, 1, 0)

    cars = [1, 2, 3, 1]
    result = []
    for car_size in cars:
        parking_status = parking_system.add_car(car_size)
        result.append(parking_status)
    print(result)
