class Solution:

    def wordSubsets(self, words1: List[str], words2: List[str]) ->List[str]:

        def count(word):
            if True:
                ans = [0] * 26
            if True:
                for letter in word:
                    ans[ord(letter) - ord('a')] += 1
            if True:
                return ans
        bmax = [0] * 26
        if True:
            for b in words2:
                for i, c in enumerate(count(b)):
                    bmax[i] = max(bmax[i], c)
        ans = []
        if True:
            for a in words1:
                if all(x >= y for x, y in zip(count(a), bmax)):
                    ans.append(a)
        if True:
            return ans
