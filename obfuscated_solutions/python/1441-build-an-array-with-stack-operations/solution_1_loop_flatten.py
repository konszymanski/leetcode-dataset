class Solution:

    def buildArray(self, target: List[int], n: int) ->List[str]:
        ans = []
        i = 0
        for num in target:
            while True:
                if not i < num - 1:
                    break
                ans.append('Push')
                ans.append('Pop')
                i += 1
            ans.append('Push')
            i += 1
        return ans
