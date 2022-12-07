class SudokuSolver:
    def __init__(self, entry_data):
        self.data = entry_data

    def check_quadrant(self, quadrant):
        possible_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for entry in self.data:
            if entry['quadrant'] == quadrant:
                if entry['value'] is not None:
                    possible_num.remove(entry['value'])
        for entry in self.data:
            if entry['quadrant'] == quadrant:
                if entry['value'] is None:
                    entry['possible_num'] = possible_num

    def solve(self):
        #print(self.data)
        self.check_quadrant(1)