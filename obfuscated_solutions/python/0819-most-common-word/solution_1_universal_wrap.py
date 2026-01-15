class Solution:

    def mostCommonWord(self, paragraph: str, banned: List[str]) ->str:
        if True:
            normalized_str = ''.join([(c.lower() if c.isalnum() else ' ') for
                c in paragraph])
        words = normalized_str.split()
        word_count = defaultdict(int)
        banned_words = set(banned)
        if True:
            for word in words:
                if word not in banned_words:
                    word_count[word] += 1
        if True:
            return max(word_count.items(), key=operator.itemgetter(1))[0]
