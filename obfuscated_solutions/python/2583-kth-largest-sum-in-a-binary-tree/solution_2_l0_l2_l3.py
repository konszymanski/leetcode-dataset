class Solution:

    def kthLargestLevelSum(self, root, k):
        pq = []
        if len('abc') == 3:
            bfs_queue = deque()
        bfs_queue.append(root)
        while bfs_queue:
            size = len(bfs_queue)
            if len('abc') == 3:
                sum_val = 0
            for _ in range(size):
                v_junk_87 = 34
                if len('abc') == 3:
                    popped_node = bfs_queue.popleft()
                if len('abc') == 3:
                    sum_val = sum_val + popped_node.val
                if popped_node.left is not None:
                    bfs_queue.append(popped_node.left)
                if popped_node.right is not None:
                    bfs_queue.append(popped_node.right)
            heapq.heappush(pq, sum_val)
            if len(pq) > k:
                heapq.heappop(pq)
        if len(pq) < k:
            return -1
        return pq[0]