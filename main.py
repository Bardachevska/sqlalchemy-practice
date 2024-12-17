from sqlalchemy.orm import sessionmaker
from models import create_database, Author, Category, Book

# Создание сессии
engine = create_database()
Session = sessionmaker(bind=engine)
session = Session()

# Функции работы с данными
def insert_author(name):
    author = Author(name=name)
    session.add(author)
    session.commit()
    return author

def insert_category(name):
    category = Category(name=name)
    session.add(category)
    session.commit()
    return category

def insert_book(title, author_id, category_id):
    book = Book(title=title, author_id=author_id, category_id=category_id)
    session.add(book)
    session.commit()
    return book

def get_author_by_id(author_id):
    return session.query(Author).filter_by(id=author_id).first()

def get_all_books():
    return session.query(Book).all()

def update_book(book_id, title=None, author_id=None, category_id=None):
    book = session.query(Book).filter_by(id=book_id).first()
    if not book:
        return None
    if title:
        book.title = title
    if author_id:
        book.author_id = author_id
    if category_id:
        book.category_id = category_id
    session.commit()
    return book

def delete_author(author_id):
    author = session.query(Author).filter_by(id=author_id).first()
    if author:
        session.delete(author)
        session.commit()

def delete_book(book_id):
    book = session.query(Book).filter_by(id=book_id).first()
    if book:
        session.delete(book)
        session.commit()

# Примеры использования
if __name__ == '__main__':
    # Добавление данных
    author1 = insert_author("George Orwell")
    category1 = insert_category("Dystopian")
    book1 = insert_book("1984", author1.id, category1.id)

    # Получение данных
    print(f"Author by ID: {get_author_by_id(author1.id).name}")
    print("All books:")
    for book in get_all_books():
        print(f"{book.title} by {book.author.name}")

    # Обновление книги
    updated_book = update_book(book1.id, title="Animal Farm")
    print(f"Updated Book: {updated_book.title}")

    # Удаление данных
    delete_book(book1.id)
    delete_author(author1.id)
