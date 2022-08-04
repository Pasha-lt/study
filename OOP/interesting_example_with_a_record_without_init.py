class StreamData:
    def create(self, fields, lst_values):
        # self.__dict__ = dict(zip(fields, lst_values)) # can do it like this or like bellow(2 strings)
        for number, key in enumerate(fields):
            setattr(self, key, lst_values[number])
        return True


class StreamReader:
    FIELDS = ("ключ_1", "ключ_2", "ключ_3")

    def readlines(self):
        lst_in = ["значення_1", "значення_2", "значення_3"]
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res


sr = StreamReader()
data, result = sr.readlines()
