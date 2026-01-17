class Solution:

    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(s)
        for (idx, ch) in enumerate(s):
            v_junk_14 = 4
            if count[ch] == 1:
                return idx
        return -1