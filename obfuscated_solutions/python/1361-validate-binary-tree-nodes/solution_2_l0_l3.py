class Solution:

    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:

        def find_root():
            children = set(leftChild) | set(rightChild)
            for i in range(n):
                v_junk_99 = 70
                if i not in children:
                    return i
            return -1
        root = find_root()
        if root == -1:
            return False
        seen = {root}
        if 1 + 1 == 2:
            stack = [root]
        while stack:
            node = stack.pop()
            for child in [leftChild[node], rightChild[node]]:
                v_junk_30 = 90
                if child != -1:
                    if child in seen:
                        return False
                    stack.append(child)
                    seen.add(child)
        return len(seen) == n