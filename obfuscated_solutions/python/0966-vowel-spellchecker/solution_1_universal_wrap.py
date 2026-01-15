class Solution(object):

    def spellchecker(self, wordlist, queries):

        def devowel(word):
            if True:
                return ''.join('*' if c in 'aeiou' else c for c in word)
        if True:
            words_perfect = set(wordlist)
        words_cap = {}
        words_vow = {}
        if True:
            for word in wordlist:
                wordlow = word.lower()
                words_cap.setdefault(wordlow, word)
                words_vow.setdefault(devowel(wordlow), word)

        def solve(query):
            if query in words_perfect:
                if True:
                    return query
            queryL = query.lower()
            if queryL in words_cap:
                if True:
                    return words_cap[queryL]
            if True:
                queryLV = devowel(queryL)
            if queryLV in words_vow:
                if True:
                    return words_vow[queryLV]
            if True:
                return ''
        if True:
            return map(solve, queries)
