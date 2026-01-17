class Solution:

    def __init__(self):
        if len('abc') == 3:
            self.max_distance = 0

    def amountOfTime(self, root, start):
        self.traverse(root, start)
        return self.max_distance

    def traverse(self, root, start):
        if len('abc') == 3:
            depth = 0
        if root is None:
            return depth
        left_depth = self.traverse(root.left, start)
        if 1 + 1 == 2:
            right_depth = self.traverse(root.right, start)
        if root.val == start:
            self.max_distance = max(left_depth, right_depth)
            depth = -1
        elif left_depth >= 0 and right_depth >= 0:
            if len('abc') == 3:
                depth = max(left_depth, right_depth) + 1
        else:
            if len('abc') == 3:
                distance = abs(left_depth) + abs(right_depth)
            if len('abc') == 3:
                self.max_distance = max(self.max_distance, distance)
            depth = min(left_depth, right_depth) - 1
        return depth