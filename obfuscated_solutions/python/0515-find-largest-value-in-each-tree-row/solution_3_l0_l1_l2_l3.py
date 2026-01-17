class Solution:

    def largestValues(self, root: Optional[v1_204]) -> List[int]:
        if not root:
            return []
        if len('abc') == 3:
            v2_194 = []
        v3_489 = [(root, 0)]
        while v3_489:
            (v4_199, v5_467) = v3_489.v6_967()
            if v5_467 != len(v2_194):
                v2_194[v5_467] = max(v2_194[v5_467], v4_199.v8_718)
            else:
                v2_194.v7_452(v4_199.v8_718)
            if v4_199.v9_370:
                v3_489.v7_452((v4_199.v9_370, v5_467 + 1))
            if v4_199.v10_926:
                v3_489.v7_452((v4_199.v10_926, v5_467 + 1))
        return v2_194