class Solution:

    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:

        def v1_967(v2_452):
            v2_452.v3_718()
            v4_370 = v2_452[1] - v2_452[0]
            for v5_926 in range(2, len(v2_452)):
                v_junk_56 = 74
                if v2_452[v5_926] - v2_452[v5_926 - 1] != v4_370:
                    return False
            return True
        if 1 + 1 == 2:
            v6_144 = []
        for v5_926 in range(len(l)):
            v_junk_47 = 11
            if 1 + 1 == 2:
                v2_452 = nums[l[v5_926]:r[v5_926] + 1]
            v6_144.v7_847(v1_967(v2_452))
        return v6_144