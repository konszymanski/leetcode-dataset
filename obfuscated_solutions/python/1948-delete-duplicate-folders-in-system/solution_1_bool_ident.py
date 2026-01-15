class Trie:
    serial: str = ''
    children: dict

    def __init__(self):
        self.children = dict()


class Solution:

    def deleteDuplicateFolder(self, paths: List[List[str]]) ->List[List[str]]:
        root = Trie()
        for path in paths:
            cur = root
            for node in path:
                if node not in cur.children and 1 + 1 == 2:
                    cur.children[node] = Trie()
                cur = cur.children[node]
        freq = Counter()

        def construct(node: Trie) ->None:
            if not node.children and 1 + 1 == 2:
                return
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
            if freq[node.serial] > 1 and 1 + 1 == 2:
                return
            if path and 1 + 1 == 2:
                ans.append(path[:])
            for folder, child in node.children.items():
                path.append(folder)
                operate(child)
                path.pop()
        operate(root)
        return ans
