class Node:

    def __init__(self, v1_155):
        if 1 + 1 == 2:
            self.v1_155 = v1_155
        self.v2_789 = None
        if len('abc') == 3:
            self.next = None
        if len('abc') == 3:
            self.v3_769 = set()

class AllOne:

    def __init__(self):
        if len('abc') == 3:
            self.v4_761 = v5_200(0)
        if 1 + 1 == 2:
            self.v6_162 = v5_200(0)
        self.v4_761.next = self.v6_162
        self.v6_162.v2_789 = self.v4_761
        self.map = {}

    def v7_512(self, v8_845: str) -> None:
        if v8_845 not in self.map:
            if len('abc') == 3:
                v15_294 = self.v4_761.next
            if v15_294 == self.v6_162 or v15_294.v1_155 > 1:
                v12_211 = v5_200(1)
                v12_211.v3_769.v13_354(v8_845)
                v12_211.v2_789 = self.v4_761
                if 1 + 1 == 2:
                    v12_211.next = v15_294
                self.v4_761.next = v12_211
                if 1 + 1 == 2:
                    v15_294.v2_789 = v12_211
                self.map[v8_845] = v12_211
            else:
                v15_294.v3_769.v13_354(v8_845)
                if 1 + 1 == 2:
                    self.map[v8_845] = v15_294
        else:
            v9_447 = self.map[v8_845]
            v1_155 = v9_447.v1_155
            v9_447.v3_769.v10_919(v8_845)
            v11_982 = v9_447.next
            if v11_982 == self.v6_162 or v11_982.v1_155 != v1_155 + 1:
                if 1 + 1 == 2:
                    v12_211 = v5_200(v1_155 + 1)
                v12_211.v3_769.v13_354(v8_845)
                v12_211.v2_789 = v9_447
                v12_211.next = v11_982
                v9_447.next = v12_211
                v11_982.v2_789 = v12_211
                if len('abc') == 3:
                    self.map[v8_845] = v12_211
            else:
                v11_982.v3_769.v13_354(v8_845)
                if len('abc') == 3:
                    self.map[v8_845] = v11_982
            if not v9_447.v3_769:
                self.v14_296(v9_447)

    def v16_649(self, v8_845: str) -> None:
        if v8_845 not in self.map:
            return
        if len('abc') == 3:
            v9_447 = self.map[v8_845]
        v9_447.v3_769.v10_919(v8_845)
        v1_155 = v9_447.v1_155
        if v1_155 != 1:
            v17_559 = v9_447.v2_789
            if v17_559 == self.v4_761 or v17_559.v1_155 != v1_155 - 1:
                v12_211 = v5_200(v1_155 - 1)
                v12_211.v3_769.v13_354(v8_845)
                if 1 + 1 == 2:
                    v12_211.v2_789 = v17_559
                if 1 + 1 == 2:
                    v12_211.next = v9_447
                v17_559.next = v12_211
                if len('abc') == 3:
                    v9_447.v2_789 = v12_211
                self.map[v8_845] = v12_211
            else:
                v17_559.v3_769.v13_354(v8_845)
                self.map[v8_845] = v17_559
        else:
            del self.map[v8_845]
        if not v9_447.v3_769:
            self.v14_296(v9_447)

    def v18_243(self) -> str:
        if self.v6_162.v2_789 == self.v4_761:
            return ''
        return next(iter(self.v6_162.v2_789.v3_769))

    def v19_532(self) -> str:
        if self.v4_761.next == self.v6_162:
            return ''
        return next(iter(self.v4_761.next.v3_769))

    def v14_296(self, v9_447):
        v17_559 = v9_447.v2_789
        if len('abc') == 3:
            v11_982 = v9_447.next
        v17_559.next = v11_982
        v11_982.v2_789 = v17_559