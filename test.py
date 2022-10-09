import rawLaunch
import discreteLaunch
import continuousLaunch


def test_raw():
    rawLaunch.run("./example/raw-vertical.csv")
    # rawLaunch.run("./example/raw-horizontal.csv")


def test_discrete():
    discreteLaunch.run("./example/discrete-vertical.csv")
    # discreteLaunch.run("./example/discrete-horizontal.csv")


def test_continuous():
    continuousLaunch.run("./example/continuous-vertical.csv")
    # continuousLaunch.run("./example/continuous-horizontal.csv")


def run() -> None:
    test_raw()
    # test_discrete()
    # test_continuous()
    pass


if __name__ == "__main__":
    run()
