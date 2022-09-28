import os
import sys
import csv
import TendencyAndDispersion.continuous as continuous


def run(path: str) -> None:
    data: list = []
    print(path + "\n")
    with open(path, "r") as f:
        reader = list(csv.reader(f))
        size: int = len(reader)
        if size == 3:
            data = horizontal_mode(reader)
        else:
            data = vertical_mode(reader)
    continuous_data = continuous.ContinuousData(data)
    continuous_data.show()


def horizontal_mode(reader) -> list:
    lcl = [float(x) for x in reader[0]]
    ucl = [float(x) for x in reader[1]]
    f = [int(x) for x in reader[2]]
    return [lcl, ucl, f]


def vertical_mode(reader) -> list:
    lcl = []
    ucl = []
    f = []
    for row in reader:
        lcl.append(float(row[0]))
        ucl.append(float(row[1]))
        f.append(int(row[2]))
    return [lcl, ucl, f]


if __name__ == "__main__":
    run(sys.argv[1])
    os.system("pause")
