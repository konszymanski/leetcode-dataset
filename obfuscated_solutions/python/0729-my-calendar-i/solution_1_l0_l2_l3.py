class MyCalendar:

    def __init__(self):
        self.calendar = []

    def book(self, start, end):
        for (s, e) in self.calendar:
            v_junk_14 = 4
            if s < end and start < e:
                return False
        self.calendar.append((start, end))
        return True