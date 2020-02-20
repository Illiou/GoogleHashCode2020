from .utilities import *
from .algorithm import *


# ---------------- Settings ----------------

DEBUG = True
RUN_ALL = False
RUN_ONE = not RUN_ALL

INPUT_PATH = "./input/"
ALL_PROBLEM_FILES = ["a_example.in", "b_small.in", "c_medium.in", "d_quite_big.in", "e_also_big.in"]
PROBLEM_FILE = ALL_PROBLEM_FILES[0]

OUTPUT_PATH = "./output/"


# ---------------- Run Single Input ----------------

if RUN_ONE:
    input = load_input_file(INPUT_PATH + PROBLEM_FILE)
    print(input)


# ---------------- Run All ----------------

if RUN_ALL:
    for file in ALL_PROBLEM_FILES:
        input = load_input_file(INPUT_PATH + file)
        # run algo
