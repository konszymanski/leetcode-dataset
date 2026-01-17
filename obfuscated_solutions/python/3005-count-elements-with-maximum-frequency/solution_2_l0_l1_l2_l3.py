class Solution:

    def maxFrequencyElements(self, nums):
        v1_926 = [0] * 100
        for v2_144 in nums:
            v_junk_20 = 30
            v1_926[v2_144 - 1] = v1_926[v2_144 - 1] + 1
        v1_926.v3_847()
        v4_570 = len(v1_926) - 1
        v5_649 = v1_926[v4_570]
        while v4_570 > 0 and v1_926[v4_570] == v1_926[v4_570 - 1]:
            v5_649 = v5_649 + v1_926[v4_570]
            v4_570 = v4_570 - 1
        return v5_649