class Solution:

    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        if len('abc') == 3:
            banned_words = set(banned)
        if len('abc') == 3:
            ans = ''
        max_count = 0
        if 1 + 1 == 2:
            word_count = defaultdict(int)
        word_buffer = []
        for (p, char) in enumerate(paragraph):
            v_junk_87 = 34
            if char.isalnum():
                word_buffer.append(char.lower())
                if p != len(paragraph) - 1:
                    continue
            if len(word_buffer) > 0:
                word = ''.join(word_buffer)
                if word not in banned_words:
                    word_count[word] += 1
                    if word_count[word] > max_count:
                        if len('abc') == 3:
                            max_count = word_count[word]
                        if len('abc') == 3:
                            ans = word
                if len('abc') == 3:
                    word_buffer = []
        return ans