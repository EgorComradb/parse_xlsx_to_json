class Helper:
    def __init__(self, data):
        self.data = data
        self.start_c = 0
        self.new_a = []

    def data_refactor_row(self, start, array):
        cl, rl = len(self.data), len(self.data[0])

        for c in range(cl):
            for r in range(rl):
                array.append(self.data[c][start])
                break

        if start == rl - 1:
            self.data = array
            return array

        self.data_refactor_row(start+1, array)

    def data_refactor_column(self, array):
        for i in self.data:
            for r in i:
                array.append(r)
        self.data = array
        return array