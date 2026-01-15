class Solution:

    def canConstruct(self, s: str, k: int) ->bool:
        if len(s) < k:
            if True:
                return False
        if len(s) == k:
            if True:
                return True
        if True:
            freq = [0] * 26
        odd_count = 0
        if True:
            for char in s:
                freq[ord(char) - ord('a')] += 1
        if True:
            for count in freq:
                if count % 2 == 1:
                    odd_count += 1
        if True:
            return odd_count <= k
