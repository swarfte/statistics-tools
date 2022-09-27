import TendencyAndDispersion.base as base


class RawData(base.Quantitative):
    def __init__(self, data: list, unit: str = "units") -> None:
        self.sort_data: list = sorted(data)
        super().__init__(data)

    def get_mean(self) -> str:
        numbers = sum(self.data)
        numbers_len = len(self.data)
        self.mean = round(numbers / numbers_len, 2)
        return f"""Mean
bar x = sigma(x) / n
      = {numbers} / {numbers_len}
      = {self.mean} {self.unit}
                """

    def get_median(self) -> str:
        data_size = len(self.sort_data)
        index = (data_size + 1) // 2
        if data_size % 2 == 1:
            self.median = self.sort_data[index - 1]
            return f"""Median
sorted data : {self.sort_data}
middle = (n + 1) / 2
       = ({data_size} + 1) / 2
       = {index} {"st" if index == 1 else "nd" if index == 2 else "rd" if index == 3 else "th"} 
median = {self.median} {self.unit}
                    """
        else:
            self.median = (self.sort_data[index - 1] + self.sort_data[index]) / 2
            return f"""Median
sorted data : {self.sort_data}
middle = (n + 1) / 2
       = ({data_size} + 1) / 2
       = {(data_size + 1) / 2} {"st" if index == 1 else "nd" if index == 2 else "rd" if index == 3 else "th"} 
median = ({self.sort_data[index - 1]} + {self.sort_data[index]}) / 2
       = {self.median} {self.unit}
                    """

    def get_mode(self) -> str:
        count_dict = {}
        for i in self.sort_data:
            if str(i) in count_dict:
                count_dict[str(i)] += 1
            else:
                count_dict[str(i)] = 1
        max_count = max(count_dict.values())
        self.mode = [float(i) for i in count_dict if count_dict[str(i)] == max_count]
        is_mode = False if len(self.mode) == len(self.sort_data) else True
        if is_mode:
            return f"""Mode
Mode = {self.mode} {self.unit}
                    """
        else:
            return f"""Mode
No mode
                    """


    def get_range(self) -> str:
        pass

    def get_variance(self) -> str:
        pass

    def get_standard_deviation(self) -> str:
        pass
