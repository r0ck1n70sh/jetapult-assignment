import json

from const import STATIC_DIR
from grid.grid import Grid
from trie.trie import Trie


def get_level_template():
    level_template_file = open(STATIC_DIR + "/level_template.json")
    return json.load(level_template_file)


def get_found_positions(str_, trie, words) -> dict:
    str_positions = {}
    positions = []

    for idx in range(0, len(str_)):
        elem_str = str_[idx: len(str_) + 1]
        indices = trie.contains(elem_str)
        positions_ = list(map(lambda end_idx: (idx, idx + end_idx), indices))
        positions.extend(positions_)

    for [start, end] in positions:
        found_str = str_[start: end + 1]

        if found_str in words:
            str_positions[found_str] = (start, end)

        reverse_str = found_str[::-1]
        if reverse_str in words:
            str_positions[reverse_str] = (end, start)

    return str_positions


if __name__ == '__main__':
    template = get_level_template()

    grid = Grid(
        characters=template.get("boardCharacters"),
        rows=template.get("rows"),
        cols=template.get("cols")
    )

    print(grid)
    # Time Complexity: O (( r*r + r*c + c*c ) * l)
    # r -> row, c -> col, l -> max length in words

    # Space Complexity: O ( r + c + W )
    # W -> total no. chars in words

    words = template.get("words")

    trie = Trie()

    for word in words:
        reverse = word[::-1]

        trie.insert(word)
        trie.insert(reverse)

    found_positions = {}

    row_str_list = grid.get_all_row_str_list()
    for r in range(0, grid.rows):
        row_str = row_str_list[r]
        row_positions = get_found_positions(str_=row_str, trie=trie, words=words)

        for word, pos in row_positions.items():
            found_positions[word] = {
                "row": r,
                "col": pos[0],
                "v": 0,
                "h": 1 if pos[0] <= pos[1] else -1
            }

    col_str_list = grid.get_all_col_str_list()
    for c in range(0, grid.cols):
        col_str = col_str_list[c]
        col_positions = get_found_positions(str_=col_str, trie=trie, words=words)

        for word, pos in col_positions.items():
            found_positions[word] = {
                "row": pos[0],
                "col": c,
                "h": 0,
                "v": 1 if pos[0] <= pos[1] else -1
            }

    col_dia_str_list = grid.get_all_col_diagonals(direction=-1)
    for c in range(0, grid.cols):
        col_dia_str = col_dia_str_list[c]
        col_dia_positions = get_found_positions(str_=col_dia_str, trie=trie, words=words)

        for word, pos in col_dia_positions.items():
            if found_positions.get(word, None) is not None:
                continue

            found_positions[word] = {
                "row": pos[0],
                "col": c - pos[0],
                "h": -1 if pos[0] <= pos[1] else 1,
                "v": 1 if pos[0] <= pos[1] else 1
            }

    row_dia_str_list = grid.get_all_row_diagonals(direction=-1)
    for r in range(0, grid.rows):
        row_dia_str = row_dia_str_list[r]
        row_dia_positions = get_found_positions(str_=row_dia_str, trie=trie, words=words)

        for word, pos in row_dia_positions.items():
            if found_positions.get(word, None) is not None:
                continue

            found_positions[word] = {
                "row": r - pos[0],
                "col": pos[0],
                "h": 1 if pos[0] <= pos[1] else -1,
                "v": -1 if pos[0] <= pos[1] else 1
            }

    col_dia_str_list = grid.get_all_col_diagonals(direction=1)
    for c in range(0, grid.cols):
        col_dia_str = col_dia_str_list[c]
        col_dia_positions = get_found_positions(str_=col_dia_str, trie=trie, words=words)

        for word, pos in col_dia_positions.items():
            if found_positions.get(word, None) is not None:
                continue

            found_positions[word] = {
                "row": pos[0],
                "col": c + pos[0],
                "h": 1 if pos[0] <= pos[1] else -1,
                "v": 1 if pos[0] <= pos[1] else -1
            }

    row_dia_str_list = grid.get_all_row_diagonals(direction=1)
    for r in range(0, grid.rows):
        row_dia_str = row_dia_str_list[r]
        row_dia_positions = get_found_positions(str_=row_dia_str, trie=trie, words=words)

        for word, pos in row_dia_positions.items():
            if found_positions.get(word, None) is not None:
                continue

            found_positions[word] = {
                "row": r + pos[0],
                "col": pos[0],
                "h": 1 if pos[0] <= pos[1] else -1,
                "v": 1 if pos[0] <= pos[1] else -1
            }

    print(found_positions)