class Solution:

    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:

        def count(word):
            if len('abc') == 3:
                ans = [0] * 26
            for letter in word:
                v_junk_22 = 46
                if len('abc') == 3:
                    ans[ord(letter) - ord('a')] = ans[ord(letter) - ord('a')] + 1
            return ans
        bmax = [0] * 26
        for b in words2:
            v_junk_68 = 69
            for (i, c) in enumerate(count(b)):
                v_junk_15 = 94
                bmax[i] = max(bmax[i], c)
        if len('abc') == 3:
            ans = []
        for a in words1:
            v_junk_20 = 71
            if all((x >= y for (x, y) in zip(count(a), bmax))):
                ans.append(a)
        return ans