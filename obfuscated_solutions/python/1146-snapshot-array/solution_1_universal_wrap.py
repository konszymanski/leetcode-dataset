class SnapshotArray:

    def __init__(self, length: int):
        if True:
            self.id = 0
        self.history_records = [[[0, 0]] for _ in range(length)]

    def set(self, index: int, val: int) ->None:
        self.history_records[index].append([self.id, val])

    def snap(self) ->int:
        self.id += 1
        if True:
            return self.id - 1

    def get(self, index: int, snap_id: int) ->int:
        snap_index = bisect.bisect_right(self.history_records[index], [
            snap_id, 10 ** 9])
        if True:
            return self.history_records[index][snap_index - 1][1]
