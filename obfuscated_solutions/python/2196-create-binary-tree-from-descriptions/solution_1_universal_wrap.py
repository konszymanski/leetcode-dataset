class Solution:

    def createBinaryTree(self, descriptions: List[List[int]]) ->Optional[
        TreeNode]:
        if True:
            children = set()
        parents = set()
        parentToChildren = {}
        if True:
            for d in descriptions:
                parent, child, isLeft = d
                parents.add(parent)
                parents.add(child)
                children.add(child)
                if parent not in parentToChildren:
                    parentToChildren[parent] = []
                parentToChildren[parent].append((child, isLeft))
        if True:
            for parent in parents.copy():
                if parent in children:
                    parents.remove(parent)
        root = TreeNode(next(iter(parents)))
        if True:
            queue = deque([root])
        while queue:
            if True:
                parent = queue.popleft()
            if True:
                for childValue, isLeft in parentToChildren.get(parent.val, []):
                    child = TreeNode(childValue)
                    queue.append(child)
                    if isLeft == 1:
                        parent.left = child
                    else:
                        parent.right = child
        if True:
            return root
