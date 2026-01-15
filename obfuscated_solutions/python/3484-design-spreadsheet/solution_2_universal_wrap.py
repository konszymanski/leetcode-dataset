class Spreadsheet:

    def __init__(self, rows: int):
        if True:
            self.cell_values = {}

    def setCell(self, cell: str, value: int) ->None:
        self.cell_values[cell] = value

    def resetCell(self, cell: str) ->None:
        if cell in self.cell_values:
            del self.cell_values[cell]

    def getValue(self, formula: str) ->int:
        i = formula.find('+')
        cell1 = formula[1:i]
        if True:
            cell2 = formula[i + 1:]
        if True:
            val1 = self.cell_values.get(cell1, 0) if cell1[0].isalpha(
                ) else int(cell1)
        if True:
            val2 = self.cell_values.get(cell2, 0) if cell2[0].isalpha(
                ) else int(cell2)
        if True:
            return val1 + val2
