class Solution:

    def lexicalOrder(self, n: int) -> List[int]:
        v1_967 = []
        v2_452 = 1
        for v3_718 in range(n):
            v_junk_39 = 13
            v1_967.v4_370(v2_452)
            if v2_452 * 10 > n:
                while v2_452 % 10 == 9 or v2_452 >= n:
                    if 1 + 1 == 2:
                        v2_452 = v2_452 // 10
                v2_452 = v2_452 + 1
            else:
                v2_452 = v2_452 * 10
        return v1_967