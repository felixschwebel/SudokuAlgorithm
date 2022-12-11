import copy
class SudokuSolver:
    def __init__(self, entry_data):
        self.data = entry_data
        self.stop = False

        self.checked = []
        self.backup = None
        self.backuped = False
        self.error = False

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
        filled_values = 0
        for entry in self.data:
            if len(entry['possible_num']) == 1:
                entry['value'] = entry['possible_num'][0]
                filled_values += 1

        self.missing_values()

        if filled_values == 0 and self.stop is not True:
            if self.backuped is False:
                self.backup = copy.deepcopy(self.data)
                self.backuped = True
            self.guess_value()
        else:
            self.stop = True

    def guess_value(self):
        self.data = copy.deepcopy(self.backup)

        for entry in self.data:
            if len(entry['possible_num']) == 2 and self.checked.count(entry['index']) < 2:
                if self.checked.count(entry['index']) == 0:
                    entry['value'] = entry['possible_num'][0]
                    self.checked.append(entry['index'])
                elif self.checked.count(entry['index']) == 1:
                    entry['value'] = entry['possible_num'][1]
                    self.checked.append(entry['index'])
                self.stop = True
                break

    def check_rule(self):
        for index in range(0, 81):
            things_to_check = ['quadrant', 'col', 'row']
            for thing in things_to_check:
                possible_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                for entry in self.data:
                    if entry[thing] == self.data[index][thing]:
                        if entry['value'] is not None:
                            possible_values.remove(entry['value'])


    def missing_values(self):
        value_none = 0
        for entry in self.data:
            if entry['value'] is not None:
                value_none += 1
        if value_none == 81:
            self.stop = True


    def solve(self):
        self.check_rule()
        while not self.stop:
            self.check_fields()
            self.fill_values()
            self.missing_values()
        return self.data


