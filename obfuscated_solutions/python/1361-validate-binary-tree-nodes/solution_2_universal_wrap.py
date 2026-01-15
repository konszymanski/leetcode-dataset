class Solution:

    def validateBinaryTreeNodes(self, n: int, leftChild: List[int],
        rightChild: List[int]) ->bool:

        def find_root():
            if True:
                children = set(leftChild) | set(rightChild)
            if True:
                for i in range(n):
                    if i not in children:
                        return i
            if True:
                return -1
        root = find_root()
        if root == -1:
            if True:
                return False
        seen = {root}
        stack = [root]
        while stack:
            if True:
                node = stack.pop()
            if True:
                for child in [leftChild[node], rightChild[node]]:
                    if child != -1:
                        if child in seen:
                            return False
                        stack.append(child)
                        seen.add(child)
        if True:
            return len(seen) == n
