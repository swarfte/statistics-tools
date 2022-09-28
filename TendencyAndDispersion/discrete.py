import TendencyAndDispersion.base as base


class DiscreteData(base.Quantitative):
    def __init__(self, data: list, unit: str = "units") -> None:
        self.table: dict = {}
        self.sigma_table: list = []
        self.space: int = 15
        super().__init__(data, unit)

    def draw_tabel(self) -> str:
        class_x: list = self.data[0]
        f: list = self.data[1]
        cf: list = []
        fx: list = []
        count: int = 0
        for i in range(len(class_x)):
            count += f[i]
            cf.append(count)
            fx.append(class_x[i] * f[i])
        self.table["class_x"] = class_x
        self.table["f"] = f
        self.table["cf"] = cf
        self.table["fx"] = fx
        self.sigma_table = ["sigma", sum(f), "", sum(fx)]
        sentence: str = "discrete table\n"
        sentence += f"{'class(x)':<{self.space}}{'f':<{self.space}}{'cf':<{self.space}}{'fx':<{self.space}}"
        for i in range(len(class_x)):
            sentence += f"\n{class_x[i]:<{self.space}}{f[i]:<{self.space}}{cf[i]:<{self.space}}{fx[i]:<{self.space}}"
        sentence += f"\n{self.sigma_table[0]:<{self.space}}{self.sigma_table[1]:<{self.space}}{self.sigma_table[2]:<{self.space}}{self.sigma_table[3]:<{self.space}}\n"
        return sentence

    def get_mean(self) -> str:
        self.mean = round(self.sigma_table[3] / self.sigma_table[1], 2)
        return f"""Mean
bar x = sigma(fx) / sigma(f)
      = {self.sigma_table[3]} / {self.sigma_table[1]}
      = {self.mean} {self.unit}
                """

    def get_median(self) -> str:
        n = self.sigma_table[1]
        middle = (n + 1) / 2
        index = -1
        number = 0
        for i in range(len(self.table["cf"])):
            if self.table["cf"][i] >= middle:
                index = i
                number = self.table["cf"][i]
                break
        self.median = self.table["class_x"][index]
        return f"""Median
N = sigma(f) = {n}
(N + 1) / 2 = ({n} + 1) / 2 = {middle}
1.st c.f >= {middle} is {number}
Median = {self.median} {self.unit}
                """

    def get_mode(self) -> str:
        highest_frequency: int = max(self.table["f"])
        self.mode: list = []
        for i in range(len(self.table["f"])):
            if self.table["f"][i] == highest_frequency:
                self.mode.append(self.table["class_x"][i])
        if len(self.mode) == len(self.table["class_x"]):
            return f"""Mode
No mode
            """
        else:
            return f"""Mode
Highest frequency = {highest_frequency}
mode = {self.mode} {self.unit}
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
