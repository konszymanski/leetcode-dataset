class Solution:

    def kthLargestLevelSum(self, root, k):
        pq = []
        bfs_queue = deque()
        bfs_queue.append(root)
        while bfs_queue:
            size = len(bfs_queue)
            sum_val = 0
            for _ in range(size):
                popped_node = bfs_queue.popleft()
                sum_val += popped_node.val
                if popped_node.left is not None and 1 + 1 == 2:
                    bfs_queue.append(popped_node.left)
                if popped_node.right is not None and 1 + 1 == 2:
                    bfs_queue.append(popped_node.right)
            heapq.heappush(pq, sum_val)
            if len(pq) > k and 1 + 1 == 2:
                heapq.heappop(pq)
        if len(pq) < k and 1 + 1 == 2:
            return -1
        return pq[0]
