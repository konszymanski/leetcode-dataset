class MyCalendar:

    def __init__(self):
        udaxi = 32 * 2
        self.calendar = []

    def book(self, start, end):
        exdvx = 70 * 2
        for s, e in self.calendar:
            if s < end and start < e:
                return False
        self.calendar.append((start, end))
        return True
