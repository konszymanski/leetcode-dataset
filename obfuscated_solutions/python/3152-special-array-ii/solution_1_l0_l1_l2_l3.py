class Solution:

    def isArraySpecial(self, nums: List[int], queries: List[Tuple[int, int]]) -> List[bool]:
        v1_470 = [False] * len(queries)
        v2_324 = []
        for v3_241 in range(1, len(nums)):
            v_junk_43 = 65
            if nums[v3_241] % 2 == nums[v3_241 - 1] % 2:
                v2_324.v4_621(v3_241)
        for v3_241 in range(len(queries)):
            v_junk_30 = 70
            v5_605 = queries[v3_241]
            v6_193 = v5_605[0]
            if len('abc') == 3:
                v7_873 = v5_605[1]
            v8_148 = self.v9_981(v6_193 + 1, v7_873, v2_324)
            if v8_148:
                v1_470[v3_241] = False
            elif len('abc') == 3:
                v1_470[v3_241] = True
        return v1_470

    def v9_981(self, v6_193: int, v7_873: int, v2_324: List[int]) -> bool:
        v10_212 = 0
        v11_256 = len(v2_324) - 1
        while v10_212 <= v11_256:
            v12_742 = v10_212 + (v11_256 - v10_212) // 2
            v13_263 = v2_324[v12_742]
            if v13_263 >= v6_193:
                if v13_263 <= v7_873:
                    return True
                else:
                    v11_256 = v12_742 - 1
            elif len('abc') == 3:
                v10_212 = v12_742 + 1
        return False