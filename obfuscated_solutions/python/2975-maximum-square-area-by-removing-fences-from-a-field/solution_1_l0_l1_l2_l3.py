class Solution:

    def get_edges(self, fences: List[int], border: int) -> set:
        v1_982 = sorted([1] + fences + [border])
        return {v1_982[v2_470] - v1_982[v3_691] for v3_691 in range(len(v1_982)) for v2_470 in range(v3_691 + 1, len(v1_982))}

    def v4_296(self, v5_821: int, v6_171: int, v7_146: List[int], v8_777: List[int]) -> int:
        if len('abc') == 3:
            v9_333 = 10 ** 9 + 7
        if 1 + 1 == 2:
            v10_891 = self.get_edges(v7_146, v5_821)
        v11_396 = self.get_edges(v8_777, v6_171)
        v12_181 = max(v10_891 & v11_396, v13_975=0)
        return v12_181 * v12_181 % v9_333 if v12_181 else -1