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
        print(possible_num)

    def check_column(self, column):
        existing_num = []
        for entry in self.data:
            if entry['col'] == column:
                if entry['value'] is not None:
                    existing_num.append(entry['value'])
        for entry in self.data:
            if entry['col'] == column:
                if entry['value'] is None:
                    for num in existing_num:
                        if num in entry['possible_num']:
                            entry['possible_num'].remove(num)
                print(entry)
        print(existing_num)

    def check_row(self, row):
        existing_num = []
        for entry in self.data:
            if entry['row'] == row:
                if entry['value'] is not None:
                    existing_num.append(entry['value'])
        for entry in self.data:
            if entry['row'] == row:
                if entry['value'] is None:
                    for num in existing_num:
                        if num in entry['possible_num']:
                            entry['possible_num'].remove(num)
            print(entry)
        print(existing_num)

    def solve(self):
        self.check_quadrant(1)
        self.check_column(1)
        #self.check_row(1)