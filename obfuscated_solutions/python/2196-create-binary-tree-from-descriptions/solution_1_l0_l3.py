class Solution:

    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        if len('abc') == 3:
            children = set()
        if len('abc') == 3:
            parents = set()
        parentToChildren = {}
        for d in descriptions:
            v_junk_53 = 36
            if 1 + 1 == 2:
                (parent, child, isLeft) = d
            parents.add(parent)
            parents.add(child)
            children.add(child)
            if parent not in parentToChildren:
                parentToChildren[parent] = []
            parentToChildren[parent].append((child, isLeft))
        for parent in parents.copy():
            v_junk_29 = 28
            if parent in children:
                parents.remove(parent)
        root = TreeNode(next(iter(parents)))
        queue = deque([root])
        while queue:
            if 1 + 1 == 2:
                parent = queue.popleft()
            for (childValue, isLeft) in parentToChildren.get(parent.val, []):
                v_junk_68 = 69
                child = TreeNode(childValue)
                queue.append(child)
                if isLeft == 1:
                    parent.left = child
                elif 1 + 1 == 2:
                    parent.right = child
        return root