# Задание 1
# Создайте класс, описывающий книгу. Он должен содержать информацию об авторе, названии, годе издания и жанре.
# Создайте несколько разных книг. Определите для него операции проверки на равенство и неравенство,
# методы __repr__ и __str__.

from response import Response


class Book:
    name = str
    author = str
    year = int
    book_genre = str
    book_responses = []

    def __init__(self, name, author, year, book_genre, book_responses):
        self.name = name
        self.author = author
        self.year = year
        self.book_genre = book_genre
        self.book_responses = book_responses

    def add_response(self, response):
        if type(response) != Response:
            return False
        self.book_responses.append(response)

    def __eq__(self, other):
        if type(other) != Book:
            return False
        if self.name != other.name:
            return False
        elif self.author != other.author:
            return False
        elif self.year != other.year:
            return False
        elif self.book_genre != other.book_genre:
            return False
        else:
            return True

    def __repr__(self):
        return '-----%s, %s, %d, %s' % (self.name, self.author, self.year, self.book_genre)

    def __str__(self):
        returned_str = 'The book %s, %s, %d, %s' % (self.name, self.author, self.year, self.book_genre)
        if len(self.book_responses) != 0:
            for resp in self.book_responses:
                returned_str += '\n' + resp.__str__()
        return returned_str


genre = 'Science fiction'
asimov = 'Isaac Asimov'

book1 = Book('Foundation', asimov, 1951, genre, [])
book2 = Book('Foundation and Empire', asimov, 1952, genre, [])
book3 = Book('Second Foundation', asimov, 1953, genre, [])

if book1 == book3:
    print('The books are equal.')
else:
    print('The books are not equal.')

resp1 = Response('First resp.')
resp2 = Response('Second resp - trulala.')

book2.add_response(resp1)
book3.add_response(resp2)

print(book2)
print(book3)
