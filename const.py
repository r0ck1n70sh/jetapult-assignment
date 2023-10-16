def get_static_filepath():
    curr_dir = __file__
    return curr_dir.replace("const.py", "static")


STATIC_DIR = get_static_filepath()
