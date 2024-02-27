class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        return self.name

    @property
    def author(self) -> str:
        return self.author
    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, pages: int, name: str, author: str):
        super().__init__(name, author)
        self.pages = pages

    def checking(self, pages: int) -> None:
        if not isinstance(pages, int):
            raise TypeError("Число страниц должно быть типа int")
        if pages <= 0:
            raise ValueError("Число страниц должно быть положительным числом")
    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}.Страниц {self.author}"
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    def __init__(self, duration: float, name: str, author: str):
        super().__init__(name, author)
        self.duration = duration
    def check(self, duration: float) -> None:
        if not isinstance(duration, float):
            raise TypeError("Продолжительность должна быть типа float")
        if duration <= 0:
            raise ValueError("Продолжительность должна быть положительным числом")
    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Продолжительность {self.duration} "
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"
