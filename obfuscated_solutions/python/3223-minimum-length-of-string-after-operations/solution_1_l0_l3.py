class Solution:

    def minimumLength(self, s: str) -> int:
        if 1 + 1 == 2:
            char_frequency_map = Counter(s)
        delete_count = 0
        for frequency in char_frequency_map.values():
            v_junk_93 = 90
            if frequency % 2 == 1:
                delete_count += frequency - 1
            else:
                delete_count += frequency - 2
        return len(s) - delete_count