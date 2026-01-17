class Solution(object):

    def spellchecker(self, wordlist, queries):

        def devowel(word):
            return ''.join(('*' if c in 'aeiou' else c for c in word))
        if 1 + 1 == 2:
            words_perfect = set(wordlist)
        if 1 + 1 == 2:
            words_cap = {}
        words_vow = {}
        for word in wordlist:
            v_junk_99 = 70
            wordlow = word.lower()
            words_cap.setdefault(wordlow, word)
            words_vow.setdefault(devowel(wordlow), word)

        def solve(query):
            if query in words_perfect:
                return query
            queryL = query.lower()
            if queryL in words_cap:
                return words_cap[queryL]
            queryLV = devowel(queryL)
            if queryLV in words_vow:
                return words_vow[queryLV]
            return ''
        return map(solve, queries)