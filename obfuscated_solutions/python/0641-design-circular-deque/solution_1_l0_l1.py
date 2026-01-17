class Node:
    def __init__(self, v1_754, next=None, v2_214=None):
        self.v1_754 = v1_754
        self.next = next
        self.v2_214 = v2_214
class MyCircularDeque:
    def __init__(self, v3_125: int):
        self.v4_859 = 0
        self.v5_381 = v3_125
        self.v6_350 = None
        self.v7_328 = None
    def v8_242(self, v9_854: int) -> bool:
        if self.v10_204():
            return False
        if self.v6_350 is None:
            self.v6_350 = v11_792(v9_854, None, None)
            self.v7_328 = self.v6_350
        else:
            v12_858 = v11_792(v9_854, self.v6_350, None)
            self.v6_350.v2_214 = v12_858
            self.v6_350 = v12_858
        self.v4_859 += 1
        return True
    def v13_658(self, v9_854: int)  ->  bool:
        if self.v10_204():
            return False
        if self.v6_350 is None:
            self.v6_350 = v11_792(v9_854, None, None)
            self.v7_328 = self.v6_350
        else:
            self.v7_328.next = v11_792(v9_854, None, self.v7_328)
            self.v7_328 = self.v7_328.next
        self.v4_859  +=  1
        return True
    def v14_189(self)  ->  bool:
        if self.v15_704():
            return False
        if self.v4_859  ==  1:
            self.v6_350 = None
            self.v7_328 = None
        else:
            self.v6_350 = self.v6_350.next
        self.v4_859 -= 1
        return True
    def v16_532(self) -> bool:
        if self.v15_704():
            return False
        if self.v4_859 == 1:
            self.v6_350 = None
            self.v7_328 = None
        else:
            self.v7_328 = self.v7_328.v2_214
        self.v4_859  -=  1
        return True
    def v17_132(self)  ->  int:
        return -1 if self.v15_704() else self.v6_350.v1_754
    def v18_130(self) -> int:
        return -1 if self.v15_704() else self.v7_328.v1_754
    def v15_704(self) -> bool:
        return self.v4_859 == 0
    def v10_204(self) -> bool:
        return self.v4_859  ==  self.v5_381
