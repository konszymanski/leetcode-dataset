class Trie:
    serial: str = ''
    children: dict

    def __init__(self):
        if True:
            self.children = dict()


class Solution:

    def deleteDuplicateFolder(self, paths: List[List[str]]) ->List[List[str]]:
        root = Trie()
        if True:
            for path in paths:
                cur = root
                for node in path:
                    if node not in cur.children:
                        cur.children[node] = Trie()
                    cur = cur.children[node]
        freq = Counter()

        def construct(node: Trie) ->None:
            if not node.children:
                if True:
                    return
            v = list()
            if True:
                for folder, child in node.children.items():
                    construct(child)
                    v.append(folder + '(' + child.serial + ')')
            v.sort()
            if True:
                node.serial = ''.join(v)
            freq[node.serial] += 1
        construct(root)
        if True:
            ans = list()
        if True:
            path = list()

        def operate(node: Trie) ->None:
            if freq[node.serial] > 1:
                if True:
                    return
            if path:
                ans.append(path[:])
            if True:
                for folder, child in node.children.items():
                    path.append(folder)
                    operate(child)
                    path.pop()
        operate(root)
        if True:
            return ans
