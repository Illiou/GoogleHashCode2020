from utilities import *
from algorithm import *


# ---------------- Settings ----------------

DEBUG = True
RUN_ALL = False
RUN_ONE = not RUN_ALL

INPUT_PATH = "./input/"
ALL_PROBLEM_FILES = ["a_example.txt", "b_read_on.txt", "c_incunabula.txt", "d_tough_choices.txt", "e_so_many_books.txt", "f_libraries_of_the_world.txt"]

PROBLEM_NUM = 0
PROBLEM_FILE = ALL_PROBLEM_FILES[PROBLEM_NUM]

OUTPUT_PATH = "./output/"

RUN_TIME = get_current_time_for_filename()

# ---------------- Run Single Input ----------------

if RUN_ONE:
    start_time = current_milli_time()
    input = load_input_file(INPUT_PATH + PROBLEM_FILE)
    if DEBUG:
        print(input)
    algo = Algorithm(input, debug=DEBUG)
    algo.find_solution()
    end_time = current_milli_time()

    if algo.verify_solution():
        solution_score = algo.score_solution()
        if DEBUG:
            print(f"Solution score: {solution_score}")
        filename = f"problem-{PROBLEM_NUM}_score-{solution_score}_{RUN_TIME}.txt"
        save_solution_file(algo.solution, OUTPUT_PATH + filename)
    else:
        print("Solution invalid")
        print(algo.solution)
        print()

    print(f"Finished in {end_time - start_time} ms")


# ---------------- Run All ----------------

if RUN_ALL:
    for file in ALL_PROBLEM_FILES:
        input = load_input_file(INPUT_PATH + file)
        # run algo
