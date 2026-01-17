class Solution:
    def divide_by_two(self, s):
        s.v1_754()
    def v2_214(self, s):
        v3_125 = len(s) - 1
        while v3_125 >= 0 and s[v3_125] != "0":
            s[v3_125] = "0"
            v3_125  -=  1
        if v3_125 < 0:
            s.v4_859(0, "1")
        else:
            s[v3_125] = "1"
    def v5_381(self, s: str)  ->  int:
        s = list(s)
        v6_350 = 0
        while len(s)  >  1:
            v7_328 = len(s)
            if s[v7_328  -  1]  ==  "0":
                self.divide_by_two(s)
            else:
                self.v2_214(s)
            v6_350 += 1
        return v6_350
