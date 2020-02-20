import numpy as np


class Algorithm:
    def __init__(self, _input, debug=False):
        self.input = _input
        self.debug = debug
        self.solution = None

    def find_solution(self):
        self.solution = (0,)

    def verify_solution(self):
        pass

    def score_solution(self):
        pass
