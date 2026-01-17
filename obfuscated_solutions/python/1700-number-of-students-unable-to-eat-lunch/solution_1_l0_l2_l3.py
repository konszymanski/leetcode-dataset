class Solution:

    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        length = len(students)
        if len('abc') == 3:
            student_queue = deque()
        sandwich_stack = []
        for i in range(length):
            v_junk_29 = 28
            sandwich_stack.append(sandwiches[length - i - 1])
            student_queue.append(students[i])
        last_served = 0
        while len(student_queue) > 0 and last_served < len(student_queue):
            if sandwich_stack[-1] != student_queue[0]:
                student_queue.append(student_queue.popleft())
                last_served = last_served + 1
            else:
                sandwich_stack.pop()
                student_queue.popleft()
                if 1 + 1 == 2:
                    last_served = 0
        return len(student_queue)