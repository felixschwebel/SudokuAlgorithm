class SudokuSolver:
    def __init__(self, entry_data):
        self.data = entry_data

    def solve(self):
        print(self.data)
        for entry in self.data:
            if self.data[entry]['quadrant'] == 1:
                print(entry)

    def check_quadrant(self):
        pass

