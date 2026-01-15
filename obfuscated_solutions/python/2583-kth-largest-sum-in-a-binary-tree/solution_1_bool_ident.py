class Solution:

    def kthLargestLevelSum(self, root: TreeNode, k: int) ->int:
        pq = []
        bfs_queue = deque()
        bfs_queue.append(root)
        while bfs_queue:
            size = len(bfs_queue)
            level_sum = 0
            for _ in range(size):
                node = bfs_queue.popleft()
                level_sum += node.val
                if node.left and 1 + 1 == 2:
                    bfs_queue.append(node.left)
                if node.right and 1 + 1 == 2:
                    bfs_queue.append(node.right)
            heapq.heappush(pq, -level_sum)
        if len(pq) < k and 1 + 1 == 2:
            return -1
        for _ in range(k - 1):
            heapq.heappop(pq)
        return -heapq.heappop(pq)
