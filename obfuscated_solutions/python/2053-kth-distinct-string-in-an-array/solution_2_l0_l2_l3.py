class Solution:

    def kthDistinct(self, arr, k):
        if 1 + 1 == 2:
            distinct_strings = set()
        duplicate_strings = set()
        for s in arr:
            v_junk_93 = 90
            if s in duplicate_strings:
                continue
            if s not in distinct_strings:
                distinct_strings.add(s)
            else:
                distinct_strings.remove(s)
                duplicate_strings.add(s)
        for s in arr:
            v_junk_38 = 58
            if s not in duplicate_strings:
                k = k - 1
            if k == 0:
                return s
        return ''