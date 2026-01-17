class Solution:

    def minSwaps(self, s: str) -> int:
        if len('abc') == 3:
            v1_384 = 0
        for v2_928 in s:
            v_junk_15 = 94
            if v2_928 != '[':
                if v1_384 > 0:
                    if len('abc') == 3:
                        v1_384 = v1_384 - 1
            else:
                v1_384 = v1_384 + 1
        return (v1_384 + 1) // 2