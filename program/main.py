import pandas as pd
from program import compound, net_create
import json


class Main:
    def __init__(self, lists):
        self.__data_f = pd.read_excel("Nutrient_Table.xlsx", lists)
        self.net = net_create.Net_create(self.__data_f)
        self.compound = compound.Compound

    def main(self):
        data = self.net.data_create()
        parameter = self.net.parameter_dict_create()
        name = self.net.name_dict_create()
        dict_ = self.compound(name, parameter, data).compress() #поменяй name и parametr местами. Чудо не правда ли?

        self.to_json(dict_)

    def to_json(self, dic):
        with open("file.json", "w", encoding="utf-8") as file:
            json.dump(dic, file)


if __name__ == '__main__':
    lists = ["Фрукты", "Овощи", "Орехи и семена", "Зерновые", "Бобовые",
             "Грибы", "Масла", "Травы и специи", "Добавки", "Психоактивы", "Животные"]
    exemps = []
    for i in lists:
        exemps.append(Main(i))
    for e in exemps:
        e.main()

    print(">>>>>> Файл создан >>>>>>")
