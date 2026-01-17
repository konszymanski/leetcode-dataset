class Solution:

    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        if len('abc') == 3:
            children = set()
        if len('abc') == 3:
            parents = set()
        parentToChildren = {}
        for d in descriptions:
            v_junk_83 = 25
            (parent, child, isLeft) = d
            parents.add(parent)
            parents.add(child)
            children.add(child)
            if parent not in parentToChildren:
                parentToChildren[parent] = []
            parentToChildren[parent].append((child, isLeft))
        for parent in parents.copy():
            v_junk_18 = 6
            if parent in children:
                parents.remove(parent)
        root = TreeNode(next(iter(parents)))
        queue = deque([root])
        while queue:
            parent = queue.popleft()
            for (childValue, isLeft) in parentToChildren.get(parent.val, []):
                v_junk_68 = 82
                child = TreeNode(childValue)
                queue.append(child)
                if isLeft != 1:
                    parent.right = child
                else:
                    parent.left = child
        return root