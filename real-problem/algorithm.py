import numpy as np
from collections import defaultdict

class Algorithm:
    def __init__(self, book_scores, available_days, library_tuples, debug=False):
        self.debug = debug
        self.library_tuples = library_tuples

        self.books_count = len(book_scores)
        self.book_scores = book_scores
        self.books_by_score = self.sort_books_by_score()
        self.library_tuples = library_tuples
        
        self.solution = None
        self.scanned_books = set()
        self.processed_libraries = set()
        self.remaining_days = available_days
        
        self.libs_by_book_hash = self.create_libs_by_book_hash(library_tuples)

        # TODO libraries?

    def create_libs_by_book_hash(self, library_tuples):
        if self.debug:
            print("create libs hash")
        # libs_by_books = {}
        # for i in range(self.books_count):
        #     libs_by_books[i] = []
        #     for lib_index, (signup_days, scanning_count, books) in enumerate(library_tuples):
        #         lib = Library(lib_index, books, self.book_scores, signup_days, scanning_count)
        #         if i in lib.books:
        #             libs_by_books[i].append(lib)

        libs_by_books = defaultdict(list)
        for lib_index, (signup_days, scanning_count, books) in enumerate(library_tuples):
            lib = Library(lib_index, books, self.book_scores, signup_days, scanning_count)
            for i in books:
                libs_by_books[i].append(lib)
        return libs_by_books
        

    def sort_books_by_score(self):
        if self.debug:
            print("start sort books")
        return sorted(range(len(self.book_scores)), key=lambda x:self.book_scores[x], reverse=True)

    def find_solution_2(self):
        signup_times = [lib[0] for lib in self.library_tuples]
        sort_ind = np.argsort(signup_times)
        self.solution = []
        for s in sort_ind:
            if self.remaining_days <= 0:
                break
            self.remaining_days -= self.library_tuples[s][0]
            self.solution.append((s, self.library_tuples[s][2]))
        return self.solution
            

    def find_solution(self):

        self.solution = []
        for i in range(self.books_count):
            if self.remaining_days <= 0:
                break
            curr_book = self.books_by_score[i]
            if curr_book in self.scanned_books:
                # book is already scanned
                continue
            if self.debug:
                print(curr_book)
                print(self.processed_libraries)
            library_list = [lib for lib in self.libs_by_book_hash[curr_book] if lib.index not in self.processed_libraries]
            if len(library_list) == 0:
                continue     
            scores = [lib.estimated_score(self.remaining_days) if lib.index not in self.processed_libraries else 0 for lib in library_list]
            if self.debug:
                print(scores)
            lib_selected = library_list[np.argmax(scores)]
            
            self.processed_libraries = self.processed_libraries.union([lib_selected.index])
            
            books_in_lib = lib_selected.get_scanned_books(self.remaining_days)
            if len(books_in_lib) == 0:
                continue
            
            if self.debug:
                print("library", lib_selected.index, books_in_lib)
            self.solution.append((lib_selected.index, books_in_lib))
            
            # add the library to our solution
            # add all book feasible in the remaining time and add to scanned books    
            self.scanned_books.union(books_in_lib)

            self.remaining_days -= lib_selected.days_to_signup

        return self.solution

    def find_solution_2(self):
        signup_times = [lib[0] for lib in self.library_tuples]
        sort_ind = np.argsort(signup_times)
        self.solution = []
        for s in sort_ind:
            if self.remaining_days <= 0:
                break
            self.remaining_days -= self.library_tuples[s][0]
            self.solution.append((s, self.library_tuples[s][2]))
        return self.solution

    def verify_solution(self):
        return True

    def score_solution(self):
        scanned_books = set(b for _, books in self.solution for b in books)
        return sum(self.book_scores[b] for b in scanned_books)
            




class Library:
    def __init__(self, index, books, scores, days_to_signup, scans_per_day):
        self.index = index
        self.books = books
        self.scores = scores
        self.days_to_signup = days_to_signup
        self.scans_per_day = scans_per_day
        self.sorted = False
        self.sorted_tuples = None # [[book_id, book_score]] # zeilen löschen wenn buch schon vorhanden

    def get_scanned_books(self, remaining_days):
        num_books = (remaining_days - self.days_to_signup) * self.scans_per_day 
        return self.sorted_tuples[0, :num_books]

    def estimated_score(self, remaining_days):
        productive_days = remaining_days - self.days_to_signup
        num_books = productive_days * self.scans_per_day 
        if not self.sorted:
            self.sort_books() # create sorted_tuples array
        score_sum = sum(self.sorted_tuples[1, :num_books])
        return score_sum # self.books[:num_books]
    
    def sort_books(self):
        scores_filtered = [self.scores[j] for j in range(len(self.scores)) if j in self.books]
        indexes = list(range(len(self.books)))
        indexes.sort(key=scores_filtered.__getitem__, reverse=True)
        sorted_books = list(map(self.books.__getitem__, indexes))
        sorted_scores = list(map(scores_filtered.__getitem__, indexes))
        self.sorted_tuples = np.asarray([sorted_books, sorted_scores])
        self.sorted = True
        