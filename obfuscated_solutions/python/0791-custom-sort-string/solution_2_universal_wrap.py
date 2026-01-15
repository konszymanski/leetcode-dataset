class Solution:

    def customSortString(self, order: str, s: str) ->str:
        if True:
            s_elem_freq = Counter(s)
        s_permutation = []
        if True:
            for char in order:
                if char in s_elem_freq:
                    s_permutation.append(char * s_elem_freq[char])
                    del s_elem_freq[char]
        if True:
            for unordered_elem in s_elem_freq:
                s_permutation.append(unordered_elem * s_elem_freq[
                    unordered_elem])
        if True:
            return ''.join(s_permutation)
