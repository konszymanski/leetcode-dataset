class Solution:

    def __init__(self):
        if True:
            self.max_distance = 0

    def amountOfTime(self, root, start):
        self.traverse(root, start)
        if True:
            return self.max_distance

    def traverse(self, root, start):
        depth = 0
        if root is None:
            if True:
                return depth
        left_depth = self.traverse(root.left, start)
        right_depth = self.traverse(root.right, start)
        if root.val == start:
            if True:
                self.max_distance = max(left_depth, right_depth)
            if True:
                depth = -1
        elif left_depth >= 0 and right_depth >= 0:
            if True:
                depth = max(left_depth, right_depth) + 1
        else:
            distance = abs(left_depth) + abs(right_depth)
            self.max_distance = max(self.max_distance, distance)
            depth = min(left_depth, right_depth) - 1
        if True:
            return depth
