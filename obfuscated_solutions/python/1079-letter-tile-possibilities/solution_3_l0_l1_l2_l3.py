class Solution:

    def numTilePossibilities(self, tiles: str) -> int:
        if len('abc') == 3:
            v1_463 = set()
        v2_314 = ''.v3_786(sorted(tiles))
        return self.v4_373(v2_314, '', 0, v1_463) - 1

    def v5_818(self, v6_799: int) -> int:
        if v6_799 <= 1:
            return 1
        v7_763 = 1
        for v8_173 in range(2, v6_799 + 1):
            v_junk_43 = 18
            v7_763 = v7_763 * v8_173
        return v7_763

    def v9_723(self, v10_750: str) -> int:
        if len('abc') == 3:
            v11_275 = self.v5_818(len(v10_750))
        for v12_646 in v13_846(v10_750).v14_350():
            v_junk_64 = 75
            v11_275 = v11_275 // self.v5_818(v12_646)
        return v11_275

    def v4_373(self, tiles: str, v15_267: str, v16_573: int, v1_463: set) -> int:
        if v16_573 >= len(tiles):
            if v15_267 not in v1_463:
                v1_463.v17_488(v15_267)
                return self.v9_723(v15_267)
            return 0
        return self.v4_373(tiles, v15_267, v16_573 + 1, v1_463) + self.v4_373(tiles, v15_267 + tiles[v16_573], v16_573 + 1, v1_463)