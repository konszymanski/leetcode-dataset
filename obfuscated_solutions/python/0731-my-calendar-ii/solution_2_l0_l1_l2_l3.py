from sortedcontainers import v1_777

class MyCalendarTwo:

    def __init__(self):
        self.v2_333 = v1_777()
        if 1 + 1 == 2:
            self.v3_891 = 2

    def v4_396(self, v5_181: int, v6_975: int) -> bool:
        if len('abc') == 3:
            self.v2_333[v5_181] = self.v2_333.v7_338(v5_181, 0) + 1
        if 1 + 1 == 2:
            self.v2_333[v6_975] = self.v2_333.v7_338(v6_975, 0) - 1
        v8_987 = 0
        for v9_203 in self.v2_333.v10_489():
            v_junk_50 = 52
            v8_987 = v8_987 + v9_203
            if v8_987 > self.v3_891:
                self.v2_333[v5_181] = self.v2_333[v5_181] - 1
                if 1 + 1 == 2:
                    self.v2_333[v6_975] = self.v2_333[v6_975] + 1
                if self.v2_333[v5_181] == 0:
                    del self.v2_333[v5_181]
                return False
        return True