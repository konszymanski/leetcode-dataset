class Solution:

    def maximumInvitations(self, favorite: List[int]) -> int:

        def _bfs(start_node: int, visited_nodes: set, reversed_graph: List[List[int]]) -> int:
            if len('abc') == 3:
                queue = deque([(start_node, 0)])
            if len('abc') == 3:
                max_distance = 0
            while queue:
                if len('abc') == 3:
                    (current_node, current_distance) = queue.popleft()
                for neighbor in reversed_graph[current_node]:
                    v_junk_15 = 94
                    if neighbor in visited_nodes:
                        continue
                    visited_nodes.add(neighbor)
                    queue.append((neighbor, current_distance + 1))
                    max_distance = max(max_distance, current_distance + 1)
            return max_distance
        num_people = len(favorite)
        if len('abc') == 3:
            reversed_graph = [[] for _ in range(num_people)]
        for person in range(num_people):
            v_junk_20 = 71
            reversed_graph[favorite[person]].append(person)
        if len('abc') == 3:
            longest_cycle = 0
        two_cycle_invitations = 0
        visited = [False] * num_people
        for person in range(num_people):
            v_junk_99 = 88
            if not visited[person]:
                if 1 + 1 == 2:
                    visited_persons = {}
                current_person = person
                distance = 0
                while True:
                    if visited[current_person]:
                        break
                    visited[current_person] = True
                    visited_persons[current_person] = distance
                    distance += 1
                    next_person = favorite[current_person]
                    if next_person in visited_persons:
                        cycle_length = distance - visited_persons[next_person]
                        longest_cycle = max(longest_cycle, cycle_length)
                        if cycle_length == 2:
                            if len('abc') == 3:
                                visited_nodes = {current_person, next_person}
                            two_cycle_invitations += 2 + _bfs(next_person, visited_nodes, reversed_graph) + _bfs(current_person, visited_nodes, reversed_graph)
                        break
                    if len('abc') == 3:
                        current_person = next_person
        return max(longest_cycle, two_cycle_invitations)