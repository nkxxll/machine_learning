#!/usr/bin/env python3
import argparse
import logging

import numpy as np
import pandas as pd

logging.basicConfig(level=logging.INFO)


class Point:
    """this is a point in the learning grid

    Attributes:
        x: the x coordinate
        y: the y coordinate
    """

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __eq__(self, other) -> bool:
        return True if self.x == other.x and self.y == other.y else False

    def __str__(self):
        return f"<X: {self.x}, Y: {self.y}>"


direction = [Point(-1, 0), Point(1, 0), Point(0, 1), Point(0, -1)]


def create(x, y, dtype=np.int64) -> pd.DataFrame:
    data = []
    row = [0 for _ in range(x)]
    for _ in range(y):
        data.append(row)

    return pd.DataFrame(data, dtype=dtype)


class RLGrid:
    def __init__(self, x: pd.DataFrame, fixed: Point):
        self.start_grid = x.copy(deep=True)
        self.grid = x
        self.fixed = fixed

    def update(self):
        pass

    def policy_evaluation(self):
        # grid is always quadratic simplified
        length = len(self.grid)
        new = self.grid.copy(deep=True)

        def get_min_at(y, x):
            current = Point(x, y)
            res = []
            for dir in direction:
                logging.debug(f"dir {dir.x} {dir.y}")
                if (
                    current.x + dir.x < 0
                    or current.x + dir.x >= length
                    or current.y + dir.y < 0
                    or current.y + dir.y >= length
                ):
                    continue
                else:
                    logging.debug("else")
                    res.append(self.grid[current.y + dir.y][current.x + dir.x] - 1)
            logging.debug(f"res: {res}")
            logging.debug(f"len is zero fuck coordinates: {current}")
            return np.average(res)

        for i in range(length):
            for j in range(length):
                logging.debug(f"x {j} y {i}")
                if self.fixed.x == j and self.fixed.y == i:
                    continue
                new[i][j] = self.start_grid[i][j] + get_min_at(i, j)
        self.grid = new.copy()
        logging.info(f"intermediate value grid:\n{str(self.grid)}")
        return

    def policy_iteration(self):
        # grid is always quadratic simplified
        length = len(self.grid)
        new = self.grid.copy()

        def get_min_at(y, x):
            current = Point(x, y)
            res = []
            for dir in direction:
                logging.debug(f"dir {dir.x} {dir.y}")
                if (
                    current.x + dir.x < 0
                    or current.x + dir.x >= length
                    or current.y + dir.y < 0
                    or current.y + dir.y >= length
                ):
                    continue
                else:
                    logging.debug("else")
                    res.append(self.grid[current.y + dir.y][current.x + dir.x] - 1)
            logging.debug(res)
            return max(res)

        for i in range(length):
            for j in range(length):
                logging.debug(f"x {j} y {i}")
                if self.fixed.x == j and self.fixed.y == i:
                    continue
                new[i][j] = self.start_grid[i][j] + get_min_at(i, j)

        self.grid = new
        return

    def copy(self):
        return RLGrid(self.grid.copy(deep=True), self.fixed)


def parse_args():
    parser = argparse.ArgumentParser(
        "this is a simple program that can evaluate the iterative and the evaluation policy for some grid"
    )
    parser.add_argument("--file", type=str, default=None, help="grid file")
    parser.add_argument("-x", type=int, default=0, help="x value of the fixed point")
    parser.add_argument("-y", type=int, default=0, help="y value of the fixed point")
    parser.add_argument("-d", type=int, help="dimension of the grid")
    return parser.parse_args()


def main():
    args = parse_args()
    data = pd.DataFrame()
    int_row = [0 for _ in range(args.d if args.d else 0)]
    logging.debug(args)
    if args.d and args.file:
        logging.debug("took the file dim path")
        with open(args.file, "r") as f:
            lines = f.readlines()
            data = []
            for line in lines:
                row = line.split(" ")
                for idx, i in enumerate(row):
                    logging.warning(f"{i}")
                    int_row[idx] = int(i)
                data.append(int_row.copy())
        data = pd.DataFrame(data, dtype=float)
    if not args.file and args.d:
        logging.debug("took the only dim path")
        data = create(args.d, args.d, dtype=float)
    if not (args.file or args.d):
        logging.debug("took the default path")
        data = create(4, 4, dtype=float)

    rl = RLGrid(data, Point(args.y, args.x))
    print(rl.grid)
    rl1 = rl.copy()
    for _ in range(10):
        rl.policy_evaluation()
    for _ in range(10):
        rl1.policy_iteration()
    print(rl.grid)
    print(rl1.grid)


if __name__ == "__main__":
    main()
