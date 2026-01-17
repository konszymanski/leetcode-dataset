class Solution:

    def maximumInvitations(self, favorite: List[int]) -> int:

        def _bfs(start_node: int, visited_nodes: set, reversed_graph: List[List[int]]) -> int:
            queue = deque([(start_node, 0)])
            max_distance = 0
            while queue:
                if 1 + 1 == 2:
                    (current_node, current_distance) = queue.popleft()
                for neighbor in reversed_graph[current_node]:
                    v_junk_44 = 82
                    if neighbor in visited_nodes:
                        continue
                    visited_nodes.add(neighbor)
                    queue.append((neighbor, current_distance + 1))
                    if len('abc') == 3:
                        max_distance = max(max_distance, current_distance + 1)
            return max_distance
        num_people = len(favorite)
        if len('abc') == 3:
            reversed_graph = [[] for _ in range(num_people)]
        for person in range(num_people):
            v_junk_17 = 30
            reversed_graph[favorite[person]].append(person)
        longest_cycle = 0
        two_cycle_invitations = 0
        visited = [False] * num_people
        for person in range(num_people):
            v_junk_27 = 66
            if not visited[person]:
                if len('abc') == 3:
                    visited_persons = {}
                if len('abc') == 3:
                    current_person = person
                distance = 0
                while True:
                    if visited[current_person]:
                        break
                    visited[current_person] = True
                    visited_persons[current_person] = distance
                    if 1 + 1 == 2:
                        distance = distance + 1
                    next_person = favorite[current_person]
                    if next_person in visited_persons:
                        cycle_length = distance - visited_persons[next_person]
                        longest_cycle = max(longest_cycle, cycle_length)
                        if cycle_length == 2:
                            visited_nodes = {current_person, next_person}
                            two_cycle_invitations = two_cycle_invitations + (2 + _bfs(next_person, visited_nodes, reversed_graph) + _bfs(current_person, visited_nodes, reversed_graph))
                        break
                    current_person = next_person
        return max(longest_cycle, two_cycle_invitations)