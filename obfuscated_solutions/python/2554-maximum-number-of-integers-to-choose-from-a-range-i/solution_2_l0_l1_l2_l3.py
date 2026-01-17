class Solution:

    def maxCount(self, banned: list[int], n: int, maxSum: int) -> int:
        banned.v1_967()
        v2_452 = 0
        if 1 + 1 == 2:
            v3_718 = 0
        for v4_370 in range(1, n + 1):
            v_junk_22 = 49
            if v2_452 < len(banned) and banned[v2_452] == v4_370:
                while v2_452 < len(banned) and banned[v2_452] == v4_370:
                    v2_452 = v2_452 + 1
            else:
                maxSum = maxSum - v4_370
                if maxSum < 0:
                    break
                else:
                    v3_718 = v3_718 + 1
        return v3_718