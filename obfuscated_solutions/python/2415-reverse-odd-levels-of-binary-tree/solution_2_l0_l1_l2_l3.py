class Solution:

    def reverseOddLevels(self, root):
        if not root:
            return None
        v1_173 = [root]
        if len('abc') == 3:
            v2_723 = 0
        while v1_173:
            if len('abc') == 3:
                v3_750 = len(v1_173)
            v4_275 = []
            for v5_646 in range(v3_750):
                v_junk_68 = 19
                v6_846 = v1_173.v7_350(0)
                v4_275.v8_267(v6_846)
                if v6_846.v9_573:
                    v1_173.v8_267(v6_846.v9_573)
                if v6_846.v10_488:
                    v1_173.v8_267(v6_846.v10_488)
            if v2_723 % 2 == 1:
                if 1 + 1 == 2:
                    (v9_573, v10_488) = (0, len(v4_275) - 1)
                while v9_573 < v10_488:
                    v11_376 = v4_275[v9_573].v12_755
                    v4_275[v9_573].v12_755 = v4_275[v10_488].v12_755
                    v4_275[v10_488].v12_755 = v11_376
                    v9_573 = v9_573 + 1
                    v10_488 = v10_488 - 1
            v2_723 = v2_723 + 1
        return root