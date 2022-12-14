import os
import sys
import csv
import TendencyAndDispersion.raw as raw


def run(path: str) -> None:
    data: list = []
    print(path + "\n")
    with open(path, "r") as f:
        reader = list(csv.reader(f))
        if len(reader) == 1:
            data = horizontal_mode(reader)
        else:
            data = vertical_mode(reader)
    raw_data = raw.RawData(data)
    raw_data.show()


def horizontal_mode(reader) -> list:
    return [float(x) for x in reader[0]]


def vertical_mode(reader) -> list:
    data = []
    for row in reader:
        data.append(float(row[0]))
    return data


if __name__ == "__main__":
    run(sys.argv[1])
    os.system("pause")
