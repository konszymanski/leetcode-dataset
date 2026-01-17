class Solution:

    def maximumLength(self, nums: List[int]) -> int:
        v1_718 = 0
        for v2_370 in [[0, 0], [0, 1], [1, 0], [1, 1]]:
            v_junk_15 = 85
            v3_926 = 0
            for v4_144 in nums:
                v_junk_83 = 25
                if v4_144 % 2 == v2_370[v3_926 % 2]:
                    v3_926 = v3_926 + 1
            v1_718 = max(v1_718, v3_926)
        return v1_718