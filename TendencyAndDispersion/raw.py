import TendencyAndDispersion.base as base


class RawData(base.Quantitative):
    def __init__(self, data: list, unit: str = "units") -> None:
        self.sort_data: list = sorted(data)
        self.square_data: list = list((round(i ** 2, 7) for i in self.sort_data))
        self.space: int = 10
        super().__init__(data)

    def get_mean(self) -> str:
        numbers: float = sum(self.data)
        numbers_len: int = len(self.data)
        self.mean: float = round(numbers / numbers_len, 2)
        return f"""Mean
bar x = sigma(x) / n
      = {numbers} / {numbers_len}
      = {self.mean} {self.unit}
                """

    def get_median(self) -> str:
        data_size: int = len(self.sort_data)
        index: int = (data_size + 1) // 2
        if data_size % 2 == 1:
            self.median: float = self.sort_data[index - 1]
            return f"""Median
middle = (n + 1) / 2
       = ({data_size} + 1) / 2
       = {index} {"st" if index == 1 else "nd" if index == 2 else "rd" if index == 3 else "th"} 
median = {self.median} {self.unit}
                    """
        else:
            self.median: float = round((self.sort_data[index - 1] + self.sort_data[index]) / 2, 2)
            return f"""Median
middle = (n + 1) / 2
       = ({data_size} + 1) / 2
       = {(data_size + 1) / 2} {"st" if index == 1 else "nd" if index == 2 else "rd" if index == 3 else "th"} 
median = ({self.sort_data[index - 1]} + {self.sort_data[index]}) / 2
       = {self.median} {self.unit}
                    """

    def get_mode(self) -> str:
        count_dict: dict = {}
        for i in self.sort_data:
            if str(i) in count_dict:
                count_dict[str(i)] += 1
            else:
                count_dict[str(i)] = 1
        max_count: int = max(count_dict.values())
        self.mode: list = [float(i) for i in count_dict if count_dict[str(i)] == max_count]
        is_mode: bool = False if len(self.mode) == len(self.sort_data) else True
        if is_mode:
            return f"""Mode
Mode = {self.mode} {self.unit}
                    """
        else:
            return f"""Mode
No mode
                    """

    def get_range(self) -> str:
        self.range: float = self.sort_data[-1] - self.sort_data[0]
        return f"""Range
R = {self.sort_data[-1]} - {self.sort_data[0]} = {self.range} {self.unit}
        """

    def get_variance(self) -> str:
        numbers: float = sum(self.data)
        numbers_len: int = len(self.data)
        self.variance = round((sum(self.square_data) - (len(self.square_data) * (numbers / numbers_len) ** 2)) / (numbers_len - 1),2)
        return f"""Variance
s^2 = (sigma(x^2) - (n * (sigma(x) / n)^2) )/ (n - 1)
    = ({round(sum(self.square_data), 7)} - ({len(self.square_data)} * ({round(numbers, 7)} / {numbers_len})^2) )/ ({numbers_len} - 1)
    = {round(self.variance, 2)} {self.unit}^2
        """

    def get_standard_deviation(self) -> str:
        self.standard_deviation: float = round(self.variance ** 0.5, 2)
        return f"""Standard Deviation
s = {self.standard_deviation} {self.unit}
        """

    def draw_tabel(self) -> str:
        sentence = f"      {'x':<{self.space}}{'x^2':<{self.space}}\n"
        for i in range(len(self.sort_data)):
            sentence += f"      {self.sort_data[i]:<{self.space}}{self.square_data[i]:<{self.space}}\n"
        sentence += f"sigma {round(sum(self.sort_data), 7):<{self.space}}{round(sum(self.square_data), 7):<{self.space}}\n"
        return f"sorted data : {self.sort_data} \n {sentence}"
