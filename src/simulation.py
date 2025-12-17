import random
from models import EBook, PaperBook
from core import Library
from errors import LibraryError


def run_simulation(steps: int = 20, seed: int | None = None) -> None:
    if seed is not None:
        random.seed(seed)

    library = Library()

    authors = ["Лев Толстой", "Фёдор Достоевский", "Александр Пушкин", "Джордж Оруэлл", "Рэй Брэдбери"]
    genres = ["Классика", "Антиутопия", "Фантастика", "Драма"]
    titles = ["Путь домой", "Секреты кода", "Ночные тени", "В поисках истины", "Зеркала времени"]

    for step in range(1, steps + 1):
        print(f"{step}. ", end="")
        try:
            event = random.randint(1, 5)
            if event == 1:  # Добавление книги
                is_ebook = random.randint(0, 1)
                common_params = {
                    "title": random.choice(titles),
                    "author": random.choice(authors),
                    "year": random.randint(1900, 2024),
                    "genre": random.choice(genres),
                    "isbn": f"ISBN-{random.randint(0, 999999)}"
                }
                if is_ebook:
                    book = EBook(**common_params, file_size=random.randint(1, 100))
                else:
                    book = PaperBook(**common_params, cover=random.choice(["твердой", "мягкой"]))
                library.add_book(book)
            elif event == 2:  # Удаление книги
                if not library.books.is_empty():
                    all_books_list = list(library.books)
                    target = random.choice(all_books_list)
                    library.remove_book(target)
                else:
                    print("Событие: попытка удаления. Библиотека пуста.")
            elif event == 3:  # Поиск по автору
                author = random.choice(authors)
                result = library.find_by_author(author)
                print(f"Поиск автора {author}: найдено {len(result)} книг")
            elif event == 4:  # Поиск по isbn
                isbn = f"ISBN-{random.randint(0, 999999)}"
                print(f"Поиск книги {isbn}")
                result = library.find_by_isbn(isbn)
                print(f"    Результат: найдена книга {result.title}.")
            elif event == 5:  # Фильтрация
                genre = random.choice(genres)
                result = library.books.filter_by_criteria(genre=genre)
                print(f"Фильтр по жанру {genre}: найдено {len(result)} книг")
        except LibraryError as e:
            print(f"{e}")
        except Exception as e:
            print(f"{e}")
    print(f"\nИтоговое состояние: {library}")
