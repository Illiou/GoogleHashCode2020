import numpy as np

class Algorithm:
    def __init__(self, book_scores, available_days, libraries, debug=False):
        self.debug = debug

        self.books_count = len(self.book_scores)
        self.book_scores = book_scores
        self.books_by_score = self.sort_books_by_score()
        
        self.solution = None
        self.scanned_books = set()
        self.remaining_days = available_days
        
        self.libs_by_book_hash = self.create_libs_by_book_hash(libraries)

        # TODO libraries?

    def create_libs_by_book_hash(self, libraries):
        libs_by_books = {}
        for i in range(self.books_count):
            libs_by_books[i] = []
            for lib in libraries:
                if i in lib.books:
                    libs_by_books[i].append(lib)
        return libs_by_books
        

    def sort_books_by_score(self):
        return np.argsort(self.book_scores, reverse=True)

    def find_solution(self):
        self.solution = []
        for i in range(self.books_count):
            curr_book = self.books_by_score[i]
            if curr_book in self.scanned_books:
                # book is already scanned
                continue
            library_list = self.libs_by_book_hash[curr_book] # not implemented yet
            
            scores = [lib.estimated_score(self.remaining_days) for lib in library_list]
            lib_selected = library_list[np.argmax(scores)]
            
            books_in_lib = lib_selected.get_scanned_books(self.remaining_days) # ?? somehow get the books in the chosen library which can be scanned in the remaining days
            # TODO: save books_in_lib für die solution
            self.solution.append((lib_selected.index, books_in_lib))
            
            # add the library to our solution
            # add all book feasible in the remaining time and add to scanned books    
            self.scanned_books.union(books_in_lib) # TODO: as set such that unique books

            self.remaining_days -= lib_selected.days_to_signup

        return self.solution

    def verify_solution(self):
        return True

    def score_solution(self):
        return sum(self.book_scores[b] for _, books in self.solution for b in books)
            




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
        return sorted_tuples[0, :num_books]

    def estimated_score(self, remaining_days):
        productive_days = remaining_days - self.days_to_signup
        num_books = productive_days * self.scans_per_day 
        if not self.sorted:
            self.sort_books() # create sorted_tuples array
        score_sum = sum(self.sorted_tuples[1, :num_books])
        return score_sum # self.books[:num_books]
    
    def sort_books(self):
        self.books.sort(key=self.scores)
        sorted_books = 
        sorted_scores = 
        self.sorted_tuples = np.asarray([sorted_books, sorted_scores])
        self.sorted = True
        