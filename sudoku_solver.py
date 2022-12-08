import copy
class SudokuSolver:
    def __init__(self, entry_data):
        self.data = entry_data
        self.data_backup = None
        self.guessed = []
        self.guessed_checked = []

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
        num_filled = 0
        all_zero = True
        print('**********START*********')
        for entry in self.data:
            print(len(entry['possible_num']))
            if len(entry['possible_num']) == 1:
                entry['value'] = entry['possible_num'][0]
                num_filled += 1
            if len(entry['possible_num']) != 0:
                all_zero = True
            else:
                all_zero = False

        # if all_zero and self.missing_values():
        #     self.data = self.data_backup
        #     self.guessed = []


        # if there is no field that has only one option
        if num_filled == 0 and self.missing_values():
            print(f"GUESSED: {self.guessed}")
            for guessed in self.guessed:
                temp = self.data[guessed]['value']
                self.data[guessed]['possible_num'].append(temp)
                self.data[guessed]['value'] = None
            for index in range(0, 81):
                if len(self.data[index]['possible_num']) == 2 and index not in self.guessed:
                    if len(self.guessed_checked) == 0:
                        self.guessed_checked.append(index)
                    self.guessed.append(index)
                    self.data_backup = copy.deepcopy(self.data)
                    self.data[index]['value'] = self.data[index]['possible_num'][0]
                    break

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


