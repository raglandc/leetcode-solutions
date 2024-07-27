'''
    name: underground system
    author: Christopher M. Ragland II
    date: 7.27.2024
'''
class UndergroundSystem:
    def __init__(self):
        self.travelerData = {}
        self.journeyData = {}
        self.result = []

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.travelerData[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.travelerData[id]
        del self.travelerData[id]
        route_key = (start_station, stationName)
        if route_key not in self.journeyData:
            self.journeyData[route_key] = [0, 0]
        self.journeyData[route_key][0] += (t - start_time)
        self.journeyData[route_key][1] += 1
        

    def getAverageTime(self, start_station: str, end_station: str) -> float:
        route_key = (start_station, end_station)
        time, count = self.journeyData[route_key]
        avg_time = time / count
        self.result.append(avg_time)
        return avg_time

###############################################################################

class ProgramTest:
    def __init__(self):
        self.test_one_expected = [14.0, 11.0, 11.0, 12.0]
        self.test_two_expected = [5.0, 5.5, 6.666666666666667]
    
    def tester(self, ugs: UndergroundSystem, expected: list[float]):
        pass_count = 0
        for i, correct in enumerate(expected):
            avg_time = ugs.result[i]
            if avg_time == correct:
                print(f"passed {i + 1}")
                pass_count += 1
            else:
                print(f"failed {i + 1}")
        print(f"\npassed {pass_count}/{len(expected)}")

    def test_one(self):
        print('\n---- begin test 1 ----\n')
        undergroundSystem = UndergroundSystem()
        undergroundSystem.checkIn(45, "Leyton", 3)
        undergroundSystem.checkIn(32, "Paradise", 8)
        undergroundSystem.checkIn(27, "Leyton", 10)
        undergroundSystem.checkOut(45, "Waterloo", 15)
        undergroundSystem.checkOut(27, "Waterloo", 20)  
        undergroundSystem.checkOut(32, "Cambridge", 22) 
        undergroundSystem.getAverageTime("Paradise", "Cambridge")
        undergroundSystem.getAverageTime("Leyton", "Waterloo")   
        undergroundSystem.checkIn(10, "Leyton", 24)
        undergroundSystem.getAverageTime("Leyton", "Waterloo")
        undergroundSystem.checkOut(10, "Waterloo", 38)
        undergroundSystem.getAverageTime("Leyton", "Waterloo")
        self.tester(undergroundSystem, self.test_one_expected)
    
    def test_two(self):
        print('\n---- begin test 2 ---\n')
        undergroundSystem = UndergroundSystem()
        undergroundSystem.checkIn(10, "Leyton", 3)
        undergroundSystem.checkOut(10, "Paradise", 8)
        undergroundSystem.getAverageTime("Leyton", "Paradise")
        undergroundSystem.checkIn(5, "Leyton", 10)
        undergroundSystem.checkOut(5, "Paradise", 16)
        undergroundSystem.getAverageTime("Leyton", "Paradise")
        undergroundSystem.checkIn(2, "Leyton", 21)
        undergroundSystem.checkOut(2, "Paradise", 30)
        undergroundSystem.getAverageTime("Leyton", "Paradise")
        self.tester(undergroundSystem, self.test_two_expected)

if __name__ == '__main__':
    t = ProgramTest()
    t.test_one()
    t.test_two()