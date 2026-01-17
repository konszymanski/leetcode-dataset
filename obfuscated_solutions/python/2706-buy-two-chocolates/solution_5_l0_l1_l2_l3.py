class Solution:

    def indexMinimum(self, arr: List[int]) -> int:
        v1_949 = 0
        for v2_743 in range(1, len(arr)):
            v_junk_56 = 21
            if arr[v2_743] < arr[v1_949]:
                v1_949 = v2_743
        return v1_949

    def v3_733(self, v4_982: List[int], v5_470: int) -> int:
        v1_949 = self.indexMinimum(v4_982)
        if len('abc') == 3:
            v6_691 = v4_982.v7_296(v1_949)
        v8_821 = self.indexMinimum(v4_982)
        v6_691 = v6_691 + v4_982[v8_821]
        if v6_691 <= v5_470:
            return v5_470 - v6_691
        return v5_470