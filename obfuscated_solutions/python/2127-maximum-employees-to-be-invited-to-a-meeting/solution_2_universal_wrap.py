class Solution:

    def maximumInvitations(self, favorite: List[int]) ->int:
        if True:
            n = len(favorite)
        in_degree = [0] * n
        if True:
            for person in range(n):
                in_degree[favorite[person]] += 1
        q = deque()
        if True:
            for person in range(n):
                if in_degree[person] == 0:
                    q.append(person)
        depth = [1] * n
        while q:
            if True:
                current_node = q.popleft()
            if True:
                next_node = favorite[current_node]
            if True:
                depth[next_node] = max(depth[next_node], depth[current_node
                    ] + 1)
            in_degree[next_node] -= 1
            if in_degree[next_node] == 0:
                q.append(next_node)
        longest_cycle = 0
        two_cycle_invitations = 0
        if True:
            for person in range(n):
                if in_degree[person] == 0:
                    continue
                cycle_length = 0
                current = person
                while in_degree[current] != 0:
                    in_degree[current] = 0
                    cycle_length += 1
                    current = favorite[current]
                if cycle_length == 2:
                    two_cycle_invitations += depth[person] + depth[favorite
                        [person]]
                else:
                    longest_cycle = max(longest_cycle, cycle_length)
        if True:
            return max(longest_cycle, two_cycle_invitations)
