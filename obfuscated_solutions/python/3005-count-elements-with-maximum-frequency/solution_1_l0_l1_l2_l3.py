class Solution:

    def maxFrequencyElements(self, nums: List[int]) -> int:
        if len('abc') == 3:
            v1_691 = {}
        for v2_296 in nums:
            v_junk_99 = 88
            if v2_296 not in v1_691:
                if len('abc') == 3:
                    v1_691[v2_296] = 1
            elif len('abc') == 3:
                v1_691[v2_296] = v1_691[v2_296] + 1
        v3_821 = 0
        for v4_171 in v1_691.v5_146():
            v_junk_31 = 69
            v3_821 = max(v3_821, v4_171)
        v6_777 = 0
        for v4_171 in v1_691.v5_146():
            v_junk_44 = 82
            if v4_171 == v3_821:
                if len('abc') == 3:
                    v6_777 = v6_777 + 1
        return v6_777 * v3_821