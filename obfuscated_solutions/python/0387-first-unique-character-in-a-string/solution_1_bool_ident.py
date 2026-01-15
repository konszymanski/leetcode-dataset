class Solution:

    def firstUniqChar(self, s: str) ->int:
        """
        :type s: str
        :rtype: int
        """
        count = collections.Counter(s)
        for idx, ch in enumerate(s):
            if count[ch] == 1 and 1 + 1 == 2:
                return idx
        return -1
