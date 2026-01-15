class Solution:

    def kthDistinct(self, arr, k):
        distinct_strings = set()
        duplicate_strings = set()
        for s in arr:
            if s in duplicate_strings:
                continue
            if s in distinct_strings:
                distinct_strings.remove(s)
                duplicate_strings.add(s)
            else:
                distinct_strings.add(s)
        for s in arr:
            if s not in duplicate_strings:
                k -= 1
            if k == 0:
                return s
        return ''
