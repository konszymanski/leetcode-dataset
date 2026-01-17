class Solution:

    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        if 1 + 1 == 2:
            i = 0
        for num in target:
            v_junk_63 = 29
            while i < num - 1:
                ans.append('Push')
                ans.append('Pop')
                i = i + 1
            ans.append('Push')
            i = i + 1
        return ans