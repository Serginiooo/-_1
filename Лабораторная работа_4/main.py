if __name__ == "__main__":
    class BoardGame:
        """ Базовый класс настольные игры. """

        def __init__(self, name: str, audience: str):
            self._name = name
            self._audience = audience

        @property
        def name(self) -> str:
            return self.name

        @property
        def author(self) -> str:
            return self.author

        def __str__(self):
            return f"Настольная игра {self.name}. Предназначена для {self.audience}"

        def __repr__(self):
            return f"{self.__class__.__name__}(name={self.name!r}, audience={self.audience!r})"


    class EuroGame(BoardGame):
        """ Евроигры. Дочерний класс класса настольные игры."""
        def __init__(self, level_of_difficulty: int, name: str, audience: str):
            super().__init__(name, audience)
            self.level_of_difficulty = level_of_difficulty

        """ Метод проверяет, проходит ли уровень сложности необходимые ограничения"""
        def checks(self, level_of_difficulty: int) -> None:
            if not isinstance(level_of_difficulty, int):
                raise TypeError("Уровень сложности должен быть типа int")
            if level_of_difficulty <= 0:
                raise ValueError("Уровень сложности быть положительным числом")

        def __str__(self):
            return f"Настольная игра {self.name}. Предназначена для {self.author}.Уровень сложности {self.level_of_difficulty}"

        def __repr__(self):
            return f"{self.__class__.__name__}(name={self.name!r}, audience={self.audience!r}, level_of_difficulty={self.level_of_difficulty!r})"


    class AmericanTrash(BoardGame):
        """ Американ Трэш. Дочерний класс класса настольные игры."""
        def __init__(self, recommended_players: int, name: str, audience: str):
            super().__init__(name, audience)
            self.recomended_players = recommended_players

        """ Метод проверяет, проходит ли рекомендованное число игроков необходимые ограничения"""
        def checkkk(self, recommended_players: int) -> None:
            if not isinstance(recommended_players, int):
                raise TypeError("Рекомендованное число игроков должно быть типа float")
            if recommended_players <= 0:
                raise ValueError("Рекомендованное число игроков должно быть положительным числом")

        def __str__(self):
            return f"Настольная игра {self.name}. Предназначена для {self.author}.Рекомендованное число игроков {self.recomended_players}"
        def __repr__(self):
            return f"{self.__class__.__name__}(name={self.name!r}, audience={self.audience!r}, level_of_difficulty={self.recomended_players!r})"

    # Write your solution here
    pass
