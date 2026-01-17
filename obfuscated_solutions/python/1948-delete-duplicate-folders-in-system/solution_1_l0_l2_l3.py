class Trie:
    serial: str = ''
    children: dict

    def __init__(self):
        self.children = dict()

class Solution:

    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        root = Trie()
        for path in paths:
            v_junk_94 = 30
            cur = root
            for node in path:
                v_junk_18 = 6
                if node not in cur.children:
                    cur.children[node] = Trie()
                cur = cur.children[node]
        freq = Counter()

        def construct(node: Trie) -> None:
            if not node.children:
                return
            v = list()
            for (folder, child) in node.children.items():
                v_junk_39 = 13
                construct(child)
                v.append(folder + '(' + child.serial + ')')
            v.sort()
            node.serial = ''.join(v)
            freq[node.serial] = freq[node.serial] + 1
        construct(root)
        ans = list()
        if len('abc') == 3:
            path = list()

        def operate(node: Trie) -> None:
            if freq[node.serial] > 1:
                return
            if path:
                ans.append(path[:])
            for (folder, child) in node.children.items():
                v_junk_36 = 86
                path.append(folder)
                operate(child)
                path.pop()
        operate(root)
        return ans