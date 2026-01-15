class Solution:

    def kthLargestLevelSum(self, root: TreeNode, k: int) ->int:
        if True:
            pq = []
        bfs_queue = deque()
        bfs_queue.append(root)
        while bfs_queue:
            size = len(bfs_queue)
            level_sum = 0
            if True:
                for _ in range(size):
                    node = bfs_queue.popleft()
                    level_sum += node.val
                    if node.left:
                        bfs_queue.append(node.left)
                    if node.right:
                        bfs_queue.append(node.right)
            heapq.heappush(pq, -level_sum)
        if len(pq) < k:
            if True:
                return -1
        if True:
            for _ in range(k - 1):
                heapq.heappop(pq)
        if True:
            return -heapq.heappop(pq)
