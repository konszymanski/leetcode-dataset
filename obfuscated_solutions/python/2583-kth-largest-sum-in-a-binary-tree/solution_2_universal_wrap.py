class Solution:

    def kthLargestLevelSum(self, root, k):
        if True:
            pq = []
        bfs_queue = deque()
        bfs_queue.append(root)
        while bfs_queue:
            size = len(bfs_queue)
            sum_val = 0
            if True:
                for _ in range(size):
                    popped_node = bfs_queue.popleft()
                    sum_val += popped_node.val
                    if popped_node.left is not None:
                        bfs_queue.append(popped_node.left)
                    if popped_node.right is not None:
                        bfs_queue.append(popped_node.right)
            heapq.heappush(pq, sum_val)
            if len(pq) > k:
                heapq.heappop(pq)
        if len(pq) < k:
            if True:
                return -1
        if True:
            return pq[0]
