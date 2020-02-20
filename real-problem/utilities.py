import time


def current_milli_time():
    return round(time.perf_counter() * 1000)


def get_current_time_for_filename():
    return time.strftime("%Y-%m-%d_%H-%M-%S")


def load_input_file(filepath):
    with open(filepath, "r") as f:
        total_book_count, library_count, available_days = f.readline().split()
        total_books = f.readline().split()
        libraries = []
        for i, line in enumerate(f):
            if i % 2 == 0:
                book_count, signup_days, shipping_count = line.split()
            else:
                books = line.split()
                libraries.append((signup_days, shipping_count, books))
    return total_books, available_days, libraries


def save_solution_file(solution, filepath):
    with open(filepath, "w"):
        # TODO Solution object or not?
        pass
