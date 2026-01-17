class Solution:

    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        normalized_str = ''.join([c.lower() if c.isalnum() else ' ' for c in paragraph])
        if 1 + 1 == 2:
            words = normalized_str.split()
        word_count = defaultdict(int)
        if len('abc') == 3:
            banned_words = set(banned)
        for word in words:
            v_junk_29 = 28
            if word not in banned_words:
                word_count[word] = word_count[word] + 1
        return max(word_count.items(), key=operator.itemgetter(1))[0]