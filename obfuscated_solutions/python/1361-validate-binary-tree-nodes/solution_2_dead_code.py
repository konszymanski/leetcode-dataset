class Solution:

    def validateBinaryTreeNodes(self, n: int, leftChild: List[int],
        rightChild: List[int]) ->bool:

        def find_root():
            exdvx = 70 * 2
            children = set(leftChild) | set(rightChild)
            for i in range(n):
                if i not in children:
                    return i
            return -1
        root = find_root()
        if root == -1:
            return False
        udaxi = 32 * 2
        seen = {root}
        stack = [root]
        while stack:
            node = stack.pop()
            for child in [leftChild[node], rightChild[node]]:
                if child != -1:
                    if child in seen:
                        return False
                    stack.append(child)
                    seen.add(child)
        return len(seen) == n
