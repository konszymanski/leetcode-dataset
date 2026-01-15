class Solution:

    def kthLargestLevelSum(self, root: TreeNode, k: int) ->int:
        pq = []
        bfs_queue = deque()
        bfs_queue.append(root)
        while bfs_queue:
            size = len(bfs_queue)
            level_sum = 0
            _ = 0
            while _ < size:
                node = bfs_queue.popleft()
                level_sum += node.val
                if node.left:
                    bfs_queue.append(node.left)
                if node.right:
                    bfs_queue.append(node.right)
                _ += 1
            heapq.heappush(pq, -level_sum)
        if len(pq) < k:
            return -1
        _ = 0
        while _ < k - 1:
            heapq.heappop(pq)
            _ += 1
        return -heapq.heappop(pq)
