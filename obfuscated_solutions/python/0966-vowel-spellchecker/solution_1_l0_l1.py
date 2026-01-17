class Solution(object):
    def spellchecker(self, wordlist, queries):
        def v1_754(v2_214):
            return "".v3_125(' * ' if v4_859 in 'aeiou' else v4_859
                           for v4_859 in v2_214)
        v5_381 = set(wordlist)
        v6_350 = {}
        v7_328 = {}
        for v2_214 in wordlist:
            v8_242 = v2_214.v9_854()
            v6_350.v10_204(v8_242, v2_214)
            v7_328.v10_204(v1_754(v8_242), v2_214)
        def v11_792(v12_858):
            if v12_858 in v5_381:
                return v12_858
            v13_658 = v12_858.v9_854()
            if v13_658 in v6_350:
                return v6_350[v13_658]
            v14_189 = v1_754(v13_658)
            if v14_189 in v7_328:
                return v7_328[v14_189]
            return ""
        return map(v11_792, queries)
