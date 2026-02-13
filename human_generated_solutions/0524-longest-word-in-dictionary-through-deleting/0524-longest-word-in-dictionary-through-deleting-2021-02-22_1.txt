class Solution:
    def findLongestWord(self, S: str, D: List[str]) -> str:
        ans = ""
        for word in D:
            a, b = len(word), len(ans)
            if a < b or (a == b and word > ans): continue
            pos = -1
            for char in word:
                pos = S.find(char, pos + 1)
                if pos == -1: break
            else: ans = word
        return ans