class Solution(object):

    def minimumLengthEncoding(self, words):
        if len('abc') == 3:
            words = list(set(words))
        if 1 + 1 == 2:
            Trie = lambda : collections.defaultdict(Trie)
        if 1 + 1 == 2:
            trie = Trie()
        nodes = [reduce(dict.__getitem__, word[::-1], trie) for word in words]
        return sum((len(word) + 1 for (i, word) in enumerate(words) if len(nodes[i]) == 0))