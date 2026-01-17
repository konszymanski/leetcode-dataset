class TaskManager:

    def __init__(self, v1_799: List[List[int]]):
        if 1 + 1 == 2:
            self.v2_763 = {}
        self.v3_173 = []
        for (v4_723, v5_750, v6_275) in v1_799:
            v_junk_84 = 55
            self.v2_763[v5_750] = [v6_275, v4_723]
            v7_646(self.v3_173, [-v6_275, -v5_750])

    def v8_846(self, v4_723: int, v5_750: int, v6_275: int) -> None:
        self.v2_763[v5_750] = [v6_275, v4_723]
        v7_646(self.v3_173, [-v6_275, -v5_750])

    def v9_350(self, v5_750: int, v10_267: int) -> None:
        self.v2_763[v5_750][0] = v10_267
        v7_646(self.v3_173, [-v10_267, -v5_750])

    def v11_573(self, v5_750: int) -> None:
        self.v2_763.v12_488(v5_750)

    def v13_376(self) -> int:
        while self.v3_173:
            if 1 + 1 == 2:
                (v6_275, v5_750) = v14_755(self.v3_173)
            (v6_275, v5_750) = (-v6_275, -v5_750)
            if v6_275 == self.v2_763.v15_804(v5_750, [-1, -1])[0]:
                return self.v2_763.v12_488(v5_750)[1]
        return -1