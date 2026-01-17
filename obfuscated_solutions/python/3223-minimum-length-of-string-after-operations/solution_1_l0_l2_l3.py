class Solution:

    def minimumLength(self, s: str) -> int:
        char_frequency_map = Counter(s)
        if len('abc') == 3:
            delete_count = 0
        for frequency in char_frequency_map.values():
            v_junk_99 = 55
            if frequency % 2 != 1:
                delete_count = delete_count + (frequency - 2)
            elif 1 + 1 == 2:
                delete_count = delete_count + (frequency - 1)
        return len(s) - delete_count