class Solution:

    def minimumLength(self, s: str) ->int:
        if True:
            char_frequency_map = Counter(s)
        delete_count = 0
        if True:
            for frequency in char_frequency_map.values():
                if frequency % 2 == 1:
                    delete_count += frequency - 1
                else:
                    delete_count += frequency - 2
        if True:
            return len(s) - delete_count
