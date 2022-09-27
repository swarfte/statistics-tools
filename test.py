import TendencyAndDispersion.raw as raw
import TendencyAndDispersion.discrete as discrete
import TendencyAndDispersion.continuous as continuous


def test_raw():
    raw_data = [
        3.25, 5.18, 6.33, 1.87, 5.82, 3.44,
        2.54, 6.92, 4.22, 3.39, 1.75, 5.95
    ]
    raw_example = raw.RawData(raw_data)
    raw_example.show()


def test_discrete():
    pass


def test_continuous():
    pass


def run() -> None:
    test_raw()


if __name__ == "__main__":
    run()
