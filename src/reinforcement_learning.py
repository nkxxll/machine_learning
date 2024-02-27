#!/usr/bin/env python3
import logging

import pandas as pd

logging.basicConfig(level=logging.INFO)


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __eq__(self, other) -> bool:
        return True if self.x == other.x and self.y == other.y else False


direction = [Point(-1, 0), Point(1, 0), Point(0, 1), Point(0, -1)]


def create(x, y) -> pd.DataFrame:
    data = []
    row = [0 for _ in range(x)]
    for _ in range(y):
        data.append(row)

    return pd.DataFrame(data)


class RLGrid:
    def __init__(self, x: pd.DataFrame, fixed: Point):
        self.grid = x
        self.fixed = fixed

    def update(self):
        pass

    def policy_evaluation(self):
        pass

    def policy_iteration(self):
        # grid is always quadratic simplified
        length = len(self.grid)
        new = self.grid.copy()

        def get_min_at(y, x):
            current = Point(x, y)
            res = []
            for dir in direction:
                logging.info(f"dir {dir.x} {dir.y}")
                if (
                    current.x + dir.x < 0
                    or current.x + dir.x >= length
                    or current.y + dir.y < 0
                    or current.y + dir.y >= length
                ):
                    continue
                else:
                    logging.info("else")
                    res.append(self.grid[current.y + dir.x][current.x + dir.x] - 1)
            logging.info(res)
            return max(res)

        for i in range(length):
            for j in range(length):
                logging.info(f"x {j} y {i}")
                if self.fixed.x == j and self.fixed.y == i:
                    continue
                new[i][j] = get_min_at(i, j)

        self.grid = new
        return


def main():
    rl = RLGrid(create(4, 4), Point(0, 0))
    rl.policy_iteration()
    print(rl.grid)


if __name__ == "__main__":
    main()
