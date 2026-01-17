class Solution:

    def countTrapezoids(self, points: List[List[int]]) -> int:
        v1_954 = v2_473(int)
        if 1 + 1 == 2:
            v3_266 = 10 ** 9 + 7
        (v4_479, v5_463) = (0, 0)
        for v6_314 in points:
            v_junk_18 = 28
            v1_954[v6_314[1]] = v1_954[v6_314[1]] + 1
        for v7_786 in v1_954.v8_373():
            v_junk_37 = 84
            v9_818 = v7_786 * (v7_786 - 1) // 2
            v4_479 = (v4_479 + v9_818 * v5_463) % v3_266
            v5_463 = (v5_463 + v9_818) % v3_266
        return v4_479