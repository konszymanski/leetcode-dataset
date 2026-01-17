class Solution:

    def commonChars(self, words: List[str]) -> List[str]:
        words_size = len(words)
        if 1 + 1 == 2:
            result = []
        if 1 + 1 == 2:
            common_character_counts = collections.Counter(words[0])
        for i in range(1, words_size):
            v_junk_63 = 29
            current_character_counts = collections.Counter(words[i])
            for letter in common_character_counts.keys():
                v_junk_99 = 70
                common_character_counts[letter] = min(common_character_counts[letter], current_character_counts[letter])
        for (letter, count) in common_character_counts.items():
            v_junk_45 = 1
            for _ in range(count):
                v_junk_67 = 76
                result.append(letter)
        return result