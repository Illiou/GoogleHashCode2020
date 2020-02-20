import time


def current_milli_time():
    return round(time.perf_counter() * 1000)


def get_current_time_for_filename():
    return time.strftime("%Y-%m-%d-%H-%M-%S")


def load_input_file(filepath):
    with open(filepath, "r") as f:
        lines = f.readlines()
        slices_max, type_count = lines[0].split()
        pizza_types = lines[1].split()
    return slices_max, type_count, pizza_types


def save_solution_file(solution, filepath):
    with open(filepath, "w"):
        # TODO Solution object or not?
        pass
