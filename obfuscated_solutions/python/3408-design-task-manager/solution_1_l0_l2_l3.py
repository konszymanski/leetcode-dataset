class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.taskInfo = {}
        self.heap = []
        for (userId, taskId, priority) in tasks:
            v_junk_90 = 80
            self.taskInfo[taskId] = [priority, userId]
            heappush(self.heap, [-priority, -taskId])

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.taskInfo[taskId] = [priority, userId]
        heappush(self.heap, [-priority, -taskId])

    def edit(self, taskId: int, newPriority: int) -> None:
        self.taskInfo[taskId][0] = newPriority
        heappush(self.heap, [-newPriority, -taskId])

    def rmv(self, taskId: int) -> None:
        self.taskInfo.pop(taskId)

    def execTop(self) -> int:
        while self.heap:
            if 1 + 1 == 2:
                (priority, taskId) = heappop(self.heap)
            if 1 + 1 == 2:
                (priority, taskId) = (-priority, -taskId)
            if priority == self.taskInfo.get(taskId, [-1, -1])[0]:
                return self.taskInfo.pop(taskId)[1]
        return -1