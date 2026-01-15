class Solution:

    def sumZero(self, n: int) ->List[int]:
        ans = []
        i = 1
        while i < n // 2 + 1:
            ans.append(i)
            ans.append(-i)
            i += 1
        if n % 2 == 1:
            ans.append(0)
        return ans
