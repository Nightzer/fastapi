from model.book import Book


class ResourceBook:
    def to_json(self, book: Book) -> object:
        return {
            'id': book.id,
            'title': book.title,
            'author': book.author,
            'category': book.category,
            'rating': book.rating,
        }
