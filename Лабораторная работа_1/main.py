# TODO Написать 3 класса с документацией и аннотацией типов
class SchoolClass:
    def __init__(self, number: int, literal: str, pupil: int):
        """
        Создание и подготовка к работе объекта "Школьный класс"

        :param number: Номер класса
        :param literal: Буква класса
        :param pupil: Количество учеников класса
        Примеры:
        >>> school_class = SchoolClass(9, "Б", 22 )  # инициализация экземпляра класса
        """
        if not isinstance(number, int):
            raise TypeError("Номер класса должен быть типа int")
        if number <= 0:
            raise ValueError("Номер класса должен быть положительным числом")
        if number > 11:
            raise ValueError("Номер класса должен быть от 1 до 11")
        self.number = number

        if not isinstance(literal, str):
            raise TypeError("Буква класса должна быть типа str")
        if literal.islower():
            raise ValueError("Буква класса не может быть строчной буквой")
        self.literal = literal

        if not isinstance(pupil, int):
            raise TypeError("Количество учеников класса должно быть типа int")
        if pupil <= 15:
            raise ValueError("Количество учеников класса должно быть больше 15")
        if pupil > 30:
            raise ValueError("Количество учеников класса должно быть меньше 31")
        self.pupil = pupil

    def is_elementary_class(self) -> bool:
        """
        Функция которая проверяет является ли класс классом начальной школы

        :return: Является ли класс классом начальной школы

        Примеры:
        >>> school_class = SchoolClass(2, "Д", 26)
        >>> school_class.is_elementary_class()
        """
        ...

    def add_pupil_class(self, new_pupils: int) -> None:
        """
        Добавление учеников в класс.
        :param new_pupils: новые ученики

        :raise ValueError: Если количество учеников в классе превышает предельно допустимое, то вызываем ошибку

        Примеры:
        >>> school_class = SchoolClass(3, "Г", 18)
        >>> school_class.add_pupil_class(2)
        """
        if not isinstance(new_pupils, int):
            raise TypeError("Добавляемое количество учеников в класс должно быть типа int")
        if new_pupils < 0:
            raise ValueError("Добавляемое количество учеников в класс должно быть положительным числом")
        ...



class Sneakers:
    def __init__(self, size: int, country: str, price: float):
        """
        Создание и подготовка к работе объекта "Школьный класс"

        :param size: Размер класса
        :param country: Страна производства класса
        :param price: Цена класса
        Примеры:
        >>> sneakers = Sneakers(36, "Вьетнам", 12000.0 )  # инициализация экземпляра класса
        """
        if not isinstance(size, int):
            raise TypeError("Размер кроссовок должен быть типа int")
        if size <= 30:
            raise ValueError("Размер кроссовок должен быть от 30 до 50")
        if size > 50:
            raise ValueError("Размер кроссовок должен быть от 30 до 50")
        self.size = size

        if not isinstance(country, str):
            raise TypeError("Страна производства должна быть типа str")
        if country not in ["Россия", "Китай", "Индия", "Вьетнам", "Индонезия"]:
            raise ValueError("Указана несуществующая страна производства")
        self.country = country

        if not isinstance(price, float):
            raise TypeError("Цена должна быть типа float")
        if price <= 0:
            raise ValueError("Цена должна быть величиной положительной")
        self.price = price

    def is_russian_sneakers(self) -> bool:
        """
        Функция которая проверяет являются ли кроссовки кроссовками отечественного производства

        :return: Относятся ли кроссовки к отечественному производству

        Примеры:
        >>> sneakers = Sneakers(43, "Россия", 7229.0)
        >>> sneakers.is_russian_sneakers()
        """
        ...

    def add_discount(self, discount: float) -> None:
        """
        Добавление скидки.
        :param discount: Скидка

        :raise ValueError: Если размер скидки составляет больше чем 30% от цены кроссовок, вызываем ошибку

        Примеры:
        >>> sneakers = Sneakers(42, "Индонезия", 15500.32)
        >>> sneakers.add_discount(1250.0)
        """
        if not isinstance(discount, float):
            raise TypeError("Скидка на кроссовки должна быть типа float")
        if discount < 0:
            raise ValueError("Скидка на кроссовки должна быть положительным числом")
        ...



class NationalRuler:
    def __init__(self, duration_of_reign: float, name_and_surname: str, century: int):
        """
        Создание и подготовка к работе объекта "Школьный класс"

        :param duration_of_reign: Продолительность правления
        :param name_and_surname: Имя и фамилия
        :param century: Век правления
        Примеры:
        >>> leader = NationalRuler(9.0, "Сильвио Берлускони", 21 )  # инициализация экземпляра класса
        """
        if not isinstance(duration_of_reign, float):
            raise TypeError("Продолжительность правления должна быть типа float")
        if duration_of_reign <= 0:
            raise ValueError("Продолжительность правления должна быть положительной величиной")
        self.duration_of_reign = duration_of_reign

        if not isinstance(name_and_surname, str):
            raise TypeError("Имя и фамилия должны быть типа str")
        self.name_and_surname = name_and_surname

        if not isinstance(century, int):
            raise TypeError("Век правления должен быть типа int")
        if century < -8:
            raise ValueError("Век правления должен быть больше или равен восьмого до нашей эры")
        if century > 21:
            raise ValueError("Век правления должен быть в настоящем или прошлом, но не в будущем")
        self.century = century

    def is_long_time_leader(self) -> bool:
        """
        Функция которая проверяет является ли правление долгим

        :return: Относятся ли правители к долгоправящим

        Примеры:
        >>> leader = NationalRuler(25.25, "Екатерина 2", 18)
        >>> leader.is_long_time_leader()
        """
        ...

    def world_war_2(self,start_year: int) -> None:
        """
        Добавление учеников в класс.
        :param start_year: Начало правления

        :raise ValueError: Если правитель не правил хотя бы год с 1939 по 1945, вызываем ошибку

        Примеры:
        >>> leader = NationalRuler(12.0, "Адольф Гитлер", 20)
        >>> leader.world_war_2(1933)
        """
        if not isinstance(start_year, int):
            raise TypeError("Год начала правления должен быть типа int")
        if start_year < 0:
            raise ValueError("Год начала правления должен быть положительным числом")
        if start_year > 1945:
            raise ValueError("Правление началось после Второй Мировой войны")
        ...



if __name__ == "__main__":
    import doctest
    doctest.testmod()  # тестирование примеров, которые находятся в документации
if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
