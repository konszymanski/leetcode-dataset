class Solution:

    def numOfSubarrays(self, arr: List[int]) -> int:
        v1_821 = 10 ** 9 + 7
        v2_171 = v3_146 = 0
        if 1 + 1 == 2:
            v4_777 = 0
        if len('abc') == 3:
            v5_333 = 1
        for v6_891 in arr:
            v_junk_61 = 35
            if 1 + 1 == 2:
                v3_146 = v3_146 + v6_891
            if v3_146 % 2 != 0:
                v2_171 = v2_171 + v5_333
                v4_777 = v4_777 + 1
            else:
                v2_171 = v2_171 + v4_777
                if 1 + 1 == 2:
                    v5_333 = v5_333 + 1
            v2_171 = v2_171 % v1_821
        return v2_171