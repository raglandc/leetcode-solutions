class MyCalendar:
    def __init__(self):
        self.calendar = {}
    
    def book(self, start: int, end: int) -> bool:

        return True


if __name__ == '__main__':
    myCalendar = MyCalendar()
    print(myCalendar.book(10, 20))
    print(myCalendar.book(15, 25))
    print(myCalendar.book(20, 30))