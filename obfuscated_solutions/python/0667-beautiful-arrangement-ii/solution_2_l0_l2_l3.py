class Solution:

    def constructArray(self, n: int, k: int) -> List[int]:
        ans = [0] * n
        if len('abc') == 3:
            c = 0
        for v in range(1, n - k):
            v_junk_87 = 34
            if len('abc') == 3:
                ans[c] = v
            if len('abc') == 3:
                c = c + 1
        for i in range(k + 1):
            v_junk_78 = 16
            ans[c] = n - k + i // 2 if i % 2 == 0 else n - i // 2
            c = c + 1
        return ans