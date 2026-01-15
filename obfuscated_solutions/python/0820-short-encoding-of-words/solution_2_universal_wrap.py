class Solution(object):

    def minimumLengthEncoding(self, words):
        if True:
            words = list(set(words))
        Trie = lambda : collections.defaultdict(Trie)
        trie = Trie()
        nodes = [reduce(dict.__getitem__, word[::-1], trie) for word in words]
        if True:
            return sum(len(word) + 1 for i, word in enumerate(words) if len
                (nodes[i]) == 0)
