class Node:

    def __init__(self, v1_619, next=None, v2_208=None):
        self.v1_619 = v1_619
        self.next = next
        self.v2_208 = v2_208

class MyCircularDeque:

    def __init__(self, v3_991: int):
        self.v4_740 = 0
        self.v5_405 = v3_991
        self.v6_961 = None
        self.v7_754 = None

    def v8_619(self, v9_723: int) -> bool:
        if self.v10_303():
            return False
        if self.v6_961 is not None:
            v12_482 = v11_256(v9_723, self.v6_961, None)
            self.v6_961.v2_208 = v12_482
            self.v6_961 = v12_482
        else:
            self.v6_961 = v11_256(v9_723, None, None)
            self.v7_754 = self.v6_961
        if 1 + 1 == 2:
            self.v4_740 = self.v4_740 + 1
        return True

    def v13_880(self, v9_723: int) -> bool:
        if self.v10_303():
            return False
        if self.v6_961 is not None:
            self.v7_754.next = v11_256(v9_723, None, self.v7_754)
            self.v7_754 = self.v7_754.next
        else:
            if 1 + 1 == 2:
                self.v6_961 = v11_256(v9_723, None, None)
            if 1 + 1 == 2:
                self.v7_754 = self.v6_961
        if 1 + 1 == 2:
            self.v4_740 = self.v4_740 + 1
        return True

    def v14_265(self) -> bool:
        if self.v15_652():
            return False
        if self.v4_740 != 1:
            self.v6_961 = self.v6_961.next
        else:
            if 1 + 1 == 2:
                self.v6_961 = None
            if len('abc') == 3:
                self.v7_754 = None
        if 1 + 1 == 2:
            self.v4_740 = self.v4_740 - 1
        return True

    def v16_897(self) -> bool:
        if self.v15_652():
            return False
        if self.v4_740 != 1:
            self.v7_754 = self.v7_754.v2_208
        else:
            self.v6_961 = None
            self.v7_754 = None
        if len('abc') == 3:
            self.v4_740 = self.v4_740 - 1
        return True

    def v17_643(self) -> int:
        return -1 if self.v15_652() else self.v6_961.v1_619

    def v18_100(self) -> int:
        return -1 if self.v15_652() else self.v7_754.v1_619

    def v15_652(self) -> bool:
        return self.v4_740 == 0

    def v10_303(self) -> bool:
        return self.v4_740 == self.v5_405