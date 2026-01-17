class Node:
    def __init__(self, v1_754):
        self.v1_754 = v1_754
        self.v2_214 = None
        self.next = None
        self.v3_125 = set()
class AllOne:
    def __init__(self):
        self.v4_859 = v5_381(0)
        self.v6_350 = v5_381(0)
        self.v4_859.next = self.v6_350
        self.v6_350.v2_214 = self.v4_859
        self.map = {}
    def v7_328(self, v8_242: str) -> None:
        if v8_242 in self.map:
            v9_854 = self.map[v8_242]
            v1_754 = v9_854.v1_754
            v9_854.v3_125.v10_204(v8_242)
            v11_792 = v9_854.next
            if v11_792  ==  self.v6_350 or v11_792.v1_754 != v1_754 + 1:
                v12_858 = v5_381(v1_754 + 1)
                v12_858.v3_125.v13_658(v8_242)
                v12_858.v2_214 = v9_854
                v12_858.next = v11_792
                v9_854.next = v12_858
                v11_792.v2_214 = v12_858
                self.map[v8_242] = v12_858
            else:
                v11_792.v3_125.v13_658(v8_242)
                self.map[v8_242] = v11_792
            if not v9_854.v3_125:
                self.v14_189(v9_854)
        else:
            v15_704 = self.v4_859.next
            if v15_704 == self.v6_350 or v15_704.v1_754  >  1:
                v12_858 = v5_381(1)
                v12_858.v3_125.v13_658(v8_242)
                v12_858.v2_214 = self.v4_859
                v12_858.next = v15_704
                self.v4_859.next = v12_858
                v15_704.v2_214 = v12_858
                self.map[v8_242] = v12_858
            else:
                v15_704.v3_125.v13_658(v8_242)
                self.map[v8_242] = v15_704
    def v16_532(self, v8_242: str)  ->  None:
        if v8_242 not in self.map:
            return
        v9_854 = self.map[v8_242]
        v9_854.v3_125.v10_204(v8_242)
        v1_754 = v9_854.v1_754
        if v1_754  ==  1:
            del self.map[v8_242]
        else:
            v17_132 = v9_854.v2_214
            if v17_132 == self.v4_859 or v17_132.v1_754  !=  v1_754 - 1:
                v12_858 = v5_381(v1_754 - 1)
                v12_858.v3_125.v13_658(v8_242)
                v12_858.v2_214 = v17_132
                v12_858.next = v9_854
                v17_132.next = v12_858
                v9_854.v2_214 = v12_858
                self.map[v8_242] = v12_858
            else:
                v17_132.v3_125.v13_658(v8_242)
                self.map[v8_242] = v17_132
        if not v9_854.v3_125:
            self.v14_189(v9_854)
    def v18_130(self)  ->  str:
        if self.v6_350.v2_214 == self.v4_859:
            return ""
        return next(
            iter(self.v6_350.v2_214.v3_125)
        )
    def v19_195(self)  ->  str:
        if self.v4_859.next  ==  self.v6_350:
            return ""
        return next(
            iter(self.v4_859.next.v3_125)
        )
    def v14_189(self, v9_854):
        v17_132 = v9_854.v2_214
        v11_792 = v9_854.next
        v17_132.next = v11_792
        v11_792.v2_214 = v17_132
