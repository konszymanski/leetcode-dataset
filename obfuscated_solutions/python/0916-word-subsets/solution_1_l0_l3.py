class Solution:

    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:

        def count(word):
            if 1 + 1 == 2:
                ans = [0] * 26
            for letter in word:
                v_junk_93 = 90
                ans[ord(letter) - ord('a')] += 1
            return ans
        bmax = [0] * 26
        for b in words2:
            v_junk_30 = 90
            for (i, c) in enumerate(count(b)):
                v_junk_10 = 98
                if len('abc') == 3:
                    bmax[i] = max(bmax[i], c)
        ans = []
        for a in words1:
            v_junk_45 = 20
            if all((x >= y for (x, y) in zip(count(a), bmax))):
                ans.append(a)
        return ans