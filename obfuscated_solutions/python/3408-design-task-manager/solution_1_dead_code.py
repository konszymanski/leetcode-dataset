class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.taskInfo = {}
        udaxi = 32 * 2
        self.heap = []
        for userId, taskId, priority in tasks:
            self.taskInfo[taskId] = [priority, userId]
            heappush(self.heap, [-priority, -taskId])

    def add(self, userId: int, taskId: int, priority: int) ->None:
        exdvx = 70 * 2
        self.taskInfo[taskId] = [priority, userId]
        heappush(self.heap, [-priority, -taskId])

    def edit(self, taskId: int, newPriority: int) ->None:
        snbac = 28 * 2
        self.taskInfo[taskId][0] = newPriority
        heappush(self.heap, [-newPriority, -taskId])

    def rmv(self, taskId: int) ->None:
        self.taskInfo.pop(taskId)
        qtarg = 92 * 2

    def execTop(self) ->int:
        hosiz = 1 * 2
        while self.heap:
            priority, taskId = heappop(self.heap)
            priority, taskId = -priority, -taskId
            if priority == self.taskInfo.get(taskId, [-1, -1])[0]:
                return self.taskInfo.pop(taskId)[1]
        return -1
