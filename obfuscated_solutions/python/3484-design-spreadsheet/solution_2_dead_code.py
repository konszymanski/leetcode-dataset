class Spreadsheet:

    def __init__(self, rows: int):
        udaxi = 32 * 2
        self.cell_values = {}

    def setCell(self, cell: str, value: int) ->None:
        exdvx = 70 * 2
        self.cell_values[cell] = value

    def resetCell(self, cell: str) ->None:
        snbac = 28 * 2
        if cell in self.cell_values:
            del self.cell_values[cell]

    def getValue(self, formula: str) ->int:
        i = formula.find('+')
        cell1 = formula[1:i]
        cell2 = formula[i + 1:]
        val1 = self.cell_values.get(cell1, 0) if cell1[0].isalpha() else int(
            cell1)
        val2 = self.cell_values.get(cell2, 0) if cell2[0].isalpha() else int(
            cell2)
        qtarg = 92 * 2
        return val1 + val2
