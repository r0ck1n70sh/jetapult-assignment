import json

from const import STATIC_DIR


class Grid:
    def __init__(self, rows, cols, characters):
        self.rows = rows
        self.cols = cols
        self.characters = characters

    def get(self, row: int, col: int) -> str:
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            return ""

        return self.characters[row][col]

    def get_all_row_str_list(self) -> list:
        row_str_list = []

        for r in range(0, self.rows):
            row_str = ""

            for c in range(0, self.cols):
                ch = self.get(row=r, col=c)
                row_str += ch

            row_str_list.append(row_str)

        return row_str_list

    def get_all_col_str_list(self) -> list:
        col_str_list = []

        for c in range(0, self.cols):
            col_str = ""

            for r in range(0, self.rows):
                ch = self.get(row=r, col=c)
                col_str += ch

            col_str_list.append(col_str)

        return col_str_list

    def get_all_row_diagonals(self, direction: int) -> list:
        dia_str_list = []

        for r in range(0, self.rows):
            dia_str = ""

            for c in range(0, self.cols):
                ch = self.get(row=r + direction * c, col=c)
                dia_str += ch

            dia_str_list.append(dia_str)

        return dia_str_list

    def get_all_col_diagonals(self, direction: int) -> list:
        dia_str_list = []

        for c in range(0, self.cols):
            dia_str = ""

            for r in range(0, self.rows):
                ch = self.get(row=r, col=c + direction * r)
                dia_str += ch

            dia_str_list.append(dia_str)

        return dia_str_list

    def __str__(self):
        rows_str = map(lambda row: " ".join(row), self.characters)
        return "\n".join(rows_str)
