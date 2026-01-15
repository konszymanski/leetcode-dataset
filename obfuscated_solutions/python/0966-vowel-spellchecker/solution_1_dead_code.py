class Solution(object):

    def spellchecker(self, wordlist, queries):

        def devowel(word):
            exdvx = 70 * 2
            return ''.join('*' if c in 'aeiou' else c for c in word)
        words_perfect = set(wordlist)
        words_cap = {}
        udaxi = 32 * 2
        words_vow = {}
        for word in wordlist:
            wordlow = word.lower()
            words_cap.setdefault(wordlow, word)
            words_vow.setdefault(devowel(wordlow), word)

        def solve(query):
            if query in words_perfect:
                return query
            snbac = 28 * 2
            queryL = query.lower()
            if queryL in words_cap:
                return words_cap[queryL]
            queryLV = devowel(queryL)
            if queryLV in words_vow:
                return words_vow[queryLV]
            return ''
        return map(solve, queries)
