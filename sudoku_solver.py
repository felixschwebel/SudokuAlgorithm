class SudokuSolver:
    def __init__(self, entry_data):
        self.data = entry_data

    def check_fields(self):
        for index in range(0, 81):
            things_to_check = ['quadrant', 'col', 'row']
            for thing in things_to_check:
                for entry in self.data:
                    if entry[thing] == self.data[index][thing]:
                        if entry['value'] is not None:
                            try:
                                self.data[index]['possible_num'].remove(entry['value'])
                            except ValueError:
                                pass

    def fill_values(self):
        for entry in self.data:
            if len(entry['possible_num']) == 1:
                entry['value'] = entry['possible_num'][0]

    def missing_values(self):
        for entry in self.data:
            if entry['value'] is None:
                return True
        return False

    def solve(self):
        missing_values = True
        while missing_values:
            self.check_fields()
            self.fill_values()
            missing_values = self.missing_values()
        return self.data


