class Response:
    book_response = str

    def __init__(self, book_response):
        self.book_response = book_response

    def __str__(self):
        return '%s' % self.book_response
