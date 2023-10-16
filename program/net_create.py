class Net_create:

    def __init__(self, data_f):
        self.__matrix_f = data_f.iloc[3:, 2:].dropna(how='all')
        self.__parameter_col = data_f.iloc[2:, 0].dropna(how='all')
        self.__name_col = data_f.iloc[0:1, 3:]

        self.__data = []

        self.__param_name = None
        self.__params = {}

        self.__product_class = None
        self.__names = {}

    def data_create(self):
        count = 0
        for _, v in self.__matrix_f.items():
            x = []
            for i in v:
                if count == len(v):
                    self.__data.append(x)
                    count = 0
                x.append(i)
                count += 1
        return self.__data

    def parameter_dict_create(self):
        for _, meaning in self.__parameter_col.items():
            if len(meaning.split()) > 6: break
            if "," in meaning:
                self.__params[self.__param_name].update({str(meaning): None})
            else:
                self.__param_name = str(meaning); self.__params[self.__param_name] = {}
        return self.__params

    def name_dict_create(self):
        for product_name, product_condition in self.__name_col.items():

            if "Unnamed" not in product_name:
                self.__product_class = str(product_name)
                self.__names[self.__product_class] = {}
            self.__names[self.__product_class].update({str(product_condition[0]): None})

        return self.__names