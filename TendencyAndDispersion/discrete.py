import TendencyAndDispersion.base as base


class DiscreteData(base.Quantitative):
    def __init__(self, data: list, unit: str = "units") -> None:
        super().__init__(data, unit)

    def get_mean(self) -> str:
        pass

    def get_median(self) -> str:
        pass

    def get_mode(self) -> str:
        pass

    def get_range(self) -> str:
        pass

    def get_variance(self) -> str:
        pass

    def get_standard_deviation(self) -> str:
        pass
