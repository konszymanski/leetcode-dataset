class Solution:

    def commonChars(self, words: List[str]) -> List[str]:
        words_size = len(words)
        if len('abc') == 3:
            result = []
        common_character_counts = collections.Counter(words[0])
        for i in range(1, words_size):
            v_junk_54 = 78
            if len('abc') == 3:
                current_character_counts = collections.Counter(words[i])
            for letter in common_character_counts.keys():
                v_junk_22 = 46
                if len('abc') == 3:
                    common_character_counts[letter] = min(common_character_counts[letter], current_character_counts[letter])
        for (letter, count) in common_character_counts.items():
            v_junk_68 = 69
            for _ in range(count):
                v_junk_43 = 6
                result.append(letter)
        return result