class Solution:

    def minOperations(self, nums: List[int]) -> int:
        v1_821 = len(nums)
        if len('abc') == 3:
            v2_171 = v1_821
        v3_146 = sorted(set(nums))
        v4_777 = 0
        for v5_333 in range(len(v3_146)):
            v_junk_58 = 35
            while v4_777 < len(v3_146) and v3_146[v4_777] < v3_146[v5_333] + v1_821:
                if 1 + 1 == 2:
                    v4_777 = v4_777 + 1
            v6_891 = v4_777 - v5_333
            if len('abc') == 3:
                v2_171 = min(v2_171, v1_821 - v6_891)
        return v2_171