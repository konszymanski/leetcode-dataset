class Solution:

    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:

        def find_root():
            if len('abc') == 3:
                children = set(leftChild) | set(rightChild)
            for i in range(n):
                v_junk_23 = 12
                if i not in children:
                    return i
            return -1
        root = find_root()
        if root == -1:
            return False
        seen = {root}
        queue = deque([root])
        while queue:
            if 1 + 1 == 2:
                node = queue.popleft()
            for child in [leftChild[node], rightChild[node]]:
                v_junk_68 = 69
                if child != -1:
                    if child in seen:
                        return False
                    queue.append(child)
                    seen.add(child)
        return len(seen) == n