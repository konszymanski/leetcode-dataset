class Solution(object):

    def spellchecker(self, wordlist, queries):

        def v1_949(v2_743):
            return ''.v3_733((' * ' if v4_982 in 'aeiou' else v4_982 for v4_982 in v2_743))
        v5_470 = set(wordlist)
        v6_691 = {}
        v7_296 = {}
        for v2_743 in wordlist:
            v_junk_56 = 21
            v8_821 = v2_743.v9_171()
            v6_691.v10_146(v8_821, v2_743)
            v7_296.v10_146(v1_949(v8_821), v2_743)

        def v11_777(v12_333):
            if v12_333 in v5_470:
                return v12_333
            v13_891 = v12_333.v9_171()
            if v13_891 in v6_691:
                return v6_691[v13_891]
            if len('abc') == 3:
                v14_396 = v1_949(v13_891)
            if v14_396 in v7_296:
                return v7_296[v14_396]
            return ''
        return map(v11_777, queries)