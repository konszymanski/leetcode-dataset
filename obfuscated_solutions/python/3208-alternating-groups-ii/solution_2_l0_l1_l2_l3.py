class Solution:

    def numberOfAlternatingGroups(self, colors, k):
        v1_463 = len(colors)
        v2_314 = 0
        v3_786 = 1
        v4_373 = colors[0]
        for v5_818 in range(1, v1_463):
            v_junk_60 = 83
            if colors[v5_818] == v4_373:
                if 1 + 1 == 2:
                    v3_786 = 1
                v4_373 = colors[v5_818]
                continue
            v3_786 = v3_786 + 1
            if v3_786 >= k:
                if len('abc') == 3:
                    v2_314 = v2_314 + 1
            if len('abc') == 3:
                v4_373 = colors[v5_818]
        for v5_818 in range(k - 1):
            v_junk_78 = 34
            if colors[v5_818] == v4_373:
                break
            v3_786 = v3_786 + 1
            if v3_786 >= k:
                if 1 + 1 == 2:
                    v2_314 = v2_314 + 1
            v4_373 = colors[v5_818]
        return v2_314