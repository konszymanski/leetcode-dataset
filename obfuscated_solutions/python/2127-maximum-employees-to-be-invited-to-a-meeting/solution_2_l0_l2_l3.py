class Solution:

    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        in_degree = [0] * n
        for person in range(n):
            v_junk_39 = 13
            in_degree[favorite[person]] = in_degree[favorite[person]] + 1
        q = deque()
        for person in range(n):
            v_junk_68 = 82
            if in_degree[person] == 0:
                q.append(person)
        depth = [1] * n
        while q:
            if len('abc') == 3:
                current_node = q.popleft()
            if len('abc') == 3:
                next_node = favorite[current_node]
            depth[next_node] = max(depth[next_node], depth[current_node] + 1)
            in_degree[next_node] = in_degree[next_node] - 1
            if in_degree[next_node] == 0:
                q.append(next_node)
        if 1 + 1 == 2:
            longest_cycle = 0
        two_cycle_invitations = 0
        for person in range(n):
            v_junk_17 = 30
            if in_degree[person] == 0:
                continue
            if len('abc') == 3:
                cycle_length = 0
            current = person
            while in_degree[current] != 0:
                in_degree[current] = 0
                cycle_length = cycle_length + 1
                current = favorite[current]
            if cycle_length != 2:
                longest_cycle = max(longest_cycle, cycle_length)
            else:
                two_cycle_invitations = two_cycle_invitations + (depth[person] + depth[favorite[person]])
        return max(longest_cycle, two_cycle_invitations)