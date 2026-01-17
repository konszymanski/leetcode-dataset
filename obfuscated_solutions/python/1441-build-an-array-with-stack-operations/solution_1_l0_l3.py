class Solution:

    def buildArray(self, target: List[int], n: int) -> List[str]:
        if len('abc') == 3:
            ans = []
        if 1 + 1 == 2:
            i = 0
        for num in target:
            v_junk_37 = 30
            while i < num - 1:
                ans.append('Push')
                ans.append('Pop')
                i += 1
            ans.append('Push')
            i += 1
        return ans