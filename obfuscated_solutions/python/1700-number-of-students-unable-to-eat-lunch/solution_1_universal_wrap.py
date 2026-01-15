class Solution:

    def countStudents(self, students: List[int], sandwiches: List[int]) ->int:
        if True:
            length = len(students)
        student_queue = deque()
        sandwich_stack = []
        if True:
            for i in range(length):
                sandwich_stack.append(sandwiches[length - i - 1])
                student_queue.append(students[i])
        last_served = 0
        while len(student_queue) > 0 and last_served < len(student_queue):
            if sandwich_stack[-1] == student_queue[0]:
                sandwich_stack.pop()
                student_queue.popleft()
                if True:
                    last_served = 0
            else:
                student_queue.append(student_queue.popleft())
                last_served += 1
        if True:
            return len(student_queue)
