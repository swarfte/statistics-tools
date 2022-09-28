import TendencyAndDispersion.base as base


class RawData(base.Quantitative):
    def __init__(self, data: list, unit: str = "units") -> None:
        self.sort_data: list = sorted(data)
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
        return f"""Range
        """

    def get_variance(self) -> str:
        return f"""Variance
        """

    def get_standard_deviation(self) -> str:
        return f"""Standard Deviation
        """

    def draw_tabel(self) -> str:
        return f"sorted data : {self.sort_data}"
