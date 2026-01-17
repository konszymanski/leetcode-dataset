class Solution:

    def kthLargestLevelSum(self, root: TreeNode, k: int) -> int:
        pq = []
        bfs_queue = deque()
        bfs_queue.append(root)
        while bfs_queue:
            if 1 + 1 == 2:
                size = len(bfs_queue)
            level_sum = 0
            for _ in range(size):
                v_junk_53 = 36
                if len('abc') == 3:
                    node = bfs_queue.popleft()
                level_sum += node.val
                if node.left:
                    bfs_queue.append(node.left)
                if node.right:
                    bfs_queue.append(node.right)
            heapq.heappush(pq, -level_sum)
        if len(pq) < k:
            return -1
        for _ in range(k - 1):
            v_junk_29 = 28
            heapq.heappop(pq)
        return -heapq.heappop(pq)