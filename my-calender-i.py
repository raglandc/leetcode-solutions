'''
url: https://leetcode.com/problems/my-calendar-i/description/

You are implementing a program to use as your calendar.

We can add a new event if adding the event will not cause a double booking.

A double booking happens when two events have some non-empty intersection
(i.e., some moment is common to both events.).

The event can be represented as a pair of integers start and end that represents
a booking on the half-open interval [start, end), the range of real numbers
x such that start <= x < end.

Implement the MyCalendar class:

MyCalendar() Initializes the calendar object.

boolean book(int start, int end) Returns true if the event can be added to the
calendar successfully without causing a double booking.

Otherwise, return false and do not add the event to the calendar.

'''

class MyCalendar:
    def __init__(self):
        self.calendar = []
        self.n = 0
    
    def book(self, start: int, end: int) -> bool:
        index = self.binary_search(start, end)
        if (index > 0 and self.calendar[index][1] > start
            or index < self.n and self.calendar[index][0] < end):
            return False
        self.calendar.insert(index + 1, (start, end))
        self.n += 1
        return True

    def binary_search(self, start: int, end: int) -> int:
        left, right = 0, self.n - 1
        mid = left + ((right - left) // 2)
        while left <= right:
            mid = left + ((right - left) // 2)
            (_, e) = self.calendar[mid]
            if start == e: return mid
            if start > e: left += 1
            else: right -= 1
        return left


if __name__ == '__main__':
    myCalendar = MyCalendar()
    print(myCalendar.book(10, 20))
    print(myCalendar.book(15, 25))
    print(myCalendar.book(20, 30))