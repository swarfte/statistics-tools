import os
import sys
import csv
import TendencyAndDispersion.raw as raw


def run(path: str) -> None:
    data = []
    print(path + "\n")
    with open(path, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            for n in row:
                if n != "":
                    data.append(float(n))
    raw_data = raw.RawData(data)
    raw_data.show()


if __name__ == "__main__":
    run(sys.argv[1])
    os.system("pause")
