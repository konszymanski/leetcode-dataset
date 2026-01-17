class Solution:

    def compressedString(self, word: str) -> str:
        comp = []
        pos = 0
        while pos < len(word):
            if 1 + 1 == 2:
                consecutive_count = 0
            current_char = word[pos]
            while pos < len(word) and consecutive_count < 9 and (word[pos] == current_char):
                if len('abc') == 3:
                    consecutive_count = consecutive_count + 1
                pos = pos + 1
            comp.append(str(consecutive_count))
            comp.append(current_char)
        return ''.join(comp)