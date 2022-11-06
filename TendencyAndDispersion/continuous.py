import TendencyAndDispersion.base as base


class ContinuousData(base.Quantitative):
    def __init__(self, data: list, unit: str = "units") -> None:
        self.table: dict = {}
        self.sigma_table: list = []
        self.space: int = 15
        self.avg_gap: float = 0
        super().__init__(data, unit)

    def get_mean(self) -> str:
        self.mean = round(self.sigma_table[6] / self.sigma_table[4], 2)
        return f"""Mean
bar x = sigma(fx) / sigma(f)
      = {self.sigma_table[6]} / {self.sigma_table[4]}
      = {self.mean} {self.unit}
        """

    def get_median(self) -> str:
        n = self.sigma_table[4]
        middle = n / 2
        index = -1
        number = 0
        for i in range(len(self.table["cf"])):
            if self.table["cf"][i] >= middle:
                index = i
                number = self.table["cf"][i]
                break
        l = self.table["lcb"][index]
        c = self.table["ucb"][index] - self.table["lcb"][index]
        f = self.table["f"][index]
        fl = self.table["cf"][index - 1] if index > 0 else 0
        self.median = round(l + ((middle - fl) / f) * c, 2)
        return f"""Median
N = sigma(f) = {n}
N / 2 = {n} / 2 = {middle}
1st c.f >= {middle} is {number}
Median class is '{self.table["classes"][index]}'
L = {self.table["lcb"][index] + self.avg_gap} - {self.avg_gap} = {l}
c = {self.table["ucb"][index]} - {self.table["lcb"][index]} = {c}
f = {f}
fl = {fl}
Median = L + ((N / 2 - fl) / f) * c
       = {l} + (({middle} - {fl}) / {f}) * {c}
       = {self.median} {self.unit}
    """

    def get_mode(self) -> str:
        highest_frequency: int = max(self.table["f"])
        self.mode: list = []
        index: list = []
        mode_classes: list = []
        for i in range(len(self.table["f"])):
            if self.table["f"][i] == highest_frequency:
                index.append(i)
                mode_classes.append(self.table["classes"][i])

        sentence: str = f"Mode\n"
        for i in range(len(index)):
            l = self.table["lcb"][index[i]]
            c = self.table["ucb"][index[i]] - self.table["lcb"][index[i]]
            d1 = self.table["f"][index[i]] - self.table["f"][index[i] - 1]
            d2 = self.table["f"][index[i]] - self.table["f"][index[i] + 1]
            self.mode.append(round(l + (d1 / (d1 + d2)) * c, 2))
            sentence += f"""Highest freq is {highest_frequency}
Modal class is '{mode_classes[i]}'
L = {self.table["lcb"][index[i]] + self.avg_gap} - {self.avg_gap} = {l}
c = {self.table["ucb"][index[i]]} - {self.table["lcb"][index[i]]} = {c}
d1 = {self.table["f"][index[i]]} - {self.table["f"][index[i] - 1]} = {d1}
d2 = {self.table["f"][index[i]]} - {self.table["f"][index[i] + 1]} = {d2}
Mode = L + (d1 / (d1 + d2)) * c 
     = {l} + ({d1} / ({d1} + {d2})) * {c}
     = {self.mode[i]} {self.unit}
"""
            return sentence

    def get_range(self) -> str:
        self.range = round(self.table["ucb"][-1] - self.table["lcb"][0], 7)
        return f"""Range
range = {self.table["ucb"][-1]} - {self.table["lcb"][0]} = {self.range} {self.unit}
        """

    def get_variance(self) -> str:
        self.variance = round(
            (self.sigma_table[7] - ((self.sigma_table[6] ** 2) / self.sigma_table[4])) / (self.sigma_table[4] - 1), 2)
        return f"""Variance
s^2 = (sigma(f * x ^ 2) - ((sigma(f * x) ^ 2) / sigma(f)) / (sigma(f) - 1)
    = ({self.sigma_table[7]} - (({self.sigma_table[6]} ^ 2) / {self.sigma_table[4]})) / ({self.sigma_table[4]} - 1)
    = {self.variance} {self.unit} ^ 2
        """

    def get_standard_deviation(self) -> str:
        self.standard_deviation = round(self.variance ** 0.5, 2)
        return f"""Standard Deviation
s = {self.standard_deviation} {self.unit}
        """

    def draw_tabel(self) -> str:
        lcl = self.data[0]
        ucl = self.data[1]
        lcb: list = []
        ucb: list = []
        classes: list = []
        mid_points: list = []
        f: list = self.data[2]
        cf: list = []
        fx: list = []
        fxx: list = []
        count: int = 0
        self.avg_gap = round((lcl[1] - ucl[0]) / 2, 7)
        for i in range(len(f)):
            lcb.append(round(lcl[i] - self.avg_gap, 7))
            classes.append(f"{lcl[i]} - {ucl[i]}")
            ucb.append(round(ucl[i] + self.avg_gap, 7))
            mid_points.append(round((lcl[i] + ucl[i]) / 2, 7))
            fx.append(round(f[i] * mid_points[i], 7))
            count += f[i]
            cf.append(count)
            fxx.append(round(f[i] * (mid_points[i] ** 2), 7))
        self.table["lcb"] = lcb
        self.table["classes"] = classes
        self.table["ucb"] = ucb
        self.table["mid_points"] = mid_points
        self.table["f"] = f
        self.table["cf"] = cf
        self.table["fx"] = fx
        self.table["fxx"] = fxx
        self.sigma_table = ["sigma", "", "", "", sum(f), "", sum(fx), sum(fxx)]
        sentence: str = "continuous table\n"
        sentence += f"{'l.c.b':<{self.space}}{'class':<{self.space}}{'u.c.b':<{self.space}}{'mid-point(x)':{self.space}}{'f':{self.space}}{'cf':{self.space}}{'fx':{self.space}}{'fx^2':{self.space}}\n"
        for i in range(len(classes)):
            sentence += f"{lcb[i]:<{self.space}}{classes[i]:<{self.space}}{ucb[i]:<{self.space}}{mid_points[i]:<{self.space}}{f[i]:<{self.space}}{cf[i]:<{self.space}}{fx[i]:<{self.space}}{fxx[i]:<{self.space}}\n"
        for i in range(len(self.sigma_table)):
            sentence += f"{self.sigma_table[i]:<{self.space}}"
        sentence += "\n"
        return sentence
