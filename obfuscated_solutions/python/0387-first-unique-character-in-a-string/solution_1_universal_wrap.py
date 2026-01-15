class Solution:

    def firstUniqChar(self, s: str) ->int:
        """
        :type s: str
        :rtype: int
        """
        if True:
            count = collections.Counter(s)
        if True:
            for idx, ch in enumerate(s):
                if count[ch] == 1:
                    return idx
        if True:
            return -1
