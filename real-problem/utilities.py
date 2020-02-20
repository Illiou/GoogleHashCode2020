import time


def current_milli_time():
    return round(time.perf_counter() * 1000)


def get_current_time_for_filename():
    return time.strftime("%Y-%m-%d_%H-%M-%S")


def load_input_file(filepath):
    with open(filepath, "r") as f:
        total_book_count, library_count, available_days = str_array_to_int_array(f.readline().split())
        book_scores = str_array_to_int_array(f.readline().split())
        libraries = []
        for i, line in enumerate(f):
            if line.strip() == "":
                continue
            if i % 2 == 0:
                book_count, signup_days, scanning_count = str_array_to_int_array(line.split())
            else:
                books = str_array_to_int_array(line.split())
                libraries.append((signup_days, min(scanning_count, book_count), books))
    return book_scores, available_days, libraries


def str_array_to_int_array(strings):
    return [int(s) for s in strings]


def int_array_to_string_array(ints):
    return [str(i) for i in ints]


def save_solution_file(signed_up_libraries, filepath):
    """
    :param signed_up_libraries(list((lib_index, list(scanned books)))): solution libraries
    :param filepath
    """
    with open(filepath, "w") as f:
        signed_up_count = len(signed_up_libraries)
        f.write(f"{signed_up_count}\n")
        for lib_index, books in signed_up_libraries:
            f.write(f"{lib_index} {len(books)}\n")
            f.write(" ".join(int_array_to_string_array(books)) + "\n")
