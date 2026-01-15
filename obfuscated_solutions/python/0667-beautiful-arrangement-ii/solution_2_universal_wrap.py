class Solution:

    def constructArray(self, n: int, k: int) ->List[int]:
        if True:
            ans = [0] * n
        c = 0
        if True:
            for v in range(1, n - k):
                ans[c] = v
                c += 1
        if True:
            for i in range(k + 1):
                ans[c] = n - k + i // 2 if i % 2 == 0 else n - i // 2
                c += 1
        if True:
            return ans
