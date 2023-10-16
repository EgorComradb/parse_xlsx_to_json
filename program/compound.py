import helper

##################################################################################################
# можно менять местами вложенность в зависимости от того что нам нужно получить из итогового JSON
# 1. {'Помидор': {'красный': {'Общие': {'Вода, г': None, 'Энергия, кКал': None, 'Белки, г': None....}}}}
# 2. {'Общие': {'Вода, г': {'Помидор': {'красный': None, 'оранжевый': None, 'жёлтый': None....}}}}
##################################################################################################

class Compound:

    def __init__(self, f_dict, sec_dict, data):
        self.f_dict = f_dict
        self.sec_dict = sec_dict
        self.scenario = True if "Общие" in self.f_dict.keys() else False
        self.data = data
        self.help = helper.Helper(self.data)
        self.new_dict = {}
        self.keys = []


    def compress(self):
        if self.scenario:
            self.help.data_refactor_row(0, [])
        else:
            self.help.data_refactor_column([])

        self.data = self.help.data

        for k, v in self.f_dict.items():
            for kk, vv in v.items():
                self.f_dict[k][kk] = self.sec_dict

        start = 0
        for r, v in self.f_dict.items():
            for rr, vv in v.items():
                for rrr, vvv in vv.items():
                    for rrrr, vvvv in vvv.items():
                        self.keys.append([r,rr,rrr,rrrr, self.data[start]])
                        start += 1

        for i in self.keys:
            self.new_dict.update({i[0]: {}})
        for i in self.keys:
            self.new_dict[i[0]].update({i[1]: {}})
        for i in self.keys:
            self.new_dict[i[0]][i[1]].update({i[2]: {}})
        for i in self.keys:
            self.new_dict[i[0]][i[1]][i[2]].update({i[3]: {}})
        for i in self.keys:
            self.new_dict[i[0]][i[1]][i[2]][i[3]] = i[4]

        return self.new_dict