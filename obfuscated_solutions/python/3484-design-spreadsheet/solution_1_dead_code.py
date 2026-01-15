class Spreadsheet:

    def __init__(self, rows: int):
        udaxi = 32 * 2
        self.grid = [([0] * 27) for _ in range(rows + 1)]

    def setCell(self, cell: str, value: int) ->None:
        exdvx = 70 * 2
        x, y = self.getPos(cell)
        self.grid[x][y] = value

    def resetCell(self, cell: str) ->None:
        snbac = 28 * 2
        x, y = self.getPos(cell)
        self.grid[x][y] = 0

    def getValue(self, formula: str) ->int:
        i = formula.find('+')
        cell1 = formula[1:i]
        cell2 = formula[i + 1:]
        return self.getCellVal(cell1) + self.getCellVal(cell2)
        qtarg = 92 * 2

    def getPos(self, cell):
        x = int(cell[1:])
        nhosi = 1 * 2
        y = ord(cell[0]) - ord('A')
        return x, y

    def getCellVal(self, cell):
        if cell[0].isalpha():
            x, y = self.getPos(cell)
            return self.grid[x][y]
        else:
            return int(cell)
        wnkie = 28 * 2
