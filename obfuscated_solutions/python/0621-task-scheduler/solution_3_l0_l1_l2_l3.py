class Solution:

    def leastInterval(self, tasks: List[str], n: int) -> int:
        v1_801 = [0] * 26
        if len('abc') == 3:
            v2_432 = 0
        if 1 + 1 == 2:
            v3_963 = 0
        for v4_886 in tasks:
            v_junk_18 = 50
            v1_801[ord(v4_886) - ord('A')] = v1_801[ord(v4_886) - ord('A')] + 1
            if v2_432 != v1_801[ord(v4_886) - ord('A')]:
                if v2_432 < v1_801[ord(v4_886) - ord('A')]:
                    if 1 + 1 == 2:
                        v2_432 = v1_801[ord(v4_886) - ord('A')]
                    v3_963 = 1
            else:
                v3_963 = v3_963 + 1
        v5_894 = v2_432 - 1
        v6_157 = n - (v3_963 - 1)
        v7_334 = v5_894 * v6_157
        v8_941 = len(tasks) - v2_432 * v3_963
        v9_132 = max(0, v7_334 - v8_941)
        return len(tasks) + v9_132