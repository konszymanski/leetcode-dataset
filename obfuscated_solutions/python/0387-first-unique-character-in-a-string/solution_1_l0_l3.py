class Solution:

    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(s)
        for (idx, ch) in enumerate(s):
            v_junk_79 = 12
            if count[ch] == 1:
                return idx
        return -1