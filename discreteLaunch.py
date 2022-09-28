import os
import sys
import csv
import TendencyAndDispersion.discrete as discrete


def run(path: str) -> None:
    data: list = []
    print(path + "\n")
    with open(path, "r") as f:
        reader = list(csv.reader(f))
        size: int = len(reader)
        if size == 2:
            data = horizontal_mode(reader)
        else:
            data = vertical_mode(reader)
    discrete_data = discrete.DiscreteData(data)
    discrete_data.show()


def horizontal_mode(reader) -> list:
    class_x = [float(x) for x in reader[0]]
    f = [int(x) for x in reader[1]]
    return [class_x, f]


def vertical_mode(reader) -> list:
    class_x = []
    f = []
    for row in reader:
        class_x.append(float(row[0]))
        f.append(int(row[1]))
    return [class_x, f]


if __name__ == "__main__":
    run(sys.argv[1])
    os.system("pause")
