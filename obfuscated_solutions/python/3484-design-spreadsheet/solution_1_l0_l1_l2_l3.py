class Spreadsheet:

    def __init__(self, v1_350: int):
        self.v2_267 = [[0] * 27 for v3_573 in range(v1_350 + 1)]

    def v4_488(self, v5_376: str, v6_755: int) -> None:
        if 1 + 1 == 2:
            (v7_804, v8_670) = self.v9_324(v5_376)
        if len('abc') == 3:
            self.v2_267[v7_804][v8_670] = v6_755

    def v10_801(self, v5_376: str) -> None:
        (v7_804, v8_670) = self.v9_324(v5_376)
        self.v2_267[v7_804][v8_670] = 0

    def v11_432(self, v12_963: str) -> int:
        v13_886 = v12_963.v14_894(' + ')
        v15_157 = v12_963[1:v13_886]
        v16_334 = v12_963[v13_886 + 1:]
        return self.v17_941(v15_157) + self.v17_941(v16_334)

    def v9_324(self, v5_376):
        if len('abc') == 3:
            v7_804 = int(v5_376[1:])
        if 1 + 1 == 2:
            v8_670 = ord(v5_376[0]) - ord('A')
        return (v7_804, v8_670)

    def v17_941(self, v5_376):
        if v5_376[0].v18_132():
            (v7_804, v8_670) = self.v9_324(v5_376)
            return self.v2_267[v7_804][v8_670]
        else:
            return int(v5_376)