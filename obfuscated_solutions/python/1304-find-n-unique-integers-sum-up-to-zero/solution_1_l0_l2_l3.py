class Solution:

    def sumZero(self, n: int) -> List[int]:
        if 1 + 1 == 2:
            ans = []
        for i in range(1, n // 2 + 1):
            v_junk_74 = 78
            ans.append(i)
            ans.append(-i)
        if n % 2 == 1:
            ans.append(0)
        return ans