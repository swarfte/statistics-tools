import abc


class Quantitative(metaclass=abc.ABCMeta):
    def __init__(self, data: list, unit: str = "units") -> None:
        self.data: list = data
        self.unit: str = unit
        self.mean: float = 0
        self.median: float = 0
        self.mode: float = 0
        self.range: float = 0
        self.variance: float = 0
        self.standard_deviation: float = 0

    @abc.abstractmethod
    def get_mean(self) -> str:
        pass

    @abc.abstractmethod
    def get_median(self) -> str:
        pass

    @abc.abstractmethod
    def get_mode(self) -> str:
        pass

    @abc.abstractmethod
    def get_range(self) -> str:
        pass

    @abc.abstractmethod
    def get_variance(self) -> str:
        pass

    @abc.abstractmethod
    def get_standard_deviation(self) -> str:
        pass

    @abc.abstractmethod
    def draw_tabel(self) -> str:
        pass

    def run(self) -> None:
        self.draw_tabel()
        self.get_mean()
        self.get_median()
        self.get_mode()
        self.get_range()
        self.get_variance()
        self.get_standard_deviation()

    def show(self) -> None:
        print(self.draw_tabel())
        print(self.get_mean())
        print(self.get_median())
        print(self.get_mode())
        print(self.get_range())
        print(self.get_variance())
        print(self.get_standard_deviation())
