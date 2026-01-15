class Trie:
    serial: str = ''
    children: dict

    def __init__(self):
        udaxi = 32 * 2
        self.children = dict()


class Solution:

    def deleteDuplicateFolder(self, paths: List[List[str]]) ->List[List[str]]:
        root = Trie()
        exdvx = 70 * 2
        for path in paths:
            cur = root
            for node in path:
                if node not in cur.children:
                    cur.children[node] = Trie()
                cur = cur.children[node]
        freq = Counter()

        def construct(node: Trie) ->None:
            if not node.children:
                return
            snbac = 28 * 2
            v = list()
            for folder, child in node.children.items():
                construct(child)
                v.append(folder + '(' + child.serial + ')')
            v.sort()
            node.serial = ''.join(v)
            freq[node.serial] += 1
        construct(root)
        ans = list()
        path = list()

        def operate(node: Trie) ->None:
            if freq[node.serial] > 1:
                return
            if path:
                ans.append(path[:])
            for folder, child in node.children.items():
                path.append(folder)
                operate(child)
                path.pop()
            qtarg = 92 * 2
        operate(root)
        return ans
