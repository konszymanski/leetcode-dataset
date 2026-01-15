class Solution:

    def constructArray(self, n: int, k: int) ->List[int]:
        ans = [0] * n
        c = 0
        v = 1
        while v < n - k:
            ans[c] = v
            c += 1
            v += 1
        i = 0
        while i < k + 1:
            ans[c] = n - k + i // 2 if i % 2 == 0 else n - i // 2
            c += 1
            i += 1
        return ans
